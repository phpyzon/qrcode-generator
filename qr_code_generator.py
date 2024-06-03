import qrcode
import argparse

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR Code saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code")
    parser.add_argument("data", help="The data to encode in the QR code")
    parser.add_argument("output_file", help="The output file for the QR code image")
    
    args = parser.parse_args()
    
    generate_qr_code(args.data, args.output_file)
