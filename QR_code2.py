import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1 , 
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10 , border = 4,)

qr.add_data("https://www.youtube.com/playlist?list=PL08903FB7ACA1C2FB")
qr.make(fit = True)
img = qr.make_image(fill_color = "blue" , back_color="black")
img.save("SQL-Server_youtube2.png")