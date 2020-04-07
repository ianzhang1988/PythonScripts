# USAGE
# python color_kmeans.py --image images/jp.png --clusters 3

# import the necessary packages
from sklearn.cluster import KMeans
#import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import time
import numpy as np
import traceback
import os

def get_dominate_color(image_path, n_clusters):
    # load the image and convert it from BGR to RGB so that
    # we can dispaly it with matplotlib
    fix_pic_flag = False
    try:
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    except Exception as e:
        print(traceback.format_exc())
        fix_pic_flag = True

    if fix_pic_flag:
        try:
            print('try fix pic')
            fix_file_name = image_path+'.fix.jpg'
            fix_cmd = 'ffmpeg -y -i {input} -pix_fmt yuvj444p -q 1 {output}'.format(input=image_path, output=fix_file_name)
            print('fix cmd',fix_cmd)
            os.system(fix_cmd)
            image = cv2.imread(fix_file_name)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(traceback.format_exc())
            raise Exception('cont fix pic')

    # resize, reducing need for cpu
    image = cv2.resize(image,(100,100))

    # reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    # cluster the pixel intensities
    clt = KMeans(n_clusters = n_clusters)
    clt.fit(image)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = utils.centroid_histogram(clt)

    return hist, clt.cluster_centers_

def pad_hex(hex_str):
    if len(hex_str)<2:
        hex_str = '0'+ hex_str
    return hex_str

def rgb2hex(rgb):
    r,g,b=map(int,rgb)
    hex_r = pad_hex(hex(r)[2:])
    hex_g = pad_hex(hex(g)[2:])
    hex_b = pad_hex(hex(b)[2:])
    return ''.join([hex_r,hex_g,hex_b])


if __name__ == '__main__':
    try:
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--image", required=True, help="Path to the image")
        ap.add_argument("-c", "--clusters", required=False, type=int, default=2,
                        help="# of clusters")
        ap.add_argument("-b", "--batch", required=False, help="Path to the image")
        args = vars(ap.parse_args())

        begin = time.time()
        hist, colors = get_dominate_color(args["image"], args["clusters"] )

        # print to std output
        # print('weight:')
        # for h in hist:
        #     print(h)
        # print('color:')
        # for c in colors:
        #     print(' '.join(map(str, c)))
        # print('elapse', time.time() -begin)

        hist = list(hist)
        color_idx = hist.index(max(hist))
        print( rgb2hex(colors[color_idx] ))

    except Exception as e:
        print(traceback.format_exc())
