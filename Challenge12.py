from PIL import Image

im = Image.open('cave.jpg')
(w, h) = im.size

even = Image.new('RGB', (w , h))
odd = Image.new('RGB', (w, h))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i,j))
        if (i+j)%2 == 1:
            odd.putpixel((i, j), p)
        else:
            even.putpixel((i , j), p)
even.save('even.jpg')
odd.save('odd.jpg')
