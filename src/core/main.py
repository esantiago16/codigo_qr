import qrcode
from PIL import Image, ImageDraw, ImageFont
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, RoundedModuleDrawer
import os
import urllib.parse
from dotenv import load_dotenv


def generate_qr(telefono_salon,mensaje):

    print(mensaje)
    text_clean = urllib.parse.quote(mensaje)
    url_whatsapp = f"https://wa.me/{telefono_salon}?text={text_clean}"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url_whatsapp)
    print(f"URL de WhatsApp: {url_whatsapp}")
    qr.make(fit=True)

    img_qr = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    img_qr.save(f"test/qr_code.png")

    return img_qr

def main ():
    
    load_dotenv()

    telefono_salon = os.getenv("telefono")
    mensaje = f"Hola, me gustaría reservar una cita en el salón de belleza. Mi número de teléfono es {telefono_salon}."
    print(mensaje)
    print(telefono_salon)
    generate_qr(telefono_salon,mensaje)

    print("Bienvenido al generador de codigod QR personalizados")

if __name__ == "__main__":
    main()

