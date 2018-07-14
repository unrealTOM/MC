import os
from PIL import Image

files = [
  'ImpSampling1.png',
  'ImpSampling2.png']
#  'normal1.png',
#  'normal2.png']
#  'uniform1.png',
#  'uniform2.png']

halfWidth = 480
#halfWidth = 400
#halfWidth = 300
height = 350
#height = 240
#height = 220
result = Image.new("RGBA", (halfWidth * 2, height))

for index, file in enumerate(files):
  path = os.path.expanduser(file)
  img = Image.open(path)
  x = index % 2 * halfWidth 
  y = index // 2 * height
  w, h = img.size
  print(x,y,w,h)
  result.paste(img, (x, height - h, x + w, height))

result.save(os.path.expanduser('ImpSampling.png'))
#result.save(os.path.expanduser('normal.png'))
#result.save(os.path.expanduser('uniform.png'))
