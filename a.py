from PIL import Image
import sys

a = Image.open(sys.argv[1])

a.save("a.webp")