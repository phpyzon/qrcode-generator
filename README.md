# QR Code Generator

This is a simple QR Code Generator written in Python. It uses the `qrcode` library to generate QR codes from input data.

## Requirements

- Python 3.x
- qrcode library (can be installed via pip)

## Installation

To install the required library, use pip:

```bash
pip install qrcode[pil]
```

## Usage

You can generate a QR code by running the script and passing the data and output file name as arguments:

```bash
python qr_code_generator.py "Your data here" output.png
```

For example:

```bash
python qr_code_generator.py "https://www.example.com" example_qr.png
```

This will generate a QR code containing the URL "https://www.example.com" and save it as example_qr.png.
