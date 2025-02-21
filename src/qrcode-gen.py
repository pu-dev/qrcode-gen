import argparse
import qrcode
# import qrcode.image.SvgImage
import qrcode.image.svg


def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        image_factory=qrcode.image.svg.SvgImage
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    with open(filename, 'wb') as f:
        f.write(qr_image.to_string())

def main():
    parser = argparse.ArgumentParser(description='Generate QR code from URL')
    parser.add_argument('url', help='URL to encode in QR code')
    parser.add_argument('--output', '-o', 
                       default='qr_code.svg',
                       help='Output filename (default: qr_code.svg)')
    
    args = parser.parse_args()
    
    try:
        generate_qr_code(args.url, args.output)
        print(f"QR code successfully generated and saved to {args.output}")
    except Exception as e:
        print(f"Error generating QR code: {e}")


if __name__ == "__main__":
    main()