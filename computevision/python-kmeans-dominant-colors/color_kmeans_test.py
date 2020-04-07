# USAGE
# python color_kmeans.py --image images/jp.png --clusters 3

# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import time
import numpy as np

# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to the image")
# ap.add_argument("-c", "--clusters", required = True, type = int,
# 	help = "# of clusters")
# args = vars(ap.parse_args())
images=[
    './snapshot/1.jpg',
    './snapshot/2.jpg',
'./snapshot/3.bmp',
'./snapshot/4.jpg',
'./snapshot/5.jpg',
'./snapshot/6.jpg',
'./snapshot/7.jpg',
]

def is_light_color(color):
    r,g,b = list(color)
    darkness = 1- (0.299*r + 0.587*g + 0.114*b)/255.0
    if darkness < 0.5:
        return True
    else:
        return False

def mend_color(color_lst):
    new_color_lst=[]
    for color in color_lst:
        # r,g,b = color
        color_cvt = np.array(color,dtype=np.uint8).reshape((1,1,3))
        print('color', color_cvt[0][0])
        new_color = cv2.cvtColor(color_cvt,cv2.COLOR_RGB2HLS)
        print('new_color', new_color.shape)
        new_color=new_color[0][0]
        print('new_color',new_color)

        if is_light_color(color):
            print('light')
            new_color[1]-=30
            new_color[2]-=80
            # new_color[1] = 30
            # new_color[2] = 80
        else:
            print('dark')
            new_color[1] += 40
            new_color[2] += 65
            # new_color[1] = 40
            # new_color[2] = 65

        print('new_color mend', new_color)

        new_color = new_color.reshape((1,1,3))

        new_rgb_color = cv2.cvtColor(new_color , cv2.COLOR_HLS2RGB)
        new_rgb_color=new_rgb_color[0][0]
        new_color_lst.append(new_rgb_color)
    return new_color_lst

for i in images:
    args={}
    args['image'] = i#'./images/batman.png'
    args['clusters'] = 2

    # load the image and convert it from BGR to RGB so that
    # we can dispaly it with matplotlib
    image = cv2.imread(args["image"])
    print(image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # show our image
    plt.figure()
    plt.axis("off")
    plt.imshow(image)

    image = cv2.resize(image,(100,100))

    begin = time.time()

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster the pixel intensities
    clt = KMeans(n_clusters = args["clusters"])
    clt.fit(image)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)
    print(hist)
    print(clt.cluster_centers_)
    new_color_lst = clt.cluster_centers_
    # new_color_lst = mend_color(clt.cluster_centers_)
    # print(new_color_lst)

    bar = utils.plot_colors(hist, new_color_lst)

    print('time: %s', time.time()-begin)

    # show our color bart
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()