#!/usr/bin/env python3

LENGTH = 16
QUANTITY = 1000

import sys
import os
import random
import string
from tqdm import tqdm
import segno

def get_args():
    """
    Get the name for the new folder that the generated QR codes will be added
    Get the base URL for the QR codes
    """
    
    folder = ''
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = input("Specify a new folder name to save the QR codes: ")
    
    if os.path.exists(folder):
        raise FileExistsError(folder)

    base_url = ''
    if len(sys.argv) > 2:
        base_url = sys.argv[2]
    else:
        base_url = input("Specify the base URL for the QR codes: ")

    args = {
        "folder": folder,
        "base_url": base_url,
    }

    for k,v in args.items():
        print(f'{k} = {v}')

    return args

def make_folder(folder):
    os.mkdir(folder)

def make_random_string(length):
    return ''.join(random.choices(string.digits + string.ascii_uppercase, k=length))

def generate_qrs(base_url, folder, quantity):
    nonces = []
    for _ in tqdm(range(quantity), desc='Generating QR codes'):
        nonce = make_random_string(LENGTH)
        value = f'{base_url}{nonce}'
        qrcode = segno.make_qr(value, error='M')
        filename = f'{nonce}.png'
        qrcode.save(os.path.join(folder, filename), scale=10)
        nonces.append(filename)
    return nonces

def write_to_file(nonces, folder):
    nonces_text = '\n'.join(nonces)
    with open(f'{folder}.csv', 'w') as f_out:
        f_out.write("QR Codes\n")
        f_out.write(nonces_text)
    print(f'QR code values saved to file: {folder}.csv')

def main():
    args = get_args()
    base_url = args["base_url"]
    folder = args["folder"]
    make_folder(folder)
    nonces = generate_qrs(base_url, folder, QUANTITY)
    write_to_file(nonces, folder)

if __name__ == '__main__':
    main()
