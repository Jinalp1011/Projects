import qrcode as qr
img = qr.make("https://www.youtube.com/playlist?list=PL08903FB7ACA1C2FB")
img.save("SQL-Server_youtube.png")