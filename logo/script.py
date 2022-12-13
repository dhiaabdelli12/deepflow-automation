import os
from PIL import Image
min_size = 300
logo_file = 'logo.png'
logo = Image.open(logo_file)
logo_width, logo_height = logo.size

LOGO_POS_X = 100
LOGO_POS_Y = 0
LOGO_WIDTH  = 200


wpercent = (LOGO_WIDTH/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((LOGO_WIDTH,hsize),Image.Resampling.LANCZOS)


def main():
    os.makedirs('withlogo', exist_ok=True)
    for filename in os.listdir('./images/'):
        if not (filename.endswith('.png'.upper()) or filename.endswith('.jpg'.upper())):
            continue
        print(filename)
        im = Image.open(os.path.join('images',filename))
        width, height = im.size

        im.paste(logo,(LOGO_POS_X,LOGO_POS_Y),logo)
        im.save(os.path.join('withlogo',filename))



if __name__=='__main__':
    main()