#!/usr/bin/python
import Image
import argparse

parser = argparse.ArgumentParser(description='Debes ingresar las opciones requeridas')
parser.add_argument('-i','--input', help='Imagen a seleccionar',required=True)
parser.add_argument('-o','--output',help='Archivo HTML a generar', required=True)
args = parser.parse_args()

print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )



def rgbtohex(rgb_tuple):
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor

img = Image.open(args.input)
f = open(args.output,"w")
pixel = img.load()

width = img.size[0]
height = img.size[1]

f.write('<style>\n')
f.write('*{margin:0px;padding:0px;}\n')
f.write('#c{float:left;width:')
f.write('%s' % width)
f.write('; height:')
f.write('%s' % height)
f.write(';}\n')
f.write('#c div{float:left;width:1px;height:1px;}\n')
k=0
for i in range(height):
    for j in range(width):
        f.write('#c%s{' % k)
        f.write('background:%s;}' % rgbtohex(pixel[j,i]))
        k = k + 1
f.write('\n</style>\n<div id="c">')

k=0
for i in range(width):
    for j in range(height):
        f.write('<div id="c%s"></div>' % k)
        k = k + 1
f.write('</div>')