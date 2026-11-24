"""Generate entry.png for news-image-20261123.
1024x1024 infographic, text drawn with PIL/DejaVu so every label is crisp.
Stories verified from 23 Nov 2026 reporting (Just Security Early Edition,
Algenom, OneTurn, BusinessWorld): COP31 collapse, Iran-US blockade standoff,
Dymer strike + Benghazi sea drones, Nvidia rebound, Democrats House win.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
BG = (247, 245, 239)
NAVY = (15, 42, 68)
GOLD = (201, 162, 39)
WHITE = (255, 255, 255)
INK = (20, 28, 38)
GREY = (84, 96, 110)

def font(name, size):
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

F_TITLE = font("DejaVuSans-Bold.ttf", 56)
F_KICKER = font("DejaVuSans-Bold.ttf", 26)
F_SUB = font("DejaVuSans.ttf", 24)
F_TAG = font("DejaVuSans-Bold.ttf", 22)
F_HEAD = font("DejaVuSans-Bold.ttf", 29)
F_BODY = font("DejaVuSans.ttf", 23)
F_FOOT = font("DejaVuSans.ttf", 20)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Header
d.rectangle([0, 0, W, 172], fill=NAVY)
d.rectangle([0, 172, W, 178], fill=GOLD)
d.text((48, 22), "WORLD NEWS  •  ONE DAY, ONE IMAGE", font=F_KICKER, fill=(201, 162, 39))
d.text((48, 58), "MONDAY 23 NOVEMBER 2026", font=F_TITLE, fill=WHITE)
d.text((48, 128), "Five stories that defined the day", font=F_SUB, fill=(200, 212, 224))

stories = [
    ("CLIMATE", (27, 120, 88), "COP31 ends with no deal",
     "UN climate talks in Antalya close two days late — the longest COP ever — with no agreement on fossil fuels or finance."),
    ("MIDDLE EAST", (178, 58, 44), "Iran defies the US blockade",
     "Tehran vows “all means” against the US naval blockade and says it downed a US drone; Trump warns strikes may resume."),
    ("UKRAINE", (38, 92, 140), "Strike kills 11 in Dymer",
     "A Russian strike hits a home near Kyiv. Ukraine says its sea drones sank a Russian ship off Libya’s Benghazi port."),
    ("MARKETS", (22, 130, 90), "Nvidia chief returns, stocks surge",
     "Jensen Huang is back as CEO, 11 days after resigning. Nvidia jumps about 33% and the S&P 500 rises 4.8%."),
    ("USA", (120, 60, 120), "Democrats win big House majority",
     "Democrats take at least 258 House seats — their largest majority since 1992 — after flipping a North Carolina seat."),
]

y = 192
ROW_H = 140
GAP = 10
for i, (tag, color, head, body) in enumerate(stories):
    x0, y0 = 36, y
    x1, y1 = W - 36, y + ROW_H
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=WHITE, outline=(220, 224, 228), width=1)
    d.rectangle([x0, y0 + 14, x0 + 10, y1 - 14], fill=color)
    # number badge
    cx, cy = x0 + 52, y0 + 44
    d.ellipse([cx - 26, cy - 26, cx + 26, cy + 26], fill=color)
    num = font("DejaVuSans-Bold.ttf", 30)
    tw = d.textlength(str(i + 1), font=num)
    d.text((cx - tw / 2, cy - 21), str(i + 1), font=num, fill=WHITE)
    tx = x0 + 96
    d.text((tx, y0 + 16), tag, font=F_TAG, fill=color)
    d.text((tx, y0 + 46), head, font=F_HEAD, fill=INK)
    # wrap body to ~62 chars
    lines = textwrap.wrap(body, width=62)
    by = y0 + 86
    for ln in lines[:2]:
        d.text((tx, by), ln, font=F_BODY, fill=GREY)
        by += 29
    y += ROW_H + GAP

# Footer
fy = y + 2
d.text((36, fy), "23 NOVEMBER 2026  •  COP31  •  IRAN  •  UKRAINE  •  MARKETS  •  WASHINGTON", font=F_FOOT, fill=GREY)
d.text((36, fy + 28), "One image, one day — the world’s news of 23 November 2026.", font=F_FOOT, fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png")
