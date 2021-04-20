# -*- coding: utf-8 -*-
"""preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14KVM0Z6HOxT8PZH1jLYuC17TZgkSHMQF
"""

# import essential libaries
from PIL import Image, ImageDraw, ImageFont
import os 
import json
import fitz

def pyMuPDF_fitz(pdfPath, imagePath,count):
    # print("imagePath=" + pdfPath)
    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        zoom_x = 1
        zoom_y = 1
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        try:
            pix = page.getPixmap(matrix=mat, alpha=False)
        except:
            print("imagePath=" + pdfPath)
            continue
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)

        pix.writePNG(imagePath + '/' + 'images_%s.png' % count)
        count +=1
    return count

def coco_test_json_generator(img_path,output_path,test_json_path):
  with open(test_json_path) as f:
    test_json = json_load(f)
  img_name_list = os.listdir(img_path)
  new_json = {}
  new_json['images'] = []
  for i,name in enumerate(img_name_list):
    img_dict = {}
    path = img_path + '/' + name
    image = Image.open(path)
    img_dict['file_name'] = name
    img_dict['width'] = image.size[0]
    img_dict['height'] = image.size[1]
    img_dict['id'] = i
    new_json['images'].append(img_dict)
  new_json['annotations'] = []
  new_json['categories'] = test_json['categories']
  new_json['type'] = test_json['type']
  file_name = 'test.json' 
  with open(output_path+'/'+file_name,'w') as file_object:
    json.dump(new_json,file_object)

