# generate-qr
Python script to generate QR codes for MIST badges

## Instructions
1. [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
1. Install the dependencies using `python3 -m pip install -r requirements.txt`
1. Run the command `python3 generate_qr.py`

## You will be prompted for 2 things:

### 1. Folder
This is the folder that the generated QR code images will be saved in. Make
sure that there does not already exist a folder/file with the same name.

### 2. Base URL
If the QR code points to https://example.com/?qr=RANDOM_BADGE_CODE, then the
base URL is `https://example.com?/qr=`. The `RANDOM_BADGE_CODE` will be
auto-generated.
