import imageio.v3 as iio

pic_names = ['pic1.jpg', 'pic2.jpg', 'pic3.jpg', 'pic4.jpg', 'pic5.jpg']
images = [ ]

for pic in pic_names:
    images.append(iio.imread(pic))

iio.imwrite('my_walk.gif', images, duration = 450, loop = 0)
