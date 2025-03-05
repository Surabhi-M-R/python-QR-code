import qrcode as qr
img=qr.make("https://www.youtube.com/results?search_query=carryminati")
img.save("youtube.png")
