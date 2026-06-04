#!/usr/bin/env python3
import qrcode

url = "https://sihuju992-lab.github.io/-1.0/"
img = qrcode.make(url)
img.save("qr_code.png")