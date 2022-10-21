from PIL import Image, ImageFont, ImageDraw



import csv
joke = ""
with open('Datasets/jokes.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:

        my_image = Image.open("Background images/snow.jpg")

        w, h = my_image.size
        
        ids = row[0]
        
        joke = str(row).replace('\\n','\n')
        #joke = "1234567890 \n 1234567890"
        
        print(joke)

        title_font = ImageFont.truetype('Roboto-Black.ttf', 30)
        
        image_editable = ImageDraw.Draw(my_image)

        wf, hf = image_editable.textsize(joke, title_font)

        print(w,"x",h," : ",wf,"x",hf)

        title_font = ImageFont.truetype('Roboto-Black.ttf', 30)

        image_editable.text(((w-wf)/2 , (h-hf)/2), joke, (242, 242, 242), font=title_font)

        my_image.save("Images/"+str(ids)+".jpg")
        
