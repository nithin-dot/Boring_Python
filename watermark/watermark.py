import cv2
from nowatermark import WatermarkRemover
path = 'C:/Users/nithin/Desktop/watermark/'
watermark_template_filename = path + 'hello.jpg'
remover = WatermarkRemover()
remover.load_watermark_template(r"C:/Users/nithin/Desktop/watermark/sample.png")

remover.remove_watermark(path + 'hello.jpg', path + 'anjuke3-result.jpg')