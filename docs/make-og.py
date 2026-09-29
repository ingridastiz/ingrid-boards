# Genera assets/og.jpg (1200x630) recortando docs/og-source.webp (1536x1024, creada con ChatGPT).
# Uso: python3 docs/make-og.py   (requiere Pillow: pip3 install pillow)
from PIL import Image
W, H = 1200, 630
im = Image.open("docs/og-source.webp").convert("RGB")
crop_h = round(im.width * H / W)            # 806 px para 1536 de ancho
center = 452                                # las piedras ocupan aprox. de y=80 a y=825, centro en 452
top = max(0, min(im.height - crop_h, center - crop_h // 2))
im = im.crop((0, top, im.width, top + crop_h)).resize((W, H), Image.LANCZOS)
im.save("assets/og.jpg", quality=90)
print("ok", im.size)
