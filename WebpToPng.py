import glob
import os
import threading

from PIL import Image


def create_image(infile, index):
  os.path.splitext(infile)
  im = Image.open(infile)
  im.save("img_png/png_" + str(index) + ".png", "PNG")


def start():
  index = 0
  for infile in glob.glob("img/*.webp"):
    t = threading.Thread(target=create_image, args=(infile, index,))
    t.start()
    t.join()
    index += 1


if __name__ == "__main__":
  start()