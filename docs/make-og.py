# Genera assets/og.jpg (1200x630) a partir de assets/ingrid.jpg.
# Uso: python3 docs/make-og.py   (requiere Pillow: pip3 install pillow)
from PIL import Image, ImageDraw, ImageFont
W, H = 1200, 630
im = Image.new("RGB", (W, H), (24, 42, 68))
photo = Image.open("assets/ingrid.jpg").convert("RGB")
pw = int(photo.width * H / photo.height)
photo = photo.resize((pw, H), Image.LANCZOS)
target_w = 480
left = (pw - target_w) // 2
photo = photo.crop((left, 0, left + target_w, H))
im.paste(photo, (W - target_w, 0))
d = ImageDraw.Draw(im)
def font(name, size):
    for p in ["/System/Library/Fonts/Supplemental/" + name, "/Library/Fonts/" + name]:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            pass
    return ImageFont.load_default()
f1, f2, f3 = font("Georgia.ttf", 64), font("Georgia.ttf", 30), font("Helvetica.ttc", 22)
x = 70
d.text((x, 150), "Ingrid Astiz", font=f1, fill=(255, 255, 255))
d.text((x, 235), "Board Member", font=f2, fill=(241, 176, 138))
d.text((x, 275), "y Consejera independiente", font=f2, fill=(241, 176, 138))
d.text((x, 360), "Tecnología, personas y", font=f3, fill=(220, 226, 235))
d.text((x, 392), "decisiones difíciles.", font=f3, fill=(220, 226, 235))
d.text((x, 540), "ingridastiz.com", font=f3, fill=(155, 180, 210))
im.save("assets/og.jpg", quality=88)
print("ok", im.size)
