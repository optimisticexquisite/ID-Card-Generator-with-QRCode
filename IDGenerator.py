from PIL import Image, ImageDraw, ImageFont

#image = Image.new('RGB', (2480, 3508), (255, 255, 255))
image1=Image.open('quadsparksadmit.png')
image = Image.new("RGB", image1.size, (255, 255, 255))
image.paste(image1, mask=image1.split()[3])
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import qrcode
import pymongo
client=pymongo.MongoClient("mongodb+srv://pravega_developer:123qwerty@pravega-qebux.mongodb.net/test?retryWrites=true&w=majority")
quadsparks=client["quadsparks"]
data=quadsparks["data"]
os.system("ID CARD Generator")

d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print('------------------------------------------------------------------------------------------------')
print(reg_format_date)
print('------------------------------------------------------------------------------------------------')

# starting position of the message
print('\n\nAll Fields are Mandatory')
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
# (x, y) = (50, 50)
# company = 'Meowpany'
# color = 'rgb(0, 0, 0)'
# font = ImageFont.truetype('arial.ttf', size=80)
# draw.text((x, y), company, fill=color, font=font)

# adding an unique id number. You can manually take it from user





for user in data.find({'prelims2':'REGISTERED'}):
    image1=Image.open('quadsparksadmit.png')
    image = Image.new("RGB", image1.size, (255, 255, 255))
    image.paste(image1, mask=image1.split()[3])
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=45)
    (x, y) = (838, 482)
    idno = user['prelims2teamid']
    message = str(idno)
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (800, 930)
    name = user['teamname']
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), name, fill=color, font=font)

    (x, y) = (1193, 1167)
    participant1 = user['participant1']
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), participant1, fill=color, font=font)
    
    (x, y) = (1193, 1350)
    participant2 = user['participant2']
    if participant2 == "":
        participant2="N/A"
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), participant2, fill=color, font=font)

    (x, y) = (800, 1568)
    school = user['school']
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), school, fill=color, font=font)


    (x, y) = (800, 1766)
    schooladdress = user['schooladdress']
    color = 'rgb(0, 0, 0)'  # black color
    font = ImageFont.truetype('arial.ttf', size=45)
    draw.text((x, y), schooladdress, fill=color, font=font)


    # save the edited image
    image.save(str(idno) + '.png')

    img = qrcode.make(user["finalhash"])  # this info. is added in QR code, also add other things
    img.save(str(idno) + '.bmp')

    til = Image.open(idno + '.png')
    im = Image.open(str(idno) + '.bmp')  
    im.resize((390,390))
    til.paste(im, (1900, 185))
    #til.save(f"admitcard/{name}.pdf")

    #til2=Image.open(name+'.png')
    # im2=Image.open('quad2.png')
    # im2=im2.resize((1400,2100))
    # til2.paste(im2,(500,650),mask=im2)
    til.save(f"admitcard/{idno}.pdf")
    print(('\n\n\nYour ID Card Successfully created in a PNG file ' + idno + '.png'))

    # End
