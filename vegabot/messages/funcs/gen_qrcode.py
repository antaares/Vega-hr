import qrcode

async def generat_qrcod(name,author,mavzu,price,time,user_id=None):
        input_data = f"Ism, familiyasi:: {name}\n\n" \
                     f"Trening nomi:: {mavzu}\n\n" \
                     f"Trening spikeri:: {author}\n\n" \
                     f"To'lagan summasi:: {price}\n\n" \
                     f"Trening vaqti:: {time}"

        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f'data/picture/{user_id}.png')