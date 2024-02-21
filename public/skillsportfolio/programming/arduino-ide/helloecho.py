#!/usr/bin/env python
#
# hello.t1614.echo
#    tiny1614 echo hello-world
#
# usage:
#    hello.t1614.echo | frep.py [dpi [filename]]
#
# Neil Gershenfeld 12/22/19
#
# This work may be reproduced, modified, distributed,
# performed, and displayed for any purpose, but must
# acknowledge this project. Copyright is retained and
# must be preserved. The work is provided as is; no
# warranty is provided, and users accept all liability.
#

#
# uncomment for desired output:
#

output = "top, labels, and exterior"
#output = "top, labels, holes, and exterior"
#output = "top, bottom, labels, and exterior"
#output = "top, bottom, labels, holes, and exterior"
#output = "top traces"
#output = "top traces and exterior"
#output = "top traces, holes, and exterior"
#output = "bottom traces reversed"
#output = "bottom traces reversed and exterior"
#output = "holes"
#output = "interior"
#output = "holes and interior"
#output = "exterior"
#output = "solder mask"

#
# import
#

import math,json,sys

#
# define shapes and transformations
#

# color(color,part)
# circle(x,y,r)
# cylinder(x,y,z0,z1,r)
# cone(x,y,z0,z1,r)
# sphere(x,y,z,r)
# torus(x,y,z,r0,r1)
# rectangle(x0,x1,y0,y1)
# cube(x0,x1,y0,y1,z0,z1)
# line(x0,y0,x1,y1,z,width)
# right_triangle(x,y,h)
# triangle(x0,y0,x1,y1,x2,y2) (points in clockwise order)
# pyramid(x0,x1,y0,y1,z0,z1)
# function(Z_of_XY)
# functions(upper_Z_of_XY,lower_Z_of_XY)
# add(part1,part2)
# subtract(part1,part2)
# intersect(part1,part2)
# move(part,dx,dy)
# translate(part,dx,dy,dz)
# rotate(part, angle)
# rotate_x(part,angle)
# rotate_y(part,angle)
# rotate_z(part,angle)
# rotate_90(part)
# rotate_180(part)
# rotate_270(part)
# reflect_x(part,x0)
# reflect_y(part,y0)
# reflect_z(part,z0)
# reflect_xy(part)
# reflect_xz(part)
# reflect_yz(part)
# scale_x(part,x0,sx)
# scale_y(part,y0,sy)
# scale_z(part,z0,sz)
# scale_xy(part,x0,y0,sxy)
# scale_xyz(part,x0,y0,z0,sxyz)
# coscale_x_y(part,x0,y0,y1,angle0,angle1,amplitude,offset)
# coscale_x_z(part,x0,z0 z1,angle0,angle1,amplitude,offset)
# coscale_xy_z(part,x0,y0,z0,z1,angle0,angle1,amplitude,offset)
# taper_x_y(part,x0,y0,y1,s0,s1)
# taper_x_z(part,x0,z0,z1,s0,s1)
# taper_xy_z(part,x0,y0,z0,z1,s0,s1)
# shear_x_y(part,y0,y1,dx0,dx1)
# shear_x_z(part,z0,z1,dx0,dx1)

true = "1"
false = "0"

def color(color,part):
   part = '('+str(color)+'*(('+part+')!=0))'
   return part

Red = (225 << 0)
Green = (225 << 8)
Blue = (225 << 16)
Gray = (128 << 16) + (128 << 8) + (128 << 0)
White = (255 << 16) + (255 << 8) + (255 << 0)
Teal = (255 << 16) + (255 << 8)
Pink = (255 << 16) + (255 << 0)
Yellow = (255 << 8) + (255 << 0)
Brown = (45 << 16) + (82 << 8) + (145 << 0)
Navy = (128 << 16) + (0 << 8) + (0 << 0)
Tan = (60 << 16) + (90 << 8) + (125 << 0)

def circle(x0,y0,r):
   part = "(((X-(x0))*(X-(x0)) + (Y-(y0))*(Y-(y0))) <= (r*r))"
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('r',str(r))
   return part

def cylinder(x0,y0,z0,z1,r):
   part = "(((X-(x0))*(X-(x0)) + (Y-(y0))*(Y-(y0)) <= (r*r)) & (Z >= (z0)) & (Z <= (z1)))"
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('r',str(r))
   return part

def cone(x0,y0,z0,z1,r0):
   part = cylinder(x0, y0, z0, z1, r0)
   part = taper_xy_z(part, x0, y0, z0, z1, 1.0, 0.0)
   return part

def sphere(x0,y0,z0,r):
   part = "(((X-(x0))*(X-(x0)) + (Y-(y0))*(Y-(y0)) + (Z-(z0))*(Z-(z0))) <= (r*r))"
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('z0',str(z0))
   part = part.replace('r',str(r))
   return part

def torus(x0,y0,z0,r0,r1):
   part = "(((r0 - sqrt((X-(x0))*(X-(x0)) + (Y-(y0))*(Y-(y0))))*(r0 - sqrt((X-(x0))*(X-(x0)) + (Y-(y0))*(Y-(y0))) + (Z-(z0))*(Z-(z0))) <= (r1*r1))"
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('z0',str(z0))
   part = part.replace('r0',str(r0))
   part = part.replace('r1',str(r1))
   return part

def rectangle(x0,x1,y0,y1):
   part = "((X >= (x0)) & (X <= (x1)) & (Y >= (y0)) & (Y <= (y1)))"
   part = part.replace('x0',str(x0))
   part = part.replace('x1',str(x1))
   part = part.replace('y0',str(y0))
   part = part.replace('y1',str(y1))
   return part

def cube(x0,x1,y0,y1,z0,z1):
   part = "((X >= (x0)) & (X <= (x1)) & (Y >= (y0)) & (Y <= (y1)) & (Z >= (z0)) & (Z <= (z1)))"
   part = part.replace('x0',str(x0))
   part = part.replace('x1',str(x1))
   part = part.replace('y0',str(y0))
   part = part.replace('y1',str(y1))
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   return part

def line(x0,y0,x1,y1,z,width):
   dx = x1-x0
   dy = y1-y0
   l = math.sqrt(dx*dx+dy*dy)
   nx = dx/l
   ny = dy/l
   rx = -ny
   ry = nx
   part = "((((X-(x0))*(nx)+(Y-(y0))*(ny)) >= 0) & (((X-(x0))*(nx)+(Y-(y0))*(ny)) <= l) & (((X-(x0))*(rx)+(Y-(y0))*(ry)) >= (-width/2)) & (((X-(x0))*(rx)+(Y-(y0))*(ry)) <= (width/2)) & (Z == z))"
   part = part.replace('x0',str(x0))
   part = part.replace('x1',str(x1))
   part = part.replace('y0',str(y0))
   part = part.replace('y1',str(y1))
   part = part.replace('nx',str(nx))
   part = part.replace('ny',str(ny))
   part = part.replace('rx',str(rx))
   part = part.replace('ry',str(ry))
   part = part.replace('l',str(l))
   part = part.replace('z',str(z))
   part = part.replace('width',str(width))
   return part

def right_triangle(x0,y0,l):
   part = "((X > x0) & (X < x0 + l - (Y-y0)) & (Y > y0))"
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('l',str(l))
   return part

def triangle(x0,y0,x1,y1,x2,y2): # points in clockwise order
   part = "(((((y1)-(y0))*(X-(x0))-((x1)-(x0))*(Y-(y0))) >= 0) & ((((y2)-(y1))*(X-(x1))-((x2)-(x1))*(Y-(y1))) >= 0) & ((((y0)-(y2))*(X-(x2))-((x0)-(x2))*(Y-(y2))) >= 0))"
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('x1',str(x1))
   part = part.replace('y1',str(y1))
   part = part.replace('x2',str(x2))
   part = part.replace('y2',str(y2))
   return part

def pyramid(x0,x1,y0,y1,z0,z1):
   part = cube(x0, x1, y0, y1, z0, z1)
   part = taper_xy_z(part, (x0+x1)/2., (y0+y1)/2., z0, z1, 1.0, 0.0)
   return part

def function(Z_of_XY):
   part = '(Z <= '+Z_of_XY+')'
   return part

def functions(upper_Z_of_XY,lower_Z_of_XY):
   part = '(Z <= '+upper_Z_of_XY+') & (Z >= '+lower_Z_of_XY+')'
   return part

def add(part1,part2):
   part = "part1 | part2"
   part = part.replace('part1',part1)
   part = part.replace('part2',part2)
   return part

def subtract(part1,part2):
   part = "(part1) & ~(part2)"
   part = part.replace('part1',part1)
   part = part.replace('part2',part2)
   return part

def intersect(part1,part2):
   part = "(part1) & (part2)"
   part = part.replace('part1',part1)
   part = part.replace('part2',part2)
   return part

def move(part,dx,dy):
   part = part.replace('X','(X-('+str(dx)+'))')
   part = part.replace('Y','(Y-('+str(dy)+'))')
   return part   

def translate(part,dx,dy,dz):
   part = part.replace('X','(X-('+str(dx)+'))')
   part = part.replace('Y','(Y-('+str(dy)+'))')
   part = part.replace('Z','(Z-('+str(dz)+'))')
   return part   

def rotate(part,angle):
   angle = angle*math.pi/180
   part = part.replace('X','(math.cos(angle)*X+math.sin(angle)*y)')
   part = part.replace('Y','(-math.sin(angle)*X+math.cos(angle)*y)')
   part = part.replace('y','Y')
   part = part.replace('angle',str(angle))
   return part

def rotate_x(part,angle):
   angle = angle*math.pi/180
   part = part.replace('Y','(math.cos(angle)*Y+math.sin(angle)*z)')
   part = part.replace('Z','(-math.sin(angle)*Y+math.cos(angle)*z)')
   part = part.replace('z','Z')
   part = part.replace('angle',str(angle))
   return part

def rotate_y(part,angle):
   angle = angle*math.pi/180
   part = part.replace('X','(math.cos(angle)*X+math.sin(angle)*z)')
   part = part.replace('Z','(-math.sin(angle)*X+math.cos(angle)*z)')
   part = part.replace('z','Z')
   part = part.replace('angle',str(angle))
   return part

def rotate_z(part,angle):
   angle = angle*math.pi/180
   part = part.replace('X','(math.cos(angle)*X+math.sin(angle)*y)')
   part = part.replace('Y','(-math.sin(angle)*X+math.cos(angle)*y)')
   part = part.replace('y','Y')
   part = part.replace('angle',str(angle))
   return part

def rotate_90(part):
   part = reflect_y(part,0)
   part = reflect_xy(part)
   return part

def rotate_180(part):
   part = rotate_90(part)
   part = rotate_90(part)
   return part

def rotate_270(part):
   part = rotate_90(part)
   part = rotate_90(part)
   part = rotate_90(part)
   return part

def reflect_x(part,x0):
   part = part.replace('X','(x0-X)')
   part = part.replace('x0',str(x0))
   return part

def reflect_y(part,y0):
   part = part.replace('Y','(y0-Y)')
   part = part.replace('y0',str(y0))
   return part

def reflect_z(part,z0):
   part = part.replace('Z','(z0-Z)')
   part = part.replace('z0',str(z0))
   return part

def reflect_xy(part):
   part = part.replace('X','temp')
   part = part.replace('Y','X')
   part = part.replace('temp','Y')
   return part

def reflect_xz(part):
   part = part.replace('X','temp')
   part = part.replace('Z','X')
   part = part.replace('temp','Z')
   return part

def reflect_yz(part):
   part = part.replace('Y','temp')
   part = part.replace('Z','Y')
   part = part.replace('temp','Z')
   return part

def scale_x(part,x0,sx):
   part = part.replace('X','((x0) + (X-(x0))/(sx))')
   part = part.replace('x0',str(x0))
   part = part.replace('sx',str(sx))
   return part

def scale_y(part,y0,sy):
   part = part.replace('Y','((y0) + (Y-(y0))/(sy))')
   part = part.replace('y0',str(y0))
   part = part.replace('sy',str(sy))
   return part

def scale_z(part,z0,sz):
   part = part.replace('Z','((z0) + (Z-(z0))/(sz))')
   part = part.replace('z0',str(z0))
   part = part.replace('sz',str(sz))
   return part

def scale_xy(part,x0,y0,sxy):
   part = part.replace('X','((x0) + (X-(x0))/(sxy))')
   part = part.replace('Y','((y0) + (Y-(y0))/(sxy))')
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('sxy',str(sxy))
   return part

def scale_xyz(part,x0,y0,z0,sxyz):
   part = part.replace('X','((x0) + (X-(x0))/(sxyz))')
   part = part.replace('Y','((y0) + (Y-(y0))/(sxyz))')
   part = part.replace('Z','((z0) + (Z-(z0))/(sxyz))')
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('z0',str(z0))
   part = part.replace('sxyz',str(sxyz))
   return part

def coscale_x_y(part,x0,y0,y1,angle0,angle1,amplitude,offset):
   phase0 = math.pi*angle0/180.
   phase1 = math.pi*angle1/180.
   part = part.replace('X','((x0) + (X-(x0))/((offset) + (amplitude)*math.cos((phase0) + ((phase1)-(phase0))*(Y-(y0))/((y1)-(y0)))))')
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('y1',str(y1))
   part = part.replace('phase0',str(phase0))
   part = part.replace('phase1',str(phase1))
   part = part.replace('amplitude',str(amplitude))
   part = part.replace('offset',str(offset))
   return part

def coscale_x_z(part,x0,z0,z1,angle0,angle1,amplitude,offset):
   phase0 = math.pi*angle0/180.
   phase1 = math.pi*angle1/180.
   part = part.replace('X','((x0) + (X-(x0))/((offset) + (amplitude)*math.cos((phase0) + ((phase1)-(phase0))*(Z-(z0))/((z1)-(z0)))))')
   part = part.replace('x0',str(x0))
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('phase0',str(phase0))
   part = part.replace('phase1',str(phase1))
   part = part.replace('amplitude',str(amplitude))
   part = part.replace('offset',str(offset))
   return part

def coscale_xy_z(part,x0,y0,z0,z1,angle0,angle1,amplitude,offset):
   phase0 = math.pi*angle0/180.
   phase1 = math.pi*angle1/180.
   part = part.replace('X','((x0) + (X-(x0))/((offset) + (amplitude)*math.cos((phase0) + ((phase1)-(phase0))*(Z-(z0))/((z1)-(z0)))))')
   part = part.replace('Y','((y0) + (Y-(y0))/((offset) + (amplitude)*math.cos((phase0) + ((phase1)-(phase0))*(Z-(z0))/((z1)-(z0)))))')
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('phase0',str(phase0))
   part = part.replace('phase1',str(phase1))
   part = part.replace('amplitude',str(amplitude))
   part = part.replace('offset',str(offset))
   return part

def taper_x_y(part,x0,y0,y1,s0,s1):
   part = part.replace('X','((x0) + (X-(x0))*((y1)-(y0))/((s1)*(Y-(y0)) + (s0)*((y1)-Y)))')
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('y1',str(y1))
   part = part.replace('s0',str(s0))
   part = part.replace('s1',str(s1))
   return part

def taper_x_z(part,x0,z0,z1,s0,s1):
   part = part.replace('X','((x0) + (X-(x0))*((z1)-(z0))/((s1)*(Z-(z0)) + (s0)*((z1)-Z)))')
   part = part.replace('x0',str(x0))
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('s0',str(s0))
   part = part.replace('s1',str(s1))
   return part

def taper_xy_z(part,x0,y0,z0,z1,s0,s1):
   part = part.replace('X','((x0) + (X-(x0))*((z1)-(z0))/((s1)*(Z-(z0)) + (s0)*((z1)-Z)))')
   part = part.replace('Y','((y0) + (Y-(y0))*((z1)-(z0))/((s1)*(Z-(z0)) + (s0)*((z1)-Z)))')
   part = part.replace('x0',str(x0))
   part = part.replace('y0',str(y0))
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('s0',str(s0))
   part = part.replace('s1',str(s1))
   return part

def shear_x_y(part,y0,y1,dx0,dx1):
   part = part.replace('X','(X - (dx0) - ((dx1)-(dx0))*(Y-(y0))/((y1)-(y0)))')
   part = part.replace('y0',str(y0))
   part = part.replace('y1',str(y1))
   part = part.replace('dx0',str(dx0))
   part = part.replace('dx1',str(dx1))
   return part

def shear_x_z(part,z0,z1,dx0,dx1):
   part = part.replace('X','(X - (dx0) - ((dx1)-(dx0))*(Z-(z0))/((z1)-(z0)))')
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('dx0',str(dx0))
   part = part.replace('dx1',str(dx1))
   return part

def coshear_x_z(part,z0,z1,angle0,angle1,amplitude,offset):
   phase0 = math.pi*angle0/180.
   phase1 = math.pi*angle1/180.
   part = part.replace('X','(X - (offset) - (amplitude)*math.cos((phase0) + ((phase1)-(phase0))*(Z-(z0))/((z1)-(z0))))')
   part = part.replace('z0',str(z0))
   part = part.replace('z1',str(z1))
   part = part.replace('phase0',str(phase0))
   part = part.replace('phase1',str(phase1))
   part = part.replace('amplitude',str(amplitude))
   part = part.replace('offset',str(offset))
   return part

#
# text classes and definitions
#

class text:
   #
   # text class
   #
   def __init__(self,text,x,y,z,line='',height='',width='',space='',align='CC',color=White,angle=0):
      #
      # parameters
      #
      if (line == ''):
         line = 1
      if (height == ''):
         height = 6*line
      if (width == ''):
         width = 4*line
      if (space == ''):
         space = line/2.0
      self.width = 0
      self.height = 0
      self.text = text
      #
      # construct shape dictionary
      #
      shapes = {}
      shape = triangle(0,0,width/2.0,height,width,0)
      cutout = triangle(0,-2.5*line,width/2.0,height-2.5*line,width,-2.5*line)
      cutout = subtract(cutout,rectangle(0,width,height/4-line/2,height/4+line/2))
      shape = subtract(shape,cutout)
      shapes['A'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/4))
      shape = add(shape,rectangle(width-line,width,0,height/3))
      shapes['a'] = shape
      shape = rectangle(0,width-height/4,0,height)
      shape = add(shape,circle(width-height/4,height/4,height/4))
      shape = add(shape,circle(width-height/4,3*height/4,height/4))
      w = height/2-1.5*line
      shape = subtract(shape,rectangle(line,line+w/1.5,height/2+line/2,height-line))
      shape = subtract(shape,circle(line+w/1.5,height/2+line/2+w/2,w/2))
      shape = subtract(shape,rectangle(line,line+w/1.5,line,height/2-line/2))
      shape = subtract(shape,circle(line+w/1.5,height/2-line/2-w/2,w/2))
      shapes['B'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/4))
      shape = add(shape,rectangle(0,line,0,height))
      shapes['b'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = add(shape,circle(width/2,height-width/2,width/2))
      shape = add(shape,rectangle(0,width,line+w/2,height-line-w/2))
      w = width-2*line
      shape = subtract(shape,circle(width/2,line+w/2,w/2))
      shape = subtract(shape,circle(width/2,height-line-w/2,w/2))
      shape = subtract(shape,rectangle(line,width,line+w/2,height-line-w/2))
      shapes['C'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/4))
      shape = subtract(shape,rectangle(width/2,width,width/2-line/1.5,width/2+line/1.5))
      shapes['c'] = shape
      shape = circle(line,width-line,width-line)
      shape = subtract(shape,circle(line,width-line,width-2*line))
      shape = subtract(shape,rectangle(-width,line,0,height))
      shape = scale_y(shape,0,height/(2*(width-line)))
      shape = add(shape,rectangle(0,line,0,height))
      shapes['D'] = shape
      shape = rectangle(width-line,width,0,height)
      shape = add(shape,circle(width/2,width/2,width/2))
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shapes['d'] = shape
      shape = rectangle(0,line,0,height)
      shape = add(shape,rectangle(0,width,height-line,height))
      shape = add(shape,rectangle(0,2*width/3,height/2-line/2,height/2+line/2))
      shape = add(shape,rectangle(0,width,0,line))      
      shapes['E'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,triangle(width,0,width/2,width/2-line/2,width,width/2-line/2))
      shape = add(shape,rectangle(0,width,width/2-line/2,width/2+line/2))
      shapes['e'] = shape
      shape = rectangle(0,line,0,height)
      shape = add(shape,rectangle(0,width,height-line,height))
      shape = add(shape,rectangle(0,2*width/3,height/2-line/2,height/2+line/2))
      shapes['F'] = shape
      shape = circle(width-line/2,height-width/2,width/2)
      shape = subtract(shape,circle(width-line/2,height-width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width-line/2,0,height-width/2))
      shape = subtract(shape,rectangle(width-line/2,2*width,0,height))
      shape = add(shape,rectangle(width/2-line/2,width/2+line/2,0,height-width/2))
      shape = add(shape,rectangle(width/5,4*width/5,height/2-line/2,height/2+line/2))
      shapes['f'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = add(shape,circle(width/2,height-width/2,width/2))
      shape = add(shape,rectangle(0,width,line+w/2,height-line-w/2))
      w = width-2*line
      shape = subtract(shape,circle(width/2,line+w/2,w/2))
      shape = subtract(shape,circle(width/2,height-line-w/2,w/2))
      shape = subtract(shape,rectangle(line,width,line+w/2,height-line-w/2))
      shape = add(shape,rectangle(width/2,width,line+w/2,2*line+w/2))
      shapes['G'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      w = height/3-width/2
      shape = add(shape,rectangle(width-line,width,w,width))
      shape = add(shape,subtract(subtract(circle(width/2,w,width/2),circle(width/2,w,width/2-line)),rectangle(0,width,w,height)))
      shapes['g'] = shape
      shape = rectangle(0,line,0,height)
      shape = add(shape,rectangle(width-line,width,0,height))
      shape = add(shape,rectangle(0,width,height/2-line/2,height/2+line/2))
      shapes['H'] = shape
      w = width/2
      shape = circle(width/2,w,width/2)
      shape = subtract(shape,circle(width/2,w,width/2-line))
      shape = subtract(shape,rectangle(0,width,0,w))
      shape = add(shape,rectangle(0,line,0,height))
      shape = add(shape,rectangle(width-line,width,0,w))
      shapes['h'] = shape
      shape = rectangle(width/2-line/2,width/2+line/2,0,height)
      shape = add(shape,rectangle(width/5,4*width/5,0,line))
      shape = add(shape,rectangle(width/5,4*width/5,height-line,height))
      shapes['I'] = shape
      shape = rectangle(width/2-line/2,width/2+line/2,0,height/2)
      shape = add(shape,circle(width/2,3*height/4,.6*line))
      shapes['i'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width,width/2,height))
      shape = add(shape,rectangle(width-line,width,width/2,height))
      shapes['J'] = shape
      w = height/3-width/2
      shape = rectangle(width/2-line/2,width/2+line/2,w,height/2)
      shape = add(shape,subtract(subtract(subtract(circle(width/4-line/2,w,width/2),circle(width/4-line/2,w,width/2-line)),rectangle(0,width,w,height)),rectangle(-width,width/4-line/2,-height/3,height)))
      shape = add(shape,circle(width/2,3*height/4,.6*line))
      shapes['j'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,triangle(line,height,width-1.1*line,height,line,height/2+.5*line))
      shape = subtract(shape,triangle(width,0,line+0.8*line,height/2,width,height))
      shape = subtract(shape,triangle(line,0,line,height/2-.5*line,width-1.1*line,0))
      shapes['K'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,rectangle(line,width,2*height/3,height))
      shape = subtract(shape,triangle(line,2*height/3,width-1.3*line,2*height/3,line,height/3+.5*line))
      shape = subtract(shape,triangle(width,0,line+0.8*line,height/3,width,2*height/3))
      shape = subtract(shape,triangle(line,0,line,height/3-0.5*line,width-1.3*line,0))
      shapes['k'] = shape
      shape = rectangle(0,line,0,height)
      shape = add(shape,rectangle(0,width,0,line))
      shapes['L'] = shape
      shape = rectangle(width/2-line/2,width/2+line/2,0,height)
      shapes['l'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,triangle(line,0,line,height-3*line,width/2-line/3,0))
      shape = subtract(shape,triangle(line,height,width-line,height,width/2,1.5*line))
      shape = subtract(shape,triangle(width/2+line/3,0,width-line,height-3*line,width-line,0))
      shapes['M'] = shape
      w = width/2
      l = 1.3*line
      shape = circle(width/2,w,width/2)
      shape = subtract(shape,circle(width/2,w,width/2-l))
      shape = subtract(shape,rectangle(0,width,0,w))
      shape = add(shape,rectangle(width-l,width,0,w))
      shape = add(shape,move(shape,width-l,0))
      shape = add(shape,rectangle(0,l,0,width))
      shape = scale_x(shape,0,width/(2*width-l))
      shapes['m'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,triangle(line,height+1.5*line,width-line,height+1.5*line,width-line,1.5*line))
      shape = subtract(shape,triangle(line,-1.5*line,line,height-1.5*line,width-line,-1.5*line))
      shapes['N'] = shape
      w = width/2
      shape = circle(width/2,w,width/2)
      shape = subtract(shape,circle(width/2,w,width/2-line))
      shape = subtract(shape,rectangle(0,width,0,w))
      shape = add(shape,rectangle(0,line,0,width))
      shape = add(shape,rectangle(width-line,width,0,w))
      shapes['n'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = add(shape,circle(width/2,height-width/2,width/2))
      shape = add(shape,rectangle(0,width,line+w/2,height-line-w/2))
      w = width-2*line
      shape = subtract(shape,circle(width/2,line+w/2,w/2))
      shape = subtract(shape,circle(width/2,height-line-w/2,w/2))
      shape = subtract(shape,rectangle(line,width-line,line+w/2,height-line-w/2))
      shapes['O'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shapes['o'] = shape
      shape = rectangle(0,line,0,height)
      w = 2*height/3
      shape = add(shape,circle(width-w/2,height-w/2,w/2))
      shape = add(shape,rectangle(0,width-w/2,height-w,height))
      shape = subtract(shape,circle(width-w/2,height-w/2,w/2-line))
      shape = subtract(shape,rectangle(line,width-w/2,height-w+line,height-line))
      shapes['P'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/4))
      shape = add(shape,rectangle(0,line,-height/3,width))
      shapes['p'] = shape
      shape = subtract(circle(width/2,width/2,width/2),circle(width/2,width/2,width/2-.9*line))
      shape = scale_y(shape,0,height/width)
      shape = add(shape,move(rotate(rectangle(-line/2,line/2,-width/4,width/4),30),3*width/4,width/4))
      shapes['Q'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = add(shape,rectangle(width-line,width,-height/3,width))
      shapes['q'] = shape
      shape = rectangle(0,line,0,height)
      w = 2*height/3
      shape = add(shape,circle(width-w/2,height-w/2,w/2))
      shape = add(shape,rectangle(0,width-w/2,height-w,height))
      shape = subtract(shape,circle(width-w/2,height-w/2,w/2-line))
      shape = subtract(shape,rectangle(line,width-w/2,height-w+line,height-line))
      leg = triangle(line,0,line,height,width,0)
      leg = subtract(leg,triangle(line,-2.0*line,line,height-2.0*line,width,-2.0*line))
      leg = subtract(leg,rectangle(0,width,height/3,height))
      shape = add(shape,leg)
      shapes['R'] = shape
      shape = circle(width,0,width)
      shape = subtract(shape,circle(width,0,width-line))
      shape = subtract(shape,rectangle(.8*width,2*width,-height,height))
      shape = subtract(shape,rectangle(0,2*width,-height,0))
      shape = add(shape,rectangle(0,line,0,width))
      shapes['r'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width/2,width/2,width))
      shape = add(shape,move(reflect_y(reflect_x(shape,width),width),0,width-line))
      shape = scale_y(shape,0,height/(2*width-line))
      shapes['S'] = shape
      w = width/3
      shape = circle(w,w,w)
      shape = subtract(shape,circle(w,w,w-.9*line))
      shape = subtract(shape,rectangle(0,w,w,2*w))
      shape = add(shape,move(reflect_y(reflect_x(shape,2*w),2*w),0,2*w-.9*line))
      shape = scale_y(shape,0,(2*height/3)/(4*w-.9*line))
      shape = move(shape,(width/2)-w,0)
      shapes['s'] = shape
      shape = rectangle(width/2-line/2,width/2+line/2,0,height)
      shape = add(shape,rectangle(0,width,height-line,height))
      shapes['T'] = shape
      shape = circle(0,3*width/8,3*width/8)
      shape = subtract(shape,circle(0,3*width/8,3*width/8-line))
      shape = subtract(shape,rectangle(-width,width,3*width/8,height))
      shape = subtract(shape,rectangle(0,width,-height,height))
      shape = move(shape,width/2-line/2+3*width/8,0)
      shape = add(shape,rectangle(width/2-line/2,width/2+line/2,width/4,3*height/4))
      shape = add(shape,rectangle(width/5,4*width/5,height/2-line/2,height/2+line/2))
      shapes['t'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width,width/2,height))
      shape = add(shape,rectangle(0,line,width/2,height))
      shape = add(shape,rectangle(width-line,width,width/2,height))
      shapes['U'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width,width/2,height))
      shape = add(shape,rectangle(0,line,width/2,2*height/3))
      shape = add(shape,rectangle(width-line,width,0,2*height/3))
      shapes['u'] = shape
      shape = triangle(0,height,width,height,width/2,0)
      shape = subtract(shape,triangle(0,height+3*line,width,height+3*line,width/2,3*line))
      shapes['V'] = shape
      w = 2*height/3.0
      shape = triangle(0,w,width,w,width/2,0)
      shape = subtract(shape,triangle(0,w+2*line,width,w+2*line,width/2,2*line))
      shapes['v'] = shape
      shape = triangle(0,height,width,height,width/2,0)
      shape = add(shape,move(shape,.6*width,0))
      cutout = triangle(0,height+4*line,width,height+4*line,width/2,4*line)
      cutout = add(cutout,move(cutout,.6*width,0))
      shape = subtract(shape,cutout)
      shape = scale_x(shape,0,1/1.6)
      shapes['W'] = shape
      shape = scale_y(shapes['W'],0,width/height)
      shapes['w'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,triangle(0,0,0,height,width/2-.7*line,height/2))
      shape = subtract(shape,triangle(width,0,width/2+.7*line,height/2,width,height))
      shape = subtract(shape,triangle(1.1*line,height,width-1.1*line,height,width/2,height/2+line))
      shape = subtract(shape,triangle(1.1*line,0,width/2,height/2-line,width-1.1*line,0))
      shapes['X'] = shape
      w = 2*height/3.0
      shape = rectangle(0,width,0,w)
      shape = subtract(shape,triangle(0,0,0,w,width/2-.75*line,w/2))
      shape = subtract(shape,triangle(width,0,width/2+.75*line,w/2,width,w))
      shape = subtract(shape,triangle(1.25*line,0,width/2,w/2-.75*line,width-1.25*line,0))
      shape = subtract(shape,triangle(1.25*line,w,width-1.25*line,w,width/2,w/2+.75*line))
      shapes['x'] = shape
      w = height/2
      shape = rectangle(0,width,w,height)
      shape = subtract(shape,triangle(0,w,0,height,width/2-line/2,w))
      shape = subtract(shape,triangle(width/2+line/2,w,width,height,width,w))
      shape = subtract(shape,triangle(1.1*line,height,width-1.1*line,height,width/2,w+1.1*line))
      shape = add(shape,rectangle(width/2-line/2,width/2+line/2,0,w))
      shapes['Y'] = shape
      shape = rectangle(0,width,-height/3,width)
      shape = subtract(shape,triangle(0,-height/3,0,width,width/2-.9*line,0))
      shape = subtract(shape,triangle(1.1*line,width,width-1.1*line,width,width/2-.2*line,1.6*line))
      shape = subtract(shape,triangle(1.2*line,-height/3,width,width,width,-height/3))
      shapes['y'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,triangle(0,line,0,height-line,width-1.4*line,height-line))
      shape = subtract(shape,triangle(1.4*line,line,width,height-line,width,line))
      shapes['Z'] = shape
      w = 2*height/3
      shape = rectangle(0,width,0,w)
      shape = subtract(shape,triangle(0,line,0,w-line,width-1.6*line,w-line))
      shape = subtract(shape,triangle(width,line,1.6*line,line,width,w-line))
      shapes['z'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-.9*line))
      shape = scale_y(shape,0,height/width)
      shapes['0'] = shape
      shape = rectangle(width/2-line/2,width/2+line/2,0,height)
      w = width/2-line/2
      cutout = circle(0,height,w)
      shape = add(shape,rectangle(0,width/2,height-w-line,height))
      shape = subtract(shape,cutout)
      shape = move(shape,(width/2+line/2)/4,0)
      shapes['1'] = shape
      shape = circle(width/2,height-width/2,width/2)
      shape = subtract(shape,circle(width/2,height-width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width/2,0,height-width/2))
      shape = add(shape,rectangle(0,width,0,height-width/2))
      shape = subtract(shape,triangle(0,line,0,height-width/2,width-line,height-width/2))
      shape = subtract(shape,triangle(1.5*line,line,width,height-width/2-.5*line,width,line))
      shapes['2'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = scale_y(shape,0,(height/2+line/2)/width)
      shape = add(shape,move(shape,0,height/2-line/2))
      shape = subtract(shape,rectangle(0,width/2,height/4,3*height/4))
      shapes['3'] = shape
      shape = rectangle(width-line,width,0,height)
      shape = add(shape,triangle(0,height/3,width-line,height,width-line,height/3))
      shape = subtract(shape,triangle(1.75*line,height/3+line,width-line,height-1.5*line,width-line,height/3+line))
      shapes['4'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width/2,width/2,width))
      shape = add(shape,rectangle(0,width/2,width-line,width))
      shape = add(shape,rectangle(0,line,width-line,height))
      shape = add(shape,rectangle(0,width,height-line,height))
      shapes['5'] = shape
      shape = circle(width/2,height-width/2,width/2)
      shape = subtract(shape,circle(width/2,height-width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width,0,height-width/2))
      shape = subtract(shape,triangle(width,height,width,height/2,width/2,height/2))
      shape = add(shape,circle(width/2,width/2,width/2))
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = add(shape,rectangle(0,line,width/2,height-width/2))
      shapes['6'] = shape
      shape = rectangle(0,width,0,height)
      shape = subtract(shape,triangle(0,0,0,height-line,width-line,height-line))
      shape = subtract(shape,triangle(line,0,width,height-line,width,0))
      shapes['7'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = scale_y(shape,0,(height/2+line/2)/width)
      shape = add(shape,move(shape,0,height/2-line/2))
      shapes['8'] = shape
      shape = circle(width/2,width/2,width/2)
      shape = subtract(shape,circle(width/2,width/2,width/2-line))
      shape = subtract(shape,rectangle(0,width,width/2,height))
      shape = subtract(shape,triangle(0,0,0,height/2,width/2,height/2))
      shape = add(shape,circle(width/2,height-width/2,width/2))
      shape = subtract(shape,circle(width/2,height-width/2,width/2-line))
      shape = add(shape,rectangle(width-line,width,width/2,height-width/2))
      shapes['9'] = shape
      w = width/2
      shape = circle(w,w,w)
      shape = subtract(shape,circle(w,w,w-line))
      shape = subtract(shape,rectangle(w,width,0,height))
      shape = scale_y(shape,0,height/width)
      shape = move(shape,w/2,0)
      shapes['('] = shape
      shape = reflect_x(shape,width)
      shapes[')'] = shape
      shapes[' '] = false
      shape = rectangle(width/2-width/3,width/2+width/3,height/2-line/2,height/2+line/2)
      shape = add(shape,rectangle(width/2-line/2,width/2+line/2,height/2-width/3,height/2+width/3))
      shapes['+'] = shape
      shape = rectangle(width/2-width/3,width/2+width/3,height/2-line/2,height/2+line/2)
      shapes['-'] = shape
      shape = circle(width/2,line,.75*line)
      shapes['.'] = shape
      shape = rectangle(0,width,0,height)
      d = .8*line
      shape = subtract(shape,triangle(d,0,width,height-d,width,0))
      shape = subtract(shape,triangle(0,d,0,height,width-d,height))
      shapes['/'] = shape
      #
      # to be done
      #
      shapes['*'] = shape
      shapes['~'] = shape
      shapes['!'] = shape
      shapes['@'] = shape
      shapes['#'] = shape
      shapes['$'] = shape
      shapes['%'] = shape
      shapes['^'] = shape
      shapes['&'] = shape
      shapes['&'] = shape
      shapes['_'] = shape
      shapes['='] = shape
      shapes['['] = shape
      shapes['{'] = shape
      shapes[']'] = shape
      shapes['}'] = shape
      shapes[';'] = shape
      shapes[':'] = shape
      shapes["'"] = shape
      shapes['"'] = shape
      shapes[','] = shape
      shapes['<'] = shape
      shapes['>'] = shape
      shapes['?'] = shape
      #
      # add a line to text shape
      #
      def addline(lineshape):
         #
         # LR align
         #
         if (align[0] == 'C'):
            lineshape = move(lineshape,-self.width/2.0,0)
         elif (align[0] == 'R'):
            lineshape = move(lineshape,-self.width,0)
         #
         # add
         #
         self.shape = add(self.shape,lineshape)
      #
      # loop over chars
      #
      dx = 0
      dy = -height
      self.width = -space
      self.height = height
      lineshape = false
      self.shape = false
      for chr in text:
         if (chr == '\n'):
            addline(lineshape)
            dx = 0
            dy -= 1.5*self.height
            self.width = -space
            self.height += 1.5*self.height
            lineshape = false
         else:
            lineshape = add(lineshape,move(shapes[chr],dx,dy))
            self.width += space + width
            dx += width + space
      addline(lineshape)
      #
      # UD align
      #
      if (align[1] == 'C'):
         self.shape = move(self.shape,0,self.height/2.0)
      elif (align[1] == 'B'):
         self.shape = move(self.shape,0,self.height)
      #
      # rotate
      #
      if (angle == 90):
         self.shape = rotate_90(self.shape)
      elif (angle == 180):
         self.shape = rotate_180(self.shape)
      elif ((angle == 270) | (angle == -90)):
         self.shape = rotate_270(self.shape)
      elif (angle != 0):
         self.shape = rotate(self.shape,angle)
      #
      # translate
      #
      self.shape = move(self.shape,x,y)
      #
      # color
      #
      self.shape = '('+str(color)+'*(('+self.shape+')!=0))'

#
# PCB classes and definitions
#

class PCB:
   def __init__(self,x0,y0,width,height,mask):
      self.board = false
      self.labels = false
      self.interior = rectangle(x0,x0+width,y0,y0+height)
      self.exterior = subtract(true,rectangle(x0,x0+width,y0,y0+height))
      self.mask = false
      self.holes = false
   def add(self,part):
      self.board = add(self.board,part)
      self.mask = add(self.mask,move(part,-mask,mask))
      self.mask = add(self.mask,move(part,-mask,-mask))
      self.mask = add(self.mask,move(part,mask,mask))
      self.mask = add(self.mask,move(part,mask,-mask))
      return self

class point:
   def __init__(self,x,y,z=0):
      self.x = x
      self.y = y
      self.z = z

class part:
   class text:
      def __init__(self,x,y,z=0,text='',line=0.006,angle=0):
         self.x = x
         self.y = y
         self.z = z
         self.text = text
         self.line = line 
         self.angle = angle
   def add(self,pcb,x,y,z=0,angle=0,line=0.007):
      self.x = x
      self.y = y
      self.z = z
      self.angle = angle
      if (angle == 90):
         self.shape = rotate_90(self.shape)
      elif (angle == 180):
         self.shape = rotate_180(self.shape)
      elif ((angle == 270) | (angle == -90)):
         self.shape = rotate_270(self.shape)
      elif (angle != 0):
         self.shape = rotate(self.shape,angle)
      self.shape = translate(self.shape,x,y,z)
      if hasattr(self,'holes'):
         if (angle == 90):
            self.holes = rotate_90(self.holes)
         elif (angle == 180):
            self.holes = rotate_180(self.holes)
         elif ((angle == 270) | (angle == -90)):
            self.holes = rotate_270(self.holes)
         elif (angle != 0):
            self.holes = rotate(self.holes,angle)
         self.holes = translate(self.holes,x,y,z)
      deg_angle = angle
      angle = math.pi*angle/180
      for i in range(len(self.pad)):
         xnew = math.cos(angle)*self.pad[i].x - math.sin(angle)*self.pad[i].y
         ynew = math.sin(angle)*self.pad[i].x + math.cos(angle)*self.pad[i].y
         self.pad[i].x = x + xnew
         self.pad[i].y = y + ynew
         self.pad[i].z += z
      pcb.labels = add(pcb.labels,text(self.value,x,y,z,line=line,color=Green).shape)
      for i in range(len(self.labels)):
         xnew = math.cos(angle)*self.labels[i].x - math.sin(angle)*self.labels[i].y
         ynew = math.sin(angle)*self.labels[i].x + math.cos(angle)*self.labels[i].y
         self.labels[i].x = x + xnew
         self.labels[i].y = y + ynew
         self.labels[i].z += z
         if ((-90 < deg_angle) & (deg_angle <= 90)):
            pcb.labels = add(pcb.labels,text(self.labels[i].text,self.labels[i].x,self.labels[i].y,self.labels[i].z,self.labels[i].line,color=Red,angle=deg_angle-self.labels[i].angle).shape)
         else:
            pcb.labels = add(pcb.labels,text(self.labels[i].text,self.labels[i].x,self.labels[i].y,self.labels[i].z,self.labels[i].line,color=Red,angle=(deg_angle-self.labels[i].angle-180)).shape)
      pcb = pcb.add(self.shape)
      if hasattr(self,'holes'):
         pcb.holes = add(pcb.holes,self.holes)
      return pcb

def wire(pcb,width,*points):
   x0 = points[0].x
   y0 = points[0].y
   z0 = points[0].z
   pcb.board = add(pcb.board,cylinder(x0,y0,z0,z0,width/2))
   for i in range(1,len(points)):
      x0 = points[i-1].x
      y0 = points[i-1].y
      z0 = points[i-1].z
      x1 = points[i].x
      y1 = points[i].y
      z1 = points[i].z
      pcb.board = add(pcb.board,line(x0,y0,x1,y1,z1,width))
      pcb.board = add(pcb.board,cylinder(x1,y1,z1,z1,width/2))
   return pcb

def wirer(pcb,width,*points):
   for i in range(1,len(points)):
      x0 = points[i-1].x
      y0 = points[i-1].y
      z0 = points[i-1].z
      x1 = points[i].x
      y1 = points[i].y
      z1 = points[i].z
      if (x0 < x1):
         pcb.board = add(pcb.board,cube(x0-width/2,x1+width/2,y0-width/2,y0+width/2,z0,z0))
      elif (x1 < x0):
         pcb.board = add(pcb.board,cube(x1-width/2,x0+width/2,y0-width/2,y0+width/2,z0,z0))
      if (y0 < y1):
         pcb.board = add(pcb.board,cube(x1-width/2,x1+width/2,y0-width/2,y1+width/2,z0,z0))
      elif (y1 < y0):
         pcb.board = add(pcb.board,cube(x1-width/2,x1+width/2,y1-width/2,y0+width/2,z0,z0))
   return pcb

#
# PCB library
#

class via(part):
   #
   # via
   #
   def __init__(self,zb,zt,rv,rp,value=''):
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = cylinder(0,0,zb,zt,rp)
      self.holes = cylinder(0,0,zb,zt,rv)
      self.pad.append(point(0,0,zt))
      self.pad.append(point(0,0,zb))


class SJ(part):
   #
   # solder jumper
   #
   def __init__(self,value=''):
      pad_SJ = cube(-.02,.02,-.03,.03,0,0)
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = translate(pad_SJ,-.029,0,0)
      self.pad.append(point(-.029,0,0))
      self.shape = add(self.shape,translate(pad_SJ,.029,0,0))
      self.pad.append(point(.029,0,0))

#
# discretes
#

pad_0402 = cube(-.0175,.0175,-.014,.014,0,0)

class R_0402(part):
   #
   # 0402 resistor
   #
   def __init__(self,value=''):
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = translate(pad_0402,-.0265,0,0)
      self.pad.append(point(-.0265,0,0))
      self.shape = add(self.shape,translate(pad_0402,.0265,0,0))
      self.pad.append(point(.0265,0,0))

pad_1206 = cube(-.032,.032,-.034,.034,0,0)

class R_1206(part):
   #
   # 1206 resistor
   #
   def __init__(self,value=''):
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = translate(pad_1206,-.06,0,0)
      self.pad.append(point(-.06,0,0))
      self.shape = add(self.shape,translate(pad_1206,.06,0,0))
      self.pad.append(point(.06,0,0))

class C_1206(part):
   #
   # 1206 capacitor
   #
   def __init__(self,value=''):
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = translate(pad_1206,-.06,0,0)
      self.pad.append(point(-.06,0,0))
      self.shape = add(self.shape,translate(pad_1206,.06,0,0))
      self.pad.append(point(.06,0,0))

pad_1210 = cube(-.032,.032,-.048,.048,0,0)

class L_1210(part):
   #
   # 1210 inductor
   #
   def __init__(self,value=''):
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = translate(pad_1210,-.06,0,0)
      self.pad.append(point(-.06,0,0))
      self.shape = add(self.shape,translate(pad_1210,.06,0,0))
      self.pad.append(point(.06,0,0))

pad_choke = cube(-.06,.06,-.06,.06,0,0)

class choke(part):
   #
   # Panasonic ELLCTV
   #
   def __init__(self,value=''):
      self.value = value
      self.labels = []
      self.pad = [point(0,0,0)]
      self.shape = translate(pad_choke,-.177,-.177,0)
      self.pad.append(point(-.177,-.177,0))
      self.shape = add(self.shape,translate(pad_choke,.177,.177,0))
      self.pad.append(point(.177,.177,0))

#
# connectors
#

class header_UPDI(part):
   #
   # UPDI header
   #    Sullins GEC36SBSN-M89	
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: UPDI
      #
      self.shape = translate(pad_header,0,-.05,0)
      self.shape = add(self.shape,cylinder(.05,-.05,0,0,.025))
      self.pad.append(point(0,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'UPDI'))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_header,0,.05,0))
      self.pad.append(point(0,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class header_UPDI_reverse(part):
   #
   # UPDI header, reverse for female connector
   #    GCT BG300-03-A-L-A	
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: UPDI
      #
      self.shape = translate(pad_header,0,.05,0)
      self.shape = add(self.shape,cylinder(.05,.05,0,0,.025))
      self.pad.append(point(0,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'UPDI'))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_header,0,-.05,0))
      self.pad.append(point(0,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class USB_A_plug(part):
   #
   # USB type A PCB plug
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: 5V
      #
      self.shape = translate(cube(-.05,.242,-.02,.02,0,0),0,.138,0)
      self.pad.append(point(0,.138,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'5V'))
      #
      # pin 2: D-
      #
      self.shape = add(self.shape,translate(cube(-0.05,.202,-.02,.02,0,0),0,.039,0))
      self.pad.append(point(0,.039,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'D-'))
      #
      # pin 3: D+
      #
      self.shape = add(self.shape,translate(cube(-.05,.202,-.02,.02,0,0),0,-.039,0))
      self.pad.append(point(0,-.039,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'D+'))
      #
      # pin 4: GND
      #
      self.shape = add(self.shape,translate(cube(-.05,.242,-.02,.02,0,0),0,-.138,0))
      self.pad.append(point(0,-.138,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # plug cutout
      #
      self.holes = cube(-.05,1,.24,1,zb,zt)
      self.holes = add(self.holes,cube(-.05,1,-1,-.24,zb,zt))

class header_SWD(part):
   #
   # Serial Wire Debug programming header
   # Amphenol 20021121-00010T1LF	2x5x0.05
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 0.077
      w = 0.015
      h = .047
      pad = cube(-h,h,-w,w,0,0)
      #
      # pin 1: VCC
      #
      self.shape = translate(pad,d,-.1,0)
      self.shape = add(self.shape,cylinder(d+h,-.1,0,0,w))
      self.pad.append(point(d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 2: DIO
      #
      self.shape = add(self.shape,translate(pad,-d,-.1,0))
      self.pad.append(point(-d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DIO'))
      #
      # pin 3: GND
      #
      self.shape = add(self.shape,translate(pad,d,-.05,0))
      self.pad.append(point(d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 4: CLK
      #
      self.shape = add(self.shape,translate(pad,-d,-.05,0))
      self.pad.append(point(-d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLK'))
      #
      # pin 5: GND
      #
      self.shape = add(self.shape,translate(pad,d,0,0))
      self.pad.append(point(d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 6: SWO
      #
      self.shape = add(self.shape,translate(pad,-d,0,0))
      self.pad.append(point(-d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SWO'))
      #
      # pin 7: KEY
      #
      self.shape = add(self.shape,translate(pad,d,.05,0))
      self.pad.append(point(d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'KEY'))
      #
      # pin 8: NC
      #
      self.shape = add(self.shape,translate(pad,-d,.05,0))
      self.pad.append(point(-d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC'))
      #
      # pin 9: GND
      #
      self.shape = add(self.shape,translate(pad,d,.1,0))
      self.pad.append(point(d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 10: nRESET
      #
      self.shape = add(self.shape,translate(pad,-d,.1,0))
      self.pad.append(point(-d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST'))

class ESC(part):
   #
   # ESC 3x1
   # Sullins S1013E-36-ND
   #
   def __init__(self,value=''):
      pad_header = cube(-.1,.1,-.05/2,.05/2,0,0)
      d = .075
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: PWM
      #
      self.shape = translate(pad_header,-d,-.1,0)
      self.pad.append(point(-d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PWM'))
      #
      # pin 2: 5V
      #
      self.shape = add(self.shape,translate(pad_header,d,0,0))
      self.pad.append(point(d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'5V'))
      #
      # pin 3: GND 
      #
      self.shape = add(self.shape,translate(pad_header,-d,.1,0))
      self.pad.append(point(-d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class I2C4x1(part):
   #
   # I2C 4x1
   # Sullins S5635-ND
   #
   def __init__(self,value=''):
      pad_header = cube(-.079/2,.079/2,-.039/2,.039/2,0,0)
      d = .209/2-.079/2
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: VCC
      #
      self.shape = translate(pad_header,-d,-.15,0)
      self.pad.append(point(-d,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1VCC'))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_header,d,-.05,0))
      self.pad.append(point(d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 3: SCL
      #
      self.shape = add(self.shape,translate(pad_header,-d,.05,0))
      self.pad.append(point(-d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCL'))
      #
      # pin 4: SDA
      #
      self.shape = add(self.shape,translate(pad_header,d,.15,0))
      self.pad.append(point(d,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDA'))

class I2C4x1i(part):
   #
   # I2C 4x1 inline
   #
   def __init__(self,value=''):
      pad_header = cube(-.079/2,.079/2,-.039/2,.039/2,0,0)
      d = 0
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: VCC
      #
      self.shape = translate(pad_header,-d,-.15,0)
      self.pad.append(point(-d,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1VCC'))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_header,d,-.05,0))
      self.pad.append(point(d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 3: SCL
      #
      self.shape = add(self.shape,translate(pad_header,-d,.05,0))
      self.pad.append(point(-d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCL'))
      #
      # pin 4: SDA
      #
      self.shape = add(self.shape,translate(pad_header,d,.15,0))
      self.pad.append(point(d,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDA'))

class RCWL0516(part):
   #
   # RCWL-0516 Doppler radar
   #
   def __init__(self,value=''):
      pad_header = cube(-.065,.065,-.025,.025,0,0)
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: 3.3V
      #
      self.shape = translate(pad_header,.107,-.2,0)
      self.shape = add(self.shape,cylinder(.172,-.2,0,0,.025))
      self.pad.append(point(.107,-.2,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3.3V'))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 3: OUT
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'OUT'))
      #
      # pin 4: VIN
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VIN'))
      #
      # pin 5: CDS
      #
      self.shape = add(self.shape,translate(pad_header,.107,.2,0))
      self.pad.append(point(.107,.2,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CDS'))

class microSD(part):
   #
   # microSD
   # Amphenol 114-00841-68
   # 
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+7*.0433,-.304,0)
      self.pad.append(point(-.177+7*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1NC',angle=90))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+6*.0433,-.304,0))
      self.pad.append(point(-.177+6*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'/CS',angle=90))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+5*.0433,-.304,0))
      self.pad.append(point(-.177+5*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MOSI',angle=90))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+4*.0433,-.304,0))
      self.pad.append(point(-.177+4*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V',angle=90))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+3*.0433,-.304,0))
      self.pad.append(point(-.177+3*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLK',angle=90))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+2*.0433,-.304,0))
      self.pad.append(point(-.177+2*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',angle=90))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+1*.0433,-.304,0))
      self.pad.append(point(-.177+1*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MISO',angle=90))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(cube(-.0138,.0138,-.034,.034,0,0),-.177+0*.0433,-.304,0))
      self.pad.append(point(-.177+0*.0433,-.304,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',angle=90))
      #
      # feet
      #
      self.shape = add(self.shape,translate(cube(-.021,.021,-.029,.029,0,0),-.228,-.299,0)) # leave extra space for 1/64 milling
      self.shape = add(self.shape,translate(cube(-.029,.029,-.029,.029,0,0),.222,-.299,0))
      self.shape = add(self.shape,translate(cube(-.015,.015,-.029,.025,0,0),-.232,0,0)) # leave extra space for 1/64 milling
      self.shape = add(self.shape,translate(cube(-.015,.015,-.029,.029,0,0),-.232+.47,.025,0))
      self.shape = add(self.shape,translate(cube(-.028,.028,-.019,.019,0,0),-.221,.059,0))
      self.shape = add(self.shape,translate(cube(-.019,.019,-.030,.030,0,0),.222,.121,0))

pad_USB_trace = cube(-.0075,.0075,-.04,.04,0,0)
pad_USB_feet = cube(-.049,.049,-.043,.043,0,0)

class USB_mini_B(part):
   #
   # USB mini B
   # Hirose UX60-MB-5ST
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_USB_trace,.063,.36,0)
      self.pad.append(point(.063,.36,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_USB_trace,.0315,.36,0))
      self.pad.append(point(.0315,.36,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_USB_trace,0,.36,0))
      self.pad.append(point(0,.36,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'+'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_USB_trace,-.0315,.36,0))
      self.pad.append(point(-.0315,.36,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'-'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_USB_trace,-.063,.36,0))
      self.pad.append(point(-.063,.36,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # feet
      #
      self.shape = add(self.shape,translate(pad_USB_feet,.165,.33,0))
      self.shape = add(self.shape,translate(pad_USB_feet,-.165,.33,0))
      self.shape = add(self.shape,translate(pad_USB_feet,.165,.12,0))
      self.shape = add(self.shape,translate(pad_USB_feet,-.165,.12,0))

pad_header = cube(-.05,.05,-.025,.025,0,0)

class header_4(part):
   #
   # 4-pin header
   # fci 95278-101a04lf bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_header,-.107,.05,0)
      self.shape = add(self.shape,cylinder(-.157,.05,0,0,.025))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'2'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_header,.107,-.05,0))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'4'))

class header_signal(part):
   #
   # signal header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 3: signal
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'signal'))
      #
      # pin 4:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))


class header_power(part):
   #
   # power header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 3: V
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 4:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))

class header_i0(part):
   #
   # i0 header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: data
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'data'))
      #
      # pin 3: V
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 4:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))

class header_serial(part):
   #
   # serial comm header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2:DTR
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DTR'))
      #
      # pin 3: Tx
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Tx'))
      #
      # pin 4: Rx
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Rx'))

class header_bus(part):
   #
   # bus header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: Tx
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Tx'))
      #
      # pin 3: V
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 4: Rx
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Rx'))

class header_I2C(part):
   #
   # I2C header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: SCL
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCL'))
      #
      # pin 2: G
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 3: SDA
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDA'))
      #
      # pin 4: V
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))

class header_APA(part):
   #
   # APA header
   # FCI 95278-101A04LF Bergstik 2x2x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_header,.107,-.05,0)
      self.shape = add(self.shape,cylinder(.157,-.05,0,0,.025))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: in
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'in'))
      #
      # pin 3: V
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 4: out
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'out'))

class header_6(part):
   #
   # 6-pin header
   # FCI 95278-101A06LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_header,.107,-.1,0)
      self.shape = add(self.shape,cylinder(.157,-.1,0,0,.025))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))

class header_ATP(part):
   #
   # Asynchronous Token Protocol header
   # FCI 95278-101A06LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_header,.107,-.1,0)
      self.shape = add(self.shape,cylinder(.157,-.1,0,0,.025))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'BI'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TI'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TO'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'BO'))

class header_PDI(part):
   #
   # in-circuit PDI programming header
   # FCI 95278-101A06LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Data
      #
      self.shape = translate(pad_header,.107,-.1,0)
      self.shape = add(self.shape,cylinder(.157,-.1,0,0,.025))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DAT'))
      #
      # pin 2: VCC
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 3: NC 
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC'))
      #
      # pin 4: NC
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC'))
      #
      # pin 5: Clock
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLK'))
      #
      # pin 6: GND
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class header_ISP(part):
   #
   # in-circuit ISP programming header
   # FCI 95278-101A06LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: MISO
      #
      self.shape = translate(pad_header,.107,-.1,0)
      self.shape = add(self.shape,cylinder(.157,-.1,0,0,.025))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MISO'))
      #
      # pin 2: V
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 3: SCK
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK'))
      #
      # pin 4: MOSI
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MOSI'))
      #
      # pin 5: RST
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST'))
      #
      # pin 6: GND
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class header_nRF24L01(part):
   #
   # nRF24L01 module header
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1:
      #
      self.shape = translate(pad_header,.107,-.15,0)
      self.shape = add(self.shape,cylinder(.157,-.15,0,0,.025))
      self.pad.append(point(.107,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.15,0))
      self.pad.append(point(-.107,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 3:
      #
      self.shape = add(self.shape,translate(pad_header,.107,-.05,0))
      self.pad.append(point(.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CE'))
      #
      # pin 4:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.05,0))
      self.pad.append(point(-.107,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CS'))
      #
      # pin 5:
      #
      self.shape = add(self.shape,translate(pad_header,.107,.05,0))
      self.pad.append(point(.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK'))
      #
      # pin 6:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.05,0))
      self.pad.append(point(-.107,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MOSI'))
      #
      # pin 7:
      #
      self.shape = add(self.shape,translate(pad_header,.107,.15,0))
      self.pad.append(point(.107,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MISO'))
      #
      # pin 8:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.15,0))
      self.pad.append(point(-.107,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IRQ'))

class header_servo(part):
   #
   # servo motor header
   # FCI 95278-101A06LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: ground
      #
      self.shape = translate(pad_header,.107,-.1,0)
      self.shape = add(self.shape,cylinder(.157,-.1,0,0,.025))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G/blk'))
      #
      # pin 2: ground
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G/blk'))
      #
      # pin 3: power
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V/red'))
      #
      # pin 4: power
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V/red'))
      #
      # pin 5: signal 0
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'S0/wht'))
      #
      # pin 6: signal 1
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'S1/wht'))

class header_unipolar_stepper(part):
   #
   # unipolar stepper header
   # FCI 95278-101A06LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_header,.107,-.1,0)
      self.shape = add(self.shape,cylinder(.157,-.1,0,0,.025))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'red'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'green'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'black'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'brown'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'orange'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'yellow'))

class header_LCD(part):
   #
   # LCD interface header
   # FCI 95278-101A10LF Bergstik 2x3x0.1"
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1:
      #
      self.shape = translate(pad_header,.107,-.2,0)
      self.shape = add(self.shape,cylinder(.157,-.2,0,0,.025))
      self.pad.append(point(.107,-.2,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DB7\n14'))
      #
      # pin 2:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.2,0))
      self.pad.append(point(-.107,-.2,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DB6\n13'))
      #
      # pin 3:
      #
      self.shape = add(self.shape,translate(pad_header,.107,-.1,0))
      self.pad.append(point(.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DB5\n12'))
      #
      # pin 4:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,-.1,0))
      self.pad.append(point(-.107,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DB4\n11'))
      #
      # pin 5:
      #
      self.shape = add(self.shape,translate(pad_header,.107,0,0))
      self.pad.append(point(.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'E\n6'))
      #
      # pin 6:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,0,0))
      self.pad.append(point(-.107,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'R/W\n5'))
      #
      # pin 7:
      #
      self.shape = add(self.shape,translate(pad_header,.107,.1,0))
      self.pad.append(point(.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RS\n4'))
      #
      # pin 8:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.1,0))
      self.pad.append(point(-.107,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Vee\n3'))
      #
      # pin 9:
      #
      self.shape = add(self.shape,translate(pad_header,.107,.2,0))
      self.pad.append(point(.107,.2,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Vcc\n2'))
      #
      # pin 10:
      #
      self.shape = add(self.shape,translate(pad_header,-.107,.2,0))
      self.pad.append(point(-.107,.2,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND\n1'))

class header_serial_reverse(part):
   #
   # serial cable header, reverse for female connector
   #    GCT BG300-06-A-L-A	
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_header,0,-.25,0)
      self.shape = add(self.shape,cylinder(-.05,-.25,0,0,.025))
      self.pad.append(point(0,-.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: CTS (brown)
      #
      self.shape = add(self.shape,translate(pad_header,0,-.15,0))
      self.pad.append(point(0,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CTS'))
      #
      # pin 3: VCC (red)
      #
      self.shape = add(self.shape,translate(pad_header,0,-.05,0))
      self.pad.append(point(0,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 4: Tx (orange)
      #
      self.shape = add(self.shape,translate(pad_header,0,0.05,0))
      self.pad.append(point(0,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Tx'))
      #
      # pin 5: Rx (yellow)
      #
      self.shape = add(self.shape,translate(pad_header,0,.15,0))
      self.pad.append(point(0,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Rx'))
      #
      # pin 6: RTS (green)
      #
      self.shape = add(self.shape,translate(pad_header,0,.25,0))
      self.pad.append(point(0,.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RTS'))

class header_FTDI(part):
   #
   # FTDI cable header
   #    Sullins GEC36SBSN-M89	
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_header,0,.25,0)
      self.shape = add(self.shape,cylinder(-.05,.25,0,0,.025))
      self.pad.append(point(0,.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: CTS (brown)
      #
      self.shape = add(self.shape,translate(pad_header,0,.15,0))
      self.pad.append(point(0,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CTS'))
      #
      # pin 3: VCC (red)
      #
      self.shape = add(self.shape,translate(pad_header,0,.05,0))
      self.pad.append(point(0,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 4: Tx (orange)
      #
      self.shape = add(self.shape,translate(pad_header,0,-0.05,0))
      self.pad.append(point(0,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Tx'))
      #
      # pin 5: Rx (yellow)
      #
      self.shape = add(self.shape,translate(pad_header,0,-.15,0))
      self.pad.append(point(0,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Rx'))
      #
      # pin 6: RTS (green)
      #
      self.shape = add(self.shape,translate(pad_header,0,-.25,0))
      self.pad.append(point(0,-.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RTS'))

class HCSR04(part):
   #
   # HC-SR04 sonar header
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_header,0,.15,0)
      self.shape = add(self.shape,cylinder(-.05,.15,0,0,.025))
      self.pad.append(point(0,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: echo
      #
      self.shape = add(self.shape,translate(pad_header,0,.05,0))
      self.pad.append(point(0,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'echo'))
      #
      # pin 3: trig
      #
      self.shape = add(self.shape,translate(pad_header,0,-.05,0))
      self.pad.append(point(0,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'trig'))
      #
      # pin 4: Vcc
      #
      self.shape = add(self.shape,translate(pad_header,0,-0.15,0))
      self.pad.append(point(0,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Vcc'))

class HCSR501(part):
   #
   # HC-SR501 motion detector header
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Vcc
      #
      self.shape = translate(pad_header,0,.1,0)
      self.shape = add(self.shape,cylinder(-.05,.1,0,0,.025))
      self.pad.append(point(0,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Vcc'))
      #
      # pin 2: out
      #
      self.shape = add(self.shape,translate(pad_header,0,0,0))
      self.pad.append(point(0,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'out'))
      #
      # pin 3: GND
      #
      self.shape = add(self.shape,translate(pad_header,0,-.1,0))
      self.pad.append(point(0,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

pad_RN4871_left = cube(-0.5/25.4,1/25.4,-0.7/2/25.4,0.7/2/25.4,0,0)
pad_RN4871_right = cube(-1/25.4,0.5/25.4,-0.7/2/25.4,0.7/2/25.4,0,0)
pad_RN4871_bot = cube(-0.7/2/25.4,0.7/2/25.4,-0.5/25.4,1/25.4,0,0)

class RN4871(part):
   #
   # RN4871
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      width = 9/25.4
      height = 7.5/25.4
      bottom = 1.9/25.4
      left = 1.5/25.4
      pitch = 1.2/25.4
      size = .004
      #
      # pin 1:
      #
      self.shape = translate(pad_RN4871_left,-width/2.0,-height+bottom+4*pitch,0)
      self.pad.append(point(-width/2.0,-height+bottom+4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'BT_RF',line=size))
      #
      # pin 2: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_left,-width/2.0,-height+bottom+3*pitch,0))
      self.pad.append(point(-width/2.0,-height+bottom+3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=size))
      #
      # pin 3: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_left,-width/2.0,-height+bottom+2*pitch,0))
      self.pad.append(point(-width/2.0,-height+bottom+2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P1_2',line=size))
      #
      # pin 4: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_left,-width/2.0,-height+bottom+1*pitch,0))
      self.pad.append(point(-width/2.0,-height+bottom+1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P1_3',line=size))
      #
      # pin 5: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_left,-width/2.0,-height+bottom+0*pitch,0))
      self.pad.append(point(-width/2.0,-height+bottom+0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P1_7',line=size))
      #
      # pin 6: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_bot,-width/2.0+left+0*pitch,-height,0))
      self.pad.append(point(-width/2.0+left+0*pitch,-height,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P1_6',line=size,angle=90))
      #
      # pin 7: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_bot,-width/2.0+left+1*pitch,-height,0))
      self.pad.append(point(-width/2.0+left+1*pitch,-height,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RX',line=size,angle=90))
      #
      # pin 8: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_bot,-width/2.0+left+2*pitch,-height,0))
      self.pad.append(point(-width/2.0+left+2*pitch,-height,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TX',line=size,angle=90))
      #
      # pin 9: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_bot,-width/2.0+left+3*pitch,-height,0))
      self.pad.append(point(-width/2.0+left+3*pitch,-height,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P3_6',line=size,angle=90))
      #
      # pin 10: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_bot,-width/2.0+left+4*pitch,-height,0))
      self.pad.append(point(-width/2.0+left+4*pitch,-height,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST_N',line=size,angle=90))
      #
      # pin 11: 
      #
      self.shape = add(self.shape,translate(pad_RN4871_bot,-width/2.0+left+5*pitch,-height,0))
      self.pad.append(point(-width/2.0+left+5*pitch,-height,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P0_0',line=size,angle=90))
      #
      # pin 12:
      #
      self.shape = add(self.shape,translate(pad_RN4871_right,width/2.0,-height+bottom+0*pitch,0))
      self.pad.append(point(width/2.0,-height+bottom+0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P0_2',line=size))
      #
      # pin 13:
      #
      self.shape = add(self.shape,translate(pad_RN4871_right,width/2.0,-height+bottom+1*pitch,0))
      self.pad.append(point(width/2.0,-height+bottom+1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=size))
      #
      # pin 14:
      #
      self.shape = add(self.shape,translate(pad_RN4871_right,width/2.0,-height+bottom+2*pitch,0))
      self.pad.append(point(width/2.0,-height+bottom+2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VBAT',line=size))
      #
      # pin 15:
      #
      self.shape = add(self.shape,translate(pad_RN4871_right,width/2.0,-height+bottom+3*pitch,0))
      self.pad.append(point(width/2.0,-height+bottom+3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P2_7',line=size))
      #
      # pin 16:
      #
      self.shape = add(self.shape,translate(pad_RN4871_right,width/2.0,-height+bottom+4*pitch,0))
      self.pad.append(point(width/2.0,-height+bottom+4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P2_0',line=size))

pad_HM11 = cube(-.047,.047,-.0177,.0177,0,0)

class HM11(part):
   #
   # HM-11
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      height = 18.5/25.4 
      width = 13.5/25.4
      pitch = 1.5/25.4
      bottom = 1/25.4
      offset = 0
      size = .004
      #
      # pin 1:
      #
      self.shape = translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+7*pitch,0)
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+7*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RTS',line=size))
      #
      # pin 2: 
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+6*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TX',line=size))
      #
      # pin 3: 
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+5*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CTS',line=size))
      #
      # pin 4: 
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+4*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RX',line=size))
      #
      # pin 5: 
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+3*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',line=size))
      #
      # pin 6: 
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+2*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',line=size))
      #
      # pin 7: 
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+1*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',line=size))
      #
      # pin 8:
      #
      self.shape = add(self.shape,translate(pad_HM11,-width/2.0+offset,-height/2.0+bottom+0*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',line=size))
      #
      # pin 9:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+0*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC',line=size))
      #
      # pin 10:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+1*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',line=size))
      #
      # pin 11:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+2*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST',line=size))
      #
      # pin 12:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+3*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=size))
      #
      # pin 13:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+4*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO3',line=size))
      #
      # pin 14:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+5*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO2',line=size))
      #
      # pin 15:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+6*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO1',line=size))
      #
      # pin 16:
      #
      self.shape = add(self.shape,translate(pad_HM11,width/2.0-offset,-height/2.0+bottom+7*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+7*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO0',line=size))

class ESP32_WROOM(part):
   #
   # ESP32-WROOM
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      pad = cube(-1/25.4,1/25.4,-.4/25.4,.4/25.4,0,0)
      padb = cube(-.4/25.4,.4/25.4,-1/25.4,1/25.4,0,0)
      width = 17/25.4
      height = 25.5/25.4
      pitch = 1.27/25.4
      #
      # pin 1
      #
      self.shape = translate(pad,-width/2,6*pitch,0)
      self.pad.append(point(-width/2,6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad,-width/2,5*pitch,0))
      self.pad.append(point(-width/2,5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3V3'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad,-width/2,4*pitch,0))
      self.pad.append(point(-width/2,4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'EN'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad,-width/2,3*pitch,0))
      self.pad.append(point(-width/2,3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VP'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad,-width/2,2*pitch,0))
      self.pad.append(point(-width/2,2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VN'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad,-width/2,1*pitch,0))
      self.pad.append(point(-width/2,1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO34'))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(pad,-width/2,0*pitch,0))
      self.pad.append(point(-width/2,0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO35'))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(pad,-width/2,-1*pitch,0))
      self.pad.append(point(-width/2,-1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO32'))
      #
      # pin 9
      #
      self.shape = add(self.shape,translate(pad,-width/2,-2*pitch,0))
      self.pad.append(point(-width/2,-2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO33'))
      #
      # pin 10
      #
      self.shape = add(self.shape,translate(pad,-width/2,-3*pitch,0))
      self.pad.append(point(-width/2,-3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO25'))
      #
      # pin 11
      #
      self.shape = add(self.shape,translate(pad,-width/2,-4*pitch,0))
      self.pad.append(point(-width/2,-4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO26'))
      #
      # pin 12
      #
      self.shape = add(self.shape,translate(pad,-width/2,-5*pitch,0))
      self.pad.append(point(-width/2,-5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO27'))
      #
      # pin 13
      #
      self.shape = add(self.shape,translate(pad,-width/2,-6*pitch,0))
      self.pad.append(point(-width/2,-6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO14'))
      #
      # pin 14
      #
      self.shape = add(self.shape,translate(pad,-width/2,-7*pitch,0))
      self.pad.append(point(-width/2,-7*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO12'))
      #
      # pin 15
      #
      self.shape = add(self.shape,translate(padb,-4.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(-4.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',angle=90))
      #
      # pin 16
      #
      self.shape = add(self.shape,translate(padb,-3.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(-3.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO13',angle=90))
      #
      # pin 17
      #
      self.shape = add(self.shape,translate(padb,-2.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(-2.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SHD',angle=90))
      #
      # pin 18
      #
      self.shape = add(self.shape,translate(padb,-1.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(-1.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SWP',angle=90))
      #
      # pin 19
      #
      self.shape = add(self.shape,translate(padb,-0.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(-0.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCS',angle=90))
      #
      # pin 20
      #
      self.shape = add(self.shape,translate(padb,0.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(0.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK',angle=90))
      #
      # pin 21
      #
      self.shape = add(self.shape,translate(padb,1.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(1.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDO',angle=90))
      #
      # pin 22
      #
      self.shape = add(self.shape,translate(padb,2.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(2.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDI',angle=90))
      #
      # pin 23
      #
      self.shape = add(self.shape,translate(padb,3.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(3.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO15',angle=90))
      #
      # pin 24
      #
      self.shape = add(self.shape,translate(padb,4.5*pitch,-7*pitch-1/25.4,0))
      self.pad.append(point(4.5*pitch,-7*pitch-1/25.4,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO2',angle=90))
      #
      # pin 25
      #
      self.shape = add(self.shape,translate(pad,width/2,-7*pitch,0))
      self.pad.append(point(width/2,-7*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO0'))
      #
      # pin 26
      #
      self.shape = add(self.shape,translate(pad,width/2,-6*pitch,0))
      self.pad.append(point(width/2,-6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO4'))
      #
      # pin 27
      #
      self.shape = add(self.shape,translate(pad,width/2,-5*pitch,0))
      self.pad.append(point(width/2,-5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO16'))
      #
      # pin 28
      #
      self.shape = add(self.shape,translate(pad,width/2,-4*pitch,0))
      self.pad.append(point(width/2,-4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO17'))
      #
      # pin 29
      #
      self.shape = add(self.shape,translate(pad,width/2,-3*pitch,0))
      self.pad.append(point(width/2,-3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO5'))
      #
      # pin 30
      #
      self.shape = add(self.shape,translate(pad,width/2,-2*pitch,0))
      self.pad.append(point(width/2,-2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO18'))
      #
      # pin 31
      #
      self.shape = add(self.shape,translate(pad,width/2,-1*pitch,0))
      self.pad.append(point(width/2,-1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO19'))
      #
      # pin 32
      #
      self.shape = add(self.shape,translate(pad,width/2,0*pitch,0))
      self.pad.append(point(width/2,0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC'))
      #
      # pin 33
      #
      self.shape = add(self.shape,translate(pad,width/2,1*pitch,0))
      self.pad.append(point(width/2,1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO21'))
      #
      # pin 34
      #
      self.shape = add(self.shape,translate(pad,width/2,2*pitch,0))
      self.pad.append(point(width/2,2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RX0'))
      #
      # pin 35
      #
      self.shape = add(self.shape,translate(pad,width/2,3*pitch,0))
      self.pad.append(point(width/2,3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TX0'))
      #
      # pin 36
      #
      self.shape = add(self.shape,translate(pad,width/2,4*pitch,0))
      self.pad.append(point(width/2,4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO22'))
      #
      # pin 37
      #
      self.shape = add(self.shape,translate(pad,width/2,5*pitch,0))
      self.pad.append(point(width/2,5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO23'))
      #
      # pin 38
      #
      self.shape = add(self.shape,translate(pad,width/2,6*pitch,0))
      self.pad.append(point(width/2,6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class ESP32_CAM(part):
   #
   # ESP32-CAM
   # Sullins S5635-ND
   #
   def __init__(self,value=''):
      pad_header = cube(-.079/2,.079/2,-.039/2,.039/2,0,0)
      d = .209/2-.079/2
      w = 0.9
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_header,+d-w/2,.35,0)
      self.pad.append(point(+d-w/2,.35,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'+5V'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_header,-d-w/2,.25,0))
      self.pad.append(point(-d-w/2,.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_header,+d-w/2,.15,0))
      self.pad.append(point(+d-w/2,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO12'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_header,-d-w/2,.05,0))
      self.pad.append(point(-d-w/2,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO13'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_header,+d-w/2,-.05,0))
      self.pad.append(point(+d-w/2,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO15'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_header,-d-w/2,-.15,0))
      self.pad.append(point(-d-w/2,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO14'))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(pad_header,+d-w/2,-.25,0))
      self.pad.append(point(+d-w/2,-.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO2'))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(pad_header,-d-w/2,-.35,0))
      self.pad.append(point(-d-w/2,-.35,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO4'))
      #
      # pin 9
      #
      self.shape = add(self.shape,translate(pad_header,-d+w/2,-.35,0))
      self.pad.append(point(-d+w/2,-.35,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 10
      #
      self.shape = add(self.shape,translate(pad_header,+d+w/2,-.25,0))
      self.pad.append(point(+d+w/2,-.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'U0T'))
      #
      # pin 11
      #
      self.shape = add(self.shape,translate(pad_header,-d+w/2,-.15,0))
      self.pad.append(point(-d+w/2,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'U0R'))
      #
      # pin 12
      #
      self.shape = add(self.shape,translate(pad_header,+d+w/2,-.05,0))
      self.pad.append(point(+d+w/2,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 13
      #
      self.shape = add(self.shape,translate(pad_header,-d+w/2,.05,0))
      self.pad.append(point(-d+w/2,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 14
      #
      self.shape = add(self.shape,translate(pad_header,+d+w/2,.15,0))
      self.pad.append(point(+d+w/2,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO0'))
      #
      # pin 15
      #
      self.shape = add(self.shape,translate(pad_header,-d+w/2,.25,0))
      self.pad.append(point(-d+w/2,.25,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IO16'))
      #
      # pin 16
      #
      self.shape = add(self.shape,translate(pad_header,+d+w/2,.35,0))
      self.pad.append(point(+d+w/2,.35,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3V3'))


class ESP8266_12E(part):
   #
   # ESP8266 12E
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      height = 24/25.4 
      width = 16/25.4
      pitch = 2/25.4
      bottom = 1.8/25.4
      left = 3/25.4
      offset = .4/25.4 - .01
      size = .004
      pad_ESP8266 = cube(-.0493,.0493,-.0197,.0197,0,0)
      pad_ESP8266_bot = cube(-.0197,.0197,-.0415,.0415,0,0)
      #
      # pin 1:
      #
      self.shape = translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+7*pitch,0)
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+7*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST',line=size))
      #
      # pin 2: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+6*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'ADC',line=size))
      #
      # pin 3: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+5*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'EN',line=size))
      #
      # pin 4: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+4*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO16',line=size))
      #
      # pin 5: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+3*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO14',line=size))
      #
      # pin 6: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+2*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO12',line=size))
      #
      # pin 7: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+1*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO13',line=size))
      #
      # pin 8: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266,-width/2.0+offset,-height/2.0+bottom+0*pitch,0))
      self.pad.append(point(-width/2.0+offset,-height/2.0+bottom+0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VDD',line=size))
      #
      # pin 9: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266_bot,-width/2.0+left+0*pitch,-height/2.0+offset,0))
      self.pad.append(point(-width/2.0+left+0*pitch,-height/2.0+offset,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CS',line=size,angle=90))
      #
      # pin 10: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266_bot,-width/2.0+left+1*pitch,-height/2.0+offset,0))
      self.pad.append(point(-width/2.0+left+1*pitch,-height/2.0+offset,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MISO',line=size,angle=90))
      #
      # pin 11: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266_bot,-width/2.0+left+2*pitch,-height/2.0+offset,0))
      self.pad.append(point(-width/2.0+left+2*pitch,-height/2.0+offset,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO9',line=size,angle=90))
      #
      # pin 12: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266_bot,-width/2.0+left+3*pitch,-height/2.0+offset,0))
      self.pad.append(point(-width/2.0+left+3*pitch,-height/2.0+offset,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO10',line=size,angle=90))
      #
      # pin 13: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266_bot,-width/2.0+left+4*pitch,-height/2.0+offset,0))
      self.pad.append(point(-width/2.0+left+4*pitch,-height/2.0+offset,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MOSI',line=size,angle=90))
      #
      # pin 14: 
      #
      self.shape = add(self.shape,translate(pad_ESP8266_bot,-width/2.0+left+5*pitch,-height/2.0+offset,0))
      self.pad.append(point(-width/2.0+left+5*pitch,-height/2.0+offset,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCLK',line=size,angle=90))
      #
      # pin 15:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+0*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+0*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=size))
      #
      # pin 16:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+1*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+1*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO15',line=size))
      #
      # pin 17:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+2*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+2*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO2',line=size))
      #
      # pin 18:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+3*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+3*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO0',line=size))
      #
      # pin 19:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+4*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+4*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO4',line=size))
      #
      # pin 20:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+5*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+5*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GPIO5',line=size))
      #
      # pin 21:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+6*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+6*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RXD',line=size))
      #
      # pin 22:
      #
      self.shape = add(self.shape,translate(pad_ESP8266,width/2.0-offset,-height/2.0+bottom+7*pitch,0))
      self.pad.append(point(width/2.0-offset,-height/2.0+bottom+7*pitch,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TXD',line=size))

pad_MTA = cube(-.021,.021,-.041,.041,0,0)
pad_MTA_solder = cube(-.071,.071,-.041,.041,0,0)

class MTA_2(part):
   #
   # AMP 1445121-2
   # MTA .050 SMT 2-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_MTA,-.025,-.1,0)
      self.pad.append(point(-.025,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_MTA,.025,.1,0))
      self.pad.append(point(.025,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'2'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.187,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.187,0,0))

class MTA_power(part):
   #
   # AMP 1445121-2
   # MTA .050 SMT 2-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_MTA,-.025,-.1,0)
      self.pad.append(point(-.025,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1\nGND'))
      #
      # pin 2: Vcc
      #
      self.shape = add(self.shape,translate(pad_MTA,.025,.1,0))
      self.pad.append(point(.025,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Vcc'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.187,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.187,0,0))

class MTA_3(part):
   #
   # AMP 1445121-3
   # MTA .050 SMT 3-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_MTA,.05,.1,0)
      self.pad.append(point(.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2: power 
      #
      self.shape = add(self.shape,translate(pad_MTA,-.05,.1,0))
      self.pad.append(point(-.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'2'))
      #
      # pin 3: data
      #
      self.shape = add(self.shape,translate(pad_MTA,0,-.1,0))
      self.pad.append(point(0,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.212,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.212,0,0))

class MTA_i0(part):
   #
   # AMP 1445121-3
   # MTA .050 SMT 3-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_MTA,.05,.1,0)
      self.pad.append(point(.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1\nGND'))
      #
      # pin 2: power 
      #
      self.shape = add(self.shape,translate(pad_MTA,-.05,.1,0))
      self.pad.append(point(-.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # pin 3: data
      #
      self.shape = add(self.shape,translate(pad_MTA,0,-.1,0))
      self.pad.append(point(0,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'data'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.212,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.212,0,0))

class MTA_4(part):
   #
   # AMP 1445121-4
   # MTA .050 SMT 4-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_MTA,-.075,-.1,0)
      self.pad.append(point(-.075,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_MTA,.025,-.1,0))
      self.pad.append(point(.025,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'2'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_MTA,.075,.1,0))
      self.pad.append(point(.075,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_MTA,-.025,.1,0))
      self.pad.append(point(-.025,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'4'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.237,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.237,0,0))

class MTA_serial(part):
   #
   # AMP 1445121-4
   # MTA .050 SMT 4-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_MTA,-.075,-.1,0)
      self.pad.append(point(-.075,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2: Tx
      #
      self.shape = add(self.shape,translate(pad_MTA,.025,-.1,0))
      self.pad.append(point(.025,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Tx'))
      #
      # pin 3: Rx
      #
      self.shape = add(self.shape,translate(pad_MTA,.075,.1,0))
      self.pad.append(point(.075,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Rx'))
      #
      # pin 4: DTR
      #
      self.shape = add(self.shape,translate(pad_MTA,-.025,.1,0))
      self.pad.append(point(-.025,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DTR'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.237,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.237,0,0))

class MTA_PS2(part):
   #
   # AMP 1445121-4
   # MTA .050 SMT 4-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_MTA,-.075,-.1,0)
      self.pad.append(point(-.075,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1\nGND'))
      #
      # pin 2: data
      #
      self.shape = add(self.shape,translate(pad_MTA,.025,-.1,0))
      self.pad.append(point(.025,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'data'))
      #
      # pin 3: clock
      #
      self.shape = add(self.shape,translate(pad_MTA,.075,.1,0))
      self.pad.append(point(.075,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'clock'))
      #
      # pin 4: 5V
      #
      self.shape = add(self.shape,translate(pad_MTA,-.025,.1,0))
      self.pad.append(point(-.025,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'5V'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.237,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.237,0,0))

class MTA_5(part):
   #
   # AMP 1445121-5
   # MTA .050 SMT 5-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_MTA,-.1,-.1,0)
      self.pad.append(point(-.1,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_MTA,0,-.1,0))
      self.pad.append(point(0,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'2'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_MTA,.1,-.1,0))
      self.pad.append(point(.1,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_MTA,.05,.1,0))
      self.pad.append(point(.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'4'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_MTA,-.05,.1,0))
      self.pad.append(point(-.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'5'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.262,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.262,0,0))

class MTA_ICP(part):
   #
   # AMP 1445121-5
   # MTA .050 SMT 5-pin vertical
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: MISO
      #
      self.shape = translate(pad_MTA,-.1,-.1,0)
      self.pad.append(point(-.1,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MISO'))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_MTA,0,-.1,0))
      self.pad.append(point(0,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 3: MOSI
      #
      self.shape = add(self.shape,translate(pad_MTA,.1,-.1,0))
      self.pad.append(point(.1,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MOSI'))
      #
      # pin 4: -RESET
      #
      self.shape = add(self.shape,translate(pad_MTA,.05,.1,0))
      self.pad.append(point(.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'-RESET'))
      #
      # pin 5: SCK
      #
      self.shape = add(self.shape,translate(pad_MTA,-.05,.1,0))
      self.pad.append(point(-.05,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_MTA_solder,-.262,0,0))
      self.shape = add(self.shape,translate(pad_MTA_solder,.262,0,0))

pad_screw_terminal = cylinder(0,0,0,0,.047)
hole_screw_terminal = circle(0,0,.025)

class screw_terminal_2(part):
   #
   # On Shore ED555/2DS
   # two position screw terminal
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_screw_terminal,-.069,0,0)
      self.pad.append(point(-.069,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_screw_terminal,.069,0,0))
      self.pad.append(point(.069,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'2'))
      #
      # holes
      #
      self.shape = add(self.shape,translate(hole_screw_terminal,-.069,0,0))
      self.shape = add(self.shape,translate(hole_screw_terminal,.069,0,0))

class screw_terminal_power(part):
   #
   # On Shore ED555/2DS
   # power screw terminal
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_screw_terminal,-.069,0,0)
      self.pad.append(point(-.069,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_screw_terminal,.069,0,0))
      self.pad.append(point(.069,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # holes
      #
      self.shape = add(self.shape,translate(hole_screw_terminal,-.069,0,0))
      self.shape = add(self.shape,translate(hole_screw_terminal,.069,0,0))

class screw_terminal_i0(part):
   #
   # On Shore ED555/3DS
   # i0 screw terminal
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Gnd
      #
      self.shape = translate(pad_screw_terminal,-.138,0,0)
      self.pad.append(point(-.138,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Gnd\n1'))
      #
      # pin 2: data
      #
      self.shape = add(self.shape,pad_screw_terminal)
      self.pad.append(point(0,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'data'))
      #
      # pin 3: V
      #
      self.shape = add(self.shape,translate(pad_screw_terminal,.138,0,0))
      self.pad.append(point(.138,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # holes
      #
      self.shape = add(self.shape,translate(hole_screw_terminal,-.138,0,0))
      self.shape = add(self.shape,hole_screw_terminal)
      self.shape = add(self.shape,translate(hole_screw_terminal,.138,0,0))

class power_65mm(part):
   #
   # CUI PJ1-023-SMT
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: power
      #
      self.shape = cube(.433,.512,-.047,.047,0,0)
      self.pad.append(point(.467,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'P'))
      #
      # pin 2: ground
      #
      self.shape = add(self.shape,cube(.285,.423,-.189,-.098,0,0))
      self.pad.append(point(.354,-.144,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 3: contact
      #
      self.shape = add(self.shape,cube(.325,.463,.098,.189,0,0))
      self.pad.append(point(.394,.144,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'C'))
      #
      # solder pads
      #
      self.shape = add(self.shape,cube(.108,.246,-.169,-.110,0,0))
      self.shape = add(self.shape,cube(.069,.207,.110,.169,0,0))

pad_stereo_2_5mm = cube(-.03,.03,-.05,.05,0,0)

class stereo_2_5mm(part):
   #
   # CUI SJ1-2533-SMT
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: base
      #
      self.shape = translate(pad_stereo_2_5mm,-.130,-.16,0)
      self.pad.append(point(-.130,-.149,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'base'))
      #
      # pin 2: tip
      #
      self.shape = add(self.shape,translate(pad_stereo_2_5mm,.197,.15,0))
      self.pad.append(point(.197,.141,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'tip'))
      #
      # pin 3: middle
      #
      self.shape = add(self.shape,translate(pad_stereo_2_5mm,-.012,-.16,0))
      self.pad.append(point(-.012,-.149,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'middle'))

pad_Molex = cube(-.0155,.0155,-.0265,.0265,0,0)
pad_Molex_solder = cube(-.055,.055,-.065,.065,0,0)

class Molex_serial(part):
   #
   # Molex 53261-0471
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Rx
      #
      self.shape = translate(pad_Molex,-.075,.064,0)
      self.pad.append(point(-.075,.064,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Rx'))
      #
      # pin 2: Tx
      #
      self.shape = add(self.shape,translate(pad_Molex,-.025,.064,0))
      self.pad.append(point(-.025,.064,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Tx'))
      #
      # pin 3: DTR
      #
      self.shape = add(self.shape,translate(pad_Molex,.025,.064,0))
      self.pad.append(point(.025,.064,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DTR'))
      #
      # pin 4: GND
      #
      self.shape = add(self.shape,translate(pad_Molex,.075,.064,0))
      self.pad.append(point(.075,.064,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # solder pads
      #
      self.shape = add(self.shape,translate(pad_Molex_solder,-.16,-.065,0))
      self.shape = add(self.shape,translate(pad_Molex_solder,.16,-.065,0))

#
# switches
#

class slide_switch(part):
   # 
   # slide switch
   # C&K AYZ0102AGRLC
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      pad = cube(-.039/2,.039/2,-.047/2,.047/2,0,0)
      #
      # pad 1
      #
      self.shape = translate(pad,-.098,.1,0)
      self.pad.append(point(-.098,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pad 2
      #
      self.shape = add(self.shape,translate(pad,0,.1,0))
      self.pad.append(point(0,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # pad 3
      #
      self.shape = add(self.shape,translate(pad,.098,.1,0))
      self.pad.append(point(.098,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,''))
      #
      # holes
      #
      self.holes = cylinder(-.118/2,0,zb,zt,.034/2)
      self.holes = add(self.holes,cylinder(.118/2,0,zb,zt,.034/2))

class button_6mm(part):
   # 
   # Omron 6mm pushbutton
   # B3SN-3112P
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      pad_button_6mm = cube(-.04,.04,-.03,.03,0,0)
      #
      # left 1
      #
      self.shape = translate(pad_button_6mm,-.125,.08,0)
      self.pad.append(point(-.125,.08,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'L1'))
      #
      # right 1
      #
      self.shape = add(self.shape,translate(pad_button_6mm,-.125,-.08,0))
      self.pad.append(point(-.125,-.08,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'R1'))
      #
      # right 2
      #
      self.shape = add(self.shape,translate(pad_button_6mm,.125,-.08,0))
      self.pad.append(point(.125,-.08,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'R2'))
      #
      # left 2
      #
      self.shape = add(self.shape,translate(pad_button_6mm,.125,.08,0))
      self.pad.append(point(.125,.08,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'L2'))

#
# crystals and resonators
#

pad_XTAL_EFOBM = cube(-.016,.016,-.085,.085,0,0)

class XTAL_EFOBM(part):
   #
   # Panasonic EFOBM series
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # left
      #
      self.shape = translate(pad_XTAL_EFOBM,-.053,0,0)
      self.pad.append(point(-.053,0,0))
      #
      # ground
      #
      self.shape = add(self.shape,translate(pad_XTAL_EFOBM,0,0,0))
      self.pad.append(point(0,0,0))
      #
      # right
      #
      self.shape = add(self.shape,translate(pad_XTAL_EFOBM,.053,0,0))
      self.pad.append(point(.053,0,0))

pad_XTAL_NX5032GA = cube(-.039,.039,-.047,.047,0,0)
.079

class XTAL_NX5032GA(part):
   #
   # NDK NX5032GA
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # left
      #
      self.shape = translate(pad_XTAL_NX5032GA,-.079,0,0)
      self.pad.append(point(-.079,0,0))
      #
      # right
      #
      self.shape = add(self.shape,translate(pad_XTAL_NX5032GA,.079,0,0))
      self.pad.append(point(.079,0,0))

pad_XTAL_CSM_7 = cube(-.108,.108,-.039,.039,0,0)

class XTAL_CSM_7(part):
   #
   # ECS CSM-7 series
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # left
      #
      self.shape = translate(pad_XTAL_CSM_7,-.187,0,0)
      self.pad.append(point(-.187,0,0))
      #
      # right
      #
      self.shape = add(self.shape,translate(pad_XTAL_CSM_7,.187,0,0))
      self.pad.append(point(.187,0,0))

#
# diodes, transistors, regulators, sensors
#

class D_1206(part):
   #
   # 1206 diode
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # anode
      #
      self.shape = translate(pad_1206,-.06,0,0)
      self.pad.append(point(-.055,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A'))
      #
      # cathode
      #
      self.shape = add(self.shape,translate(pad_1206,.06,0,0))
      self.pad.append(point(.055,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'C'))

class LED_1206(part):
   #
   # 1206 LED
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # anode
      #
      self.shape = translate(pad_1206,-.06,0,0)
      self.pad.append(point(-.055,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A'))
      #
      # cathode
      #
      self.shape = add(self.shape,translate(pad_1206,.06,0,0))
      self.pad.append(point(.055,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'C'))

pad_RGB = cube(-.02,.02,-.029,.029,0,0)

class LED_RGB(part):
   #
   # CREE CLV1A-FKB
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      dx = .029
      dy = .059
      #
      # pin 1: red
      #
      self.shape = translate(pad_RGB,-dx,-dy,0)
      self.shape = add(self.shape,cylinder(-dx,-dy-.029,0,0,.02))
      self.pad.append(point(-dx,-dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'R'))
      #
      # pin 2: anode
      #
      self.shape = add(self.shape,translate(pad_RGB,dx,-dy,0))
      self.pad.append(point(dx,-dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A'))
      #
      # pin 3: blue
      #
      self.shape = add(self.shape,translate(pad_RGB,dx,dy,0))
      self.pad.append(point(dx,dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'B'))
      #
      # pin 4: green
      #
      self.shape = add(self.shape,translate(pad_RGB,-dx,dy,0))
      self.pad.append(point(-dx,dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))

class phototransistor_1206(part):
   #
   # 1206 phototransistor
   # OPTEK 520,521
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # collector
      #
      self.shape = translate(pad_1206,-.06,0,0)
      self.pad.append(point(-.055,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'C'))
      #
      # emitter
      #
      self.shape = add(self.shape,translate(pad_1206,.06,0,0))
      self.pad.append(point(.055,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'E'))

pad_PLCC2 = cube(-.029,.029,-.059,.059,0,0)

class phototransistor_PLCC2(part):
   #
   # PLCC2 phototransistor
   # Optek OP580
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # collector
      #
      self.shape = translate(pad_PLCC2,-.065,0,0)
      self.pad.append(point(-.065,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'C'))
      #
      # emitter
      #
      self.shape = add(self.shape,translate(pad_PLCC2,.065,0,0))
      self.pad.append(point(.065,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'E'))

pad_SOD_123 = cube(-.02,.02,-.024,.024,0,0)

class D_SOD_123(part):
   #
   # SOD-123 diode
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # anode
      #
      self.shape = translate(pad_SOD_123,-.07,0,0)
      self.pad.append(point(-.07,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A'))
      #
      # cathode
      #
      self.shape = add(self.shape,translate(pad_SOD_123,.07,0,0))
      self.pad.append(point(.07,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'C'))

pad_SOT23 = cube(-.02,.02,-.012,.012,0,0)

class NMOSFET_SOT23(part):
   #
   # Fairchild NDS355AN
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: gate
      #
      self.shape = translate(pad_SOT23,.045,-.0375,0)
      self.pad.append(point(.045,-.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 2: source
      #
      self.shape = add(self.shape,translate(pad_SOT23,.045,.0375,0))
      self.pad.append(point(.045,.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'S'))
      #
      # pin 3: drain
      #
      self.shape = add(self.shape,translate(pad_SOT23,-.045,0,0))
      self.pad.append(point(-.045,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'D'))

class PMOSFET_SOT23(part):
   #
   # Fairchild NDS356AP
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: gate
      #
      self.shape = translate(pad_SOT23,.045,-.0375,0)
      self.pad.append(point(.045,-.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 2: source
      #
      self.shape = add(self.shape,translate(pad_SOT23,.045,.0375,0))
      self.pad.append(point(.045,.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'S'))
      #
      # pin 3: drain
      #
      self.shape = add(self.shape,translate(pad_SOT23,-.045,0,0))
      self.pad.append(point(-.045,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'D'))

class NMOSFET_TO252AA(part):
   #
   # Fairchild RFD16N05LSM
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: gate
      #
      self.shape = translate(cube(-.031,.031,-.059,.059,0,0),-.090,0,0)
      self.pad.append(point(-.090,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G 1'))
      #
      # pin 2: source
      #
      self.shape = add(self.shape,translate(cube(-.031,.031,-.059,.059,0,0),.090,0,0))
      self.pad.append(point(.090,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'S'))
      #
      # pin 3: drain
      #
      self.shape = add(self.shape,translate(cube(-.132,.132,-.132,.132,0,0),0,.261,0))
      self.pad.append(point(0,.261,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'D'))

class Hall_SOT23(part):
   #
   # Allegro A1324
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: output
      #
      self.shape = translate(pad_SOT23,-.045,.0375,0)
      self.pad.append(point(-.045,.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Vcc'))
      #
      # pin 2: input
      #
      self.shape = add(self.shape,translate(pad_SOT23,-.045,-.0375,0))
      self.pad.append(point(-.045,-.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'out'))
      #
      # pin 3: ground
      #
      self.shape = add(self.shape,translate(pad_SOT23,.045,0,0))
      self.pad.append(point(.045,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'gnd'))

class regulator_SOT23(part):
   #
   # TI LM3480IM3
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: output
      #
      self.shape = translate(pad_SOT23,-.045,.0375,0)
      self.pad.append(point(-.045,.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'out'))
      #
      # pin 2: input
      #
      self.shape = add(self.shape,translate(pad_SOT23,-.045,-.0375,0))
      self.pad.append(point(-.045,-.0375,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'in'))
      #
      # pin 3: ground
      #
      self.shape = add(self.shape,translate(pad_SOT23,.045,0,0))
      self.pad.append(point(.045,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'gnd'))

class regulator_SOT223(part):
   #
   # Zetex ZLDO1117
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      pad_SOT223 = cube(-.02,.02,-.03,.03,0,0)
      pad_SOT223_ground = cube(-.065,.065,-.03,.03,0,0)
      #
      # pin 1: GND
      #
      self.shape = translate(pad_SOT223,-.09,-.12,0)
      self.pad.append(point(-.09,-.12,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1G'))
      #
      # pin 2: output
      #
      self.shape = add(self.shape,translate(pad_SOT223,0,-.12,0))
      self.pad.append(point(0,-.12,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'O'))
      #
      # pin 3: input
      #
      self.shape = add(self.shape,translate(pad_SOT223,.09,-.12,0))
      self.pad.append(point(.09,-.12,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'I'))
      #
      # pin 4: output
      #
      self.shape = add(self.shape,translate(pad_SOT223_ground,0,.12,0))
      self.pad.append(point(0,.12,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'out'))

class A4953_SOICN(part):
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_SOIC,-.11,.075,0)
      self.shape = add(self.shape,cylinder(-.153,.075,0,0,.015))
      self.pad.append(point(-.11,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2: IN2
      #
      self.shape = add(self.shape,translate(pad_SOIC,-.11,.025,0))
      self.pad.append(point(-.11,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IN2'))
      #
      # pin 3: IN1
      #
      self.shape = add(self.shape,translate(pad_SOIC,-.11,-.025,0))
      self.pad.append(point(-.11,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IN1'))
      #
      # pin 4: VREF
      #
      self.shape = add(self.shape,translate(pad_SOIC,-.11,-.075,0))
      self.pad.append(point(-.11,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VREF'))
      #
      # pin 5: VBB
      #
      self.shape = add(self.shape,translate(pad_SOIC,.11,-.075,0))
      self.pad.append(point(.11,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VBB'))
      #
      # pin 6: OUT1
      #
      self.shape = add(self.shape,translate(pad_SOIC,.11,-.025,0))
      self.pad.append(point(.11,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'OUT1'))
      #
      # pin 7: LSS
      #
      self.shape = add(self.shape,translate(pad_SOIC,.11,.025,0))
      self.pad.append(point(.11,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'LSS'))
      #
      # pin 8: OUT2
      #
      self.shape = add(self.shape,translate(pad_SOIC,.11,.075,0))
      self.pad.append(point(.11,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'OUT2'))
      #
      # thermal pad
      #
      self.shape = add(self.shape,rectangle(-.04,.04,-.075,.075))

pad_SM8 = cube(-.035,.035,-.016,.016,0,0)

class H_bridge_SM8(part):
   #
   # Zetex ZXMHC3A01T8
   #
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      d = .13
      #
      # pin 1: G3 (right N gate)
      #
      self.shape = translate(pad_SM8,-d,.09,0)
      self.shape = add(self.shape,cylinder(-d-.035,.09,0,0,.016))
      self.pad.append(point(-d,.09,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GRN'))
      #
      # pin 2: S2 S3 (N source)
      #
      self.shape = add(self.shape,translate(pad_SM8,-d,.03,0))
      self.pad.append(point(-d,.03,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SN'))
      #
      # pin 3: G2 (left N gate)
      #
      self.shape = add(self.shape,translate(pad_SM8,-d,-.03,0))
      self.pad.append(point(-d,-.03,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GLN'))
      #
      # pin 4: G1 (left P gate)
      #
      self.shape = add(self.shape,translate(pad_SM8,-d,-.09,0))
      self.pad.append(point(-d,-.09,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GLP'))
      #
      # pin 5: D1 D2 (left drain)
      #
      self.shape = add(self.shape,translate(pad_SM8,d,-.09,0))
      self.pad.append(point(d,-.09,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DL'))
      #
      # pin 6: S1 S4 (P source)
      #
      self.shape = add(self.shape,translate(pad_SM8,d,-.03,0))
      self.pad.append(point(d,-.03,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SP'))
      #
      # pin 7: D3 D4 (right drain)
      #
      self.shape = add(self.shape,translate(pad_SM8,d,.03,0))
      self.pad.append(point(d,.03,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DR'))
      #
      # pin 8: G4 (right N gate)
      #
      self.shape = add(self.shape,translate(pad_SM8,d,.09,0))
      self.pad.append(point(d,.09,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GRP'))

pad_mic = cylinder(0,0,0,0,.02)

class mic_SPU0414HR5H(part):
   #
   # Knowles SPU0414HR5H-SB
   #
   def __init__(self,value=''):
      s = 0.004
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: Vdd
      #
      self.shape = translate(pad_mic,.033,.048,0)
      self.pad.append(point(.033,.048,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V1',line=s))
      #
      # pin 2: GND
      #
      self.shape = add(self.shape,translate(pad_mic,.033,-.048,0))
      self.pad.append(point(.033,-.048,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 3: gain
      #
      self.shape = add(self.shape,translate(pad_mic,-.033,-.048,0))
      self.pad.append(point(-.033,-.048,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'gain',line=s))
      #
      # pin 4: out
      #
      self.shape = add(self.shape,translate(pad_mic,-.033,.048,0))
      self.pad.append(point(-.033,.048,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'out',line=s))

class mic_SPM1437(part):
   #
   # Knowles SPM1437HM4H-B
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_mic,-.046,.065,0)
      #self.shape = add(self.shape,cylinder(-.183,.075,0,0,.015))
      self.pad.append(point(-.046,.065,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_mic,-.046,0,0))
      self.pad.append(point(-.046,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SEL'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_mic,-.046,-.065,0))
      self.pad.append(point(-.046,-.065,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_mic,.046,-.065,0))
      self.pad.append(point(.046,-.065,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLK'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_mic,.046,0,0))
      self.pad.append(point(.046,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DAT'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_mic,.046,.065,0))
      self.shape = add(self.shape,translate(pad_mic,.038,.057,0))
      self.pad.append(point(.046,.065,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))

pad_accel = cube(-.03,.03,-.0125,.0125,0,0)
pad_accel90 = cube(-.0125,.0125,-.03,.03,0,0)

class accel_MXD6235M(part):
   #
   # MEMSIC MXD6235M
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_accel,-.1,.05,0)
      self.shape = add(self.shape,cylinder(-.13,.05,0,0,.0125))
      self.pad.append(point(-.1,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_accel,-.1,0,0))
      self.pad.append(point(-.1,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TP'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_accel,-.1,-.05,0))
      self.pad.append(point(-.1,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'G'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_accel90,0,-.1,0))
      self.pad.append(point(0,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_accel,.1,-.05,0))
      self.pad.append(point(.1,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_accel,.1,0,0))
      self.pad.append(point(.1,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Y'))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(pad_accel,.1,.05,0))
      self.pad.append(point(.1,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'X'))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(pad_accel90,0,.1,0))
      self.pad.append(point(0,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V'))
      #
      # ground plane
      #
      self.shape = add(self.shape,cube(-.05,.05,-.05,.05,0,0))

pad_cc_14_1 = cube(-.014,.014,-.0075,.0075,0,0)
pad_cc_14_1_90 = cube(-.0075,.0075,-.014,.014,0,0)

class ADXL343(part):
   #
   # ADI ADXL343 accelerometer
   #
   def __init__(self,value=''):
      d = 0.8/25.4
      w = 1.01/25.4
      s = 0.004
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1
      #
      self.shape = translate(pad_cc_14_1,-w,2.5*d,0)
      self.pad.append(point(-w,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,"VD1",line=s))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,-w,1.5*d,0))
      self.pad.append(point(-w,1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,-w,.5*d,0))
      self.pad.append(point(-w,.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RSV',line=s))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,-w,-.5*d,0))
      self.pad.append(point(-w,-.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,-w,-1.5*d,0))
      self.pad.append(point(-w,-1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,-w,-2.5*d,0))
      self.pad.append(point(-w,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VS',line=s))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(pad_cc_14_1_90,0,-2.5*d,0))
      self.pad.append(point(0,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'-CS',angle=90,line=s))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,w,-2.5*d,0))
      self.pad.append(point(w,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'INT1',line=s))
      #
      # pin 9
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,w,-1.5*d,0))
      self.pad.append(point(w,-1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'INT2',line=s))
      #
      # pin 10
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,w,-.5*d,0))
      self.pad.append(point(w,-.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'NC',line=s))
      #
      # pin 11
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,w,.5*d,0))
      self.pad.append(point(w,.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RSV',line=s))
      #
      # pin 12
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,w,1.5*d,0))
      self.pad.append(point(w,1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'ALT',line=s))
      #
      # pin 13
      #
      self.shape = add(self.shape,translate(pad_cc_14_1,w,2.5*d,0))
      self.pad.append(point(w,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDA',line=s))
      #
      # pin 14
      #
      self.shape = add(self.shape,translate(pad_cc_14_1_90,0,2.5*d,0))
      self.pad.append(point(0,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCL',angle=90,line=s))

#
# ICs
#

class ATtiny1614(part):
   #
   # SOIC
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 0.11
      w = 0.015
      h = .03
      pad = cube(-h,h,-w,w,0,0)
      #
      # pin 1
      #
      self.shape = translate(pad,-d,.15,0)
      self.shape = add(self.shape,cylinder(-d-h,.15,0,0,w))
      self.pad.append(point(-d,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1VCC'))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad,-d,.1,0))
      self.pad.append(point(-d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA4'))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad,-d,.050,0))
      self.pad.append(point(-d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA5'))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad,-d,0,0))
      self.pad.append(point(-d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA6'))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad,-d,-.05,0))
      self.pad.append(point(-d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA7'))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad,-d,-.1,0))
      self.pad.append(point(-d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RB3'))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(pad,-d,-.15,0))
      self.pad.append(point(-d,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TB2'))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(pad,d,-.15,0))
      self.pad.append(point(d,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB1'))
      #
      # pin 9
      #
      self.shape = add(self.shape,translate(pad,d,-.1,0))
      self.pad.append(point(d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB0'))
      #
      # pin 10
      #
      self.shape = add(self.shape,translate(pad,d,-.05,0))
      self.pad.append(point(d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'UPDI'))
      #
      # pin 11
      #
      self.shape = add(self.shape,translate(pad,d,0,0))
      self.pad.append(point(d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA1'))
      #
      # pin 12
      #
      self.shape = add(self.shape,translate(pad,d,.050,0))
      self.pad.append(point(d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA2'))
      #
      # pin 13
      #
      self.shape = add(self.shape,translate(pad,d,.1,0))
      self.pad.append(point(d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA3'))
      #
      # pin 14
      self.shape = add(self.shape,translate(pad,d,.15,0))
      self.pad.append(point(d,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class FT230XS(part):
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 0.11
      w = 0.0053
      h = .03
      p = .65/25.4
      l = 0.004
      pad = cube(-h,h,-w,w,0,0)
      #
      # pin 1
      #
      self.shape = translate(pad,-d,3.5*p,0)
      self.shape = add(self.shape,cylinder(-d-h,3.5*p,0,0,w))
      self.pad.append(point(-d,3.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1TXD',line=l))
      #
      # pin 2
      #
      self.shape = add(self.shape,translate(pad,-d,2.5*p,0))
      self.pad.append(point(-d,2.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RTS',line=l))
      #
      # pin 3
      #
      self.shape = add(self.shape,translate(pad,-d,1.5*p,0))
      self.pad.append(point(-d,1.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VIO',line=l))
      #
      # pin 4
      #
      self.shape = add(self.shape,translate(pad,-d,.5*p,0))
      self.pad.append(point(-d,.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RXD',line=l))
      #
      # pin 5
      #
      self.shape = add(self.shape,translate(pad,-d,-.5*p,0))
      self.pad.append(point(-d,-.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=l))
      #
      # pin 6
      #
      self.shape = add(self.shape,translate(pad,-d,-1.5*p,0))
      self.pad.append(point(-d,-1.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CTS',line=l))
      #
      # pin 7
      #
      self.shape = add(self.shape,translate(pad,-d,-2.5*p,0))
      self.pad.append(point(-d,-2.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CB2',line=l))
      #
      # pin 8
      #
      self.shape = add(self.shape,translate(pad,-d,-3.5*p,0))
      self.pad.append(point(-d,-3.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'USP',line=l))
      #
      # pin 9
      #
      self.shape = add(self.shape,translate(pad,d,-3.5*p,0))
      self.pad.append(point(d,-3.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'USM',line=l))
      #
      # pin 10
      #
      self.shape = add(self.shape,translate(pad,d,-2.5*p,0))
      self.pad.append(point(d,-2.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'3V3',line=l))
      #
      # pin 11
      #
      self.shape = add(self.shape,translate(pad,d,-1.5*p,0))
      self.pad.append(point(d,-1.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST',line=l))
      #
      # pin 12
      #
      self.shape = add(self.shape,translate(pad,d,-.5*p,0))
      self.pad.append(point(d,-.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC',line=l))
      #
      # pin 13
      #
      self.shape = add(self.shape,translate(pad,d,.5*p,0))
      self.pad.append(point(d,.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=l))
      #
      # pin 14
      self.shape = add(self.shape,translate(pad,d,1.5*p,0))
      self.pad.append(point(d,1.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CB1',line=l))
      #
      # pin 15
      #
      self.shape = add(self.shape,translate(pad,d,2.5*p,0))
      self.pad.append(point(d,2.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CB0',line=l))
      #
      # pin 16
      self.shape = add(self.shape,translate(pad,d,3.5*p,0))
      self.pad.append(point(d,3.5*p,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CB3',line=l))


class ATtiny412(part):
   #
   # SOIC150
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 0.11
      w = 0.015
      h = .03
      pad = cube(-h,h,-w,w,0,0)
      #
      # pin 1: VCC
      #
      self.shape = translate(pad,-d,.075,0)
      self.shape = add(self.shape,cylinder(-d-h,.075,0,0,w))
      self.pad.append(point(-d,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 2: PA6
      #
      self.shape = add(self.shape,translate(pad,-d,.025,0))
      self.pad.append(point(-d,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA6'))
      #
      # pin 3: PA7
      #
      self.shape = add(self.shape,translate(pad,-d,-.025,0))
      self.pad.append(point(-d,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA7'))
      #
      # pin 4: PA1
      #
      self.shape = add(self.shape,translate(pad,-d,-.075,0))
      self.pad.append(point(-d,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA1'))
      #
      # pin 5: PA2
      #
      self.shape = add(self.shape,translate(pad,d,-.075,0))
      self.pad.append(point(d,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA2'))
      #
      # pin 6: UPDI
      #
      self.shape = add(self.shape,translate(pad,d,-.025,0))
      self.pad.append(point(d,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'UPDI'))
      #
      # pin 7: PA3
      #
      self.shape = add(self.shape,translate(pad,d,.025,0))
      self.pad.append(point(d,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA3'))
      #
      # pin 8: GND
      #
      self.shape = add(self.shape,translate(pad,d,.075,0))
      self.pad.append(point(d,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

class SAMD11C(part):
   #
   # SOIC
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 0.11
      w = 0.015
      h = .03
      pad = cube(-h,h,-w,w,0,0)
      #
      # pin 1: PA05
      #
      self.shape = translate(pad,-d,.15,0)
      self.shape = add(self.shape,cylinder(-d-h,.15,0,0,w))
      self.pad.append(point(-d,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1A05'))
      #
      # pin 2: PA08
      #
      self.shape = add(self.shape,translate(pad,-d,.1,0))
      self.pad.append(point(-d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A08'))
      #
      # pin 3: PA09
      #
      self.shape = add(self.shape,translate(pad,-d,.050,0))
      self.pad.append(point(-d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A09'))
      #
      # pin 4: PA14
      #
      self.shape = add(self.shape,translate(pad,-d,0,0))
      self.pad.append(point(-d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A14'))
      #
      # pin 5: PA15
      #
      self.shape = add(self.shape,translate(pad,-d,-.05,0))
      self.pad.append(point(-d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A15'))
      #
      # pin 6: nRESET
      #
      self.shape = add(self.shape,translate(pad,-d,-.1,0))
      self.pad.append(point(-d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST'))
      #
      # pin 7: CLK
      #
      self.shape = add(self.shape,translate(pad,-d,-.15,0))
      self.pad.append(point(-d,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLK'))
      #
      # pin 8: DIO
      #
      self.shape = add(self.shape,translate(pad,d,-.15,0))
      self.pad.append(point(d,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DIO'))
      #
      # pin 9: PA24/D-
      #
      self.shape = add(self.shape,translate(pad,d,-.1,0))
      self.pad.append(point(d,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'24-'))
      #
      # pin 10: PA25/D+
      #
      self.shape = add(self.shape,translate(pad,d,-.05,0))
      self.pad.append(point(d,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'25+'))
      #
      # pin 11: GND
      #
      self.shape = add(self.shape,translate(pad,d,0,0))
      self.pad.append(point(d,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 12: VDD
      #
      self.shape = add(self.shape,translate(pad,d,.050,0))
      self.pad.append(point(d,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VDD'))
      #
      # pin 13: PA02
      #
      self.shape = add(self.shape,translate(pad,d,.1,0))
      self.pad.append(point(d,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A02'))
      #
      # pin 14: PA04
      self.shape = add(self.shape,translate(pad,d,.15,0))
      self.pad.append(point(d,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A04'))

pad_SOT23_5 = cube(-.01,.01,-.02,.02,0,0)

class op_amp_SOT23_5(part):
   def __init__(self,value=''):
      self.value = value
      self.x = 0
      self.y = 0
      self.z = 0
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: output
      #
      self.shape = translate(pad_SOT23_5,-.0375,-.045,0)
      self.pad.append(point(-.0375,-.045,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'O'))
      #
      # pin 2: V-
      #
      self.shape = add(self.shape,translate(pad_SOT23_5,0,-.045,0))
      self.pad.append(point(0,-.045,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V-'))
      #
      # pin 3: I+
      #
      self.shape = add(self.shape,translate(pad_SOT23_5,.0375,-.045,0))
      self.pad.append(point(.0375,-.045,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'I+'))
      #
      # pin 4: I-
      #
      self.shape = add(self.shape,translate(pad_SOT23_5,.0375,.045,0))
      self.pad.append(point(.0375,.045,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'I-'))
      #
      # pin 5: V+
      #
      self.shape = add(self.shape,translate(pad_SOT23_5,-.0375,.045,0))
      self.pad.append(point(-.0375,.045,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V+'))

pad_SOICN = cube(-.035,.035,-.015,.015,0,0)

class op_amp_SOICN(part):
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: A out
      #
      self.shape = translate(pad_SOICN,-.12,.075,0)
      self.pad.append(point(-.12,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1 Ao'))
      #
      # pin 2: A-
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,.025,0))
      self.pad.append(point(-.12,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A-'))
      #
      # pin 3: A+
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,-.025,0))
      self.pad.append(point(-.12,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'A+'))
      #
      # pin 4: V-
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,-.075,0))
      self.pad.append(point(-.12,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V-'))
      #
      # pin 5: B+
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,-.075,0))
      self.pad.append(point(.12,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'B+'))
      #
      # pin 6: B-
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,-.025,0))
      self.pad.append(point(.12,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'B-'))
      #
      # pin 7: B out
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,.025,0))
      self.pad.append(point(.12,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Bo'))
      #
      # pin 8: V+
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,.075,0))
      self.pad.append(point(.12,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'V+'))

TSSOP_pad_width = 0.040
TSSOP_pad_height = 0.011
TSSOP_pad_dy = 0.026
TSSOP_pad_dx = 0.120
pad_TSSOP = cube(-TSSOP_pad_width/2.0,TSSOP_pad_width/2.0,-TSSOP_pad_height/2.0,TSSOP_pad_height/2.0,0,0)

class TRC102(part):
   #
   # RFM TRC102 ISM transceiver
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: SDI
      #
      self.shape = translate(pad_TSSOP,-TSSOP_pad_dx,3.5*TSSOP_pad_dy,0)
      self.pad.append(point(-TSSOP_pad_dx,3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1 SDI'))
      #
      # pin 2: SCK
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK'))
      #
      # pin 3: nCS
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'nCS'))
      #
      # pin 4: SDO
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDO'))
      #
      # pin 5: IRQ
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IRQ'))
      #
      # pin 6: DATA/nFSEL
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DATA'))
      #
      # pin 7: CR
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CR'))
      #
      # pin 8: CLKOUT
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLKOUT'))
      #
      # pin 9: Xtal/Ref
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Xtal'))
      #
      # pin 10: RESET
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RESET'))
      #
      # pin 11: GND
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 12: RF_P
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RF_P'))
      #
      # pin 13: RF_N
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RF_N'))
      #
      # pin 14: VDD
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VDD'))
      #
      # pin 15: RSSIA
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RSSIA'))
      #
      # pin 16: nINT/DDET
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,3.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'nINT'))

pad_SOIC = cube(-.041,.041,-.015,.015,0,0)

class ATtiny45_SOIC(part):
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: PB5/dW/ADC0/-RESET/PCINT5
      #
      self.shape = translate(pad_SOIC,-.14,.075,0)
      self.shape = add(self.shape,cylinder(-.183,.075,0,0,.015))
      self.pad.append(point(-.14,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST'))
      #
      # pin 2: PB3/ADC3/-OC1B/CLKI/XTAL1/PCINT3
      #
      self.shape = add(self.shape,translate(pad_SOIC,-.14,.025,0))
      self.pad.append(point(-.14,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB3'))
      #
      # pin 3: PB4/ADC2/OC1B/CLKO/XTAL2/PCINT4
      #
      self.shape = add(self.shape,translate(pad_SOIC,-.14,-.025,0))
      self.pad.append(point(-.14,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB4'))
      #
      # pin 4: GND
      #
      self.shape = add(self.shape,translate(pad_SOIC,-.14,-.075,0))
      self.pad.append(point(-.14,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 5: PB0/MOSI/DI/SDA/AIN0/OC0A/-OC1A/AREF/PCINT0
      #
      self.shape = add(self.shape,translate(pad_SOIC,.14,-.075,0))
      self.pad.append(point(.14,-.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB0'))
      #
      # pin 6: PB1/MISO/DO/AIN1/OC0B/OC1A/PCINT1
      #
      self.shape = add(self.shape,translate(pad_SOIC,.14,-.025,0))
      self.pad.append(point(.14,-.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB1'))
      #
      # pin 7: PB2/SCK/USCK/SCL/ADC1/T0/INT0/PCINT2
      #
      self.shape = add(self.shape,translate(pad_SOIC,.14,.025,0))
      self.pad.append(point(.14,.025,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB2'))
      #
      # pin 8: VCC
      #
      self.shape = add(self.shape,translate(pad_SOIC,.14,.075,0))
      self.pad.append(point(.14,.075,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))

class ATtiny44_SOICN(part):
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: VCC
      #
      self.shape = translate(pad_SOICN,-.12,.15,0)
      self.shape = add(self.shape,cylinder(-.155,.15,0,0,.015))
      self.pad.append(point(-.12,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 2: PB0/XTAL1/PCINT8
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,.1,0))
      self.pad.append(point(-.12,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB0'))
      #
      # pin 3: PB1/XTAL2/PCINT9
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,.050,0))
      self.pad.append(point(-.12,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB1'))
      #
      # pin 4: PB3/dW/-RESET/PCINT11
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,0,0))
      self.pad.append(point(-.12,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB3'))
      #
      # pin 5: PB2/CKOUT/OC0A/INT0/PCINT10
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,-.05,0))
      self.pad.append(point(-.12,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB2'))
      #
      # pin 6: PA7/ADC7/OC0B/ICP/PCINT7
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,-.1,0))
      self.pad.append(point(-.12,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA7'))
      #
      # pin 7: PA6/ADC6/MOSI/SDA/OC1A/PCINT6
      #
      self.shape = add(self.shape,translate(pad_SOICN,-.12,-.15,0))
      self.pad.append(point(-.12,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA6'))
      #
      # pin 8: PA5/ADC5/DO/MISO/OC1B/PCINT5
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,-.15,0))
      self.pad.append(point(.12,-.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA5'))
      #
      # pin 9: PA4/ADC4/USCK/SCL/T1/PCINT4
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,-.1,0))
      self.pad.append(point(.12,-.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA4'))
      #
      # pin 10: PA3/ADC3/T0/PCINT3
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,-.05,0))
      self.pad.append(point(.12,-.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA3'))
      #
      # pin 11: PA2/ADC2/AIN1/PCINT2
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,0,0))
      self.pad.append(point(.12,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA2'))
      #
      # pin 12: PA1/ADC1/AIN0/PCINT1
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,.050,0))
      self.pad.append(point(.12,.05,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA1'))
      #
      # pin 13: PA0/ADC0/AREF/PCINT0
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,.1,0))
      self.pad.append(point(.12,.1,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA0'))
      #
      # pin 14: GND
      #
      self.shape = add(self.shape,translate(pad_SOICN,.12,.15,0))
      self.pad.append(point(.12,.15,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))

pad_TQFP_h = cube(-.025,.025,-.007,.007,0,0)
pad_TQFP_v = cube(-.007,.007,-.025,.025,0,0)

class ATxmegaE5_TQFP(part):
   def __init__(self,value=''):
      c = .18
      d = 0.8/25.4
      s = 0.004
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: GND
      #
      self.shape = translate(pad_TQFP_h,-c,3.5*d,0)
      self.pad.append(point(-c,3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1 GND',line=s))
      #
      # pin 2: PA4
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,2.5*d,0))
      self.pad.append(point(-c,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA4',line=s))
      #
      # pin 3: PA3
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,1.5*d,0))
      self.pad.append(point(-c,1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA3',line=s))
      #
      # pin 4: PA2
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,.5*d,0))
      self.pad.append(point(-c,.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA2',line=s))
      #
      # pin 5: PA1
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-.5*d,0))
      self.pad.append(point(-c,-.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA1',line=s))
      #
      # pin 6: PA0
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-1.5*d,0))
      self.pad.append(point(-c,-1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA0',line=s))
      #
      # pin 7: PDI/DATA
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-2.5*d,0))
      self.pad.append(point(-c,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PDI/DATA',line=s))
      #
      # pin 8: RST/CLOCK
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-3.5*d,0))
      self.pad.append(point(-c,-3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RST/CLOCK',line=s))
      #
      # pin 9: PC7
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-3.5*d,-c,0))
      self.pad.append(point(-3.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC7',angle=90,line=s))
      #
      # pin 10: PC6
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-2.5*d,-c,0))
      self.pad.append(point(-2.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC6',angle=90,line=s))
      #
      # pin 11: PC5
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-1.5*d,-c,0))
      self.pad.append(point(-1.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC5',angle=90,line=s))
      #
      # pin 12: PC4
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-.5*d,-c,0))
      self.pad.append(point(-.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC4',angle=90,line=s))
      #
      # pin 13: PC3
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,.5*d,-c,0))
      self.pad.append(point(.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC3',angle=90,line=s))
      #
      # pin 14: PC2
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,1.5*d,-c,0))
      self.pad.append(point(1.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC2',angle=90,line=s))
      #
      # pin 15: PC1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,2.5*d,-c,0))
      self.pad.append(point(2.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC1',angle=90,line=s))
      #
      # pin 16: PC0
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,3.5*d,-c,0))
      self.pad.append(point(3.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC0',angle=90,line=s))
      #
      # pin 17: VCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-3.5*d,0))
      self.pad.append(point(c,-3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC',line=s))
      #
      # pin 18: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-2.5*d,0))
      self.pad.append(point(c,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 19: PR1
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-1.5*d,0))
      self.pad.append(point(c,-1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PR1',line=s))
      #
      # pin 20: PR0
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-.5*d,0))
      self.pad.append(point(c,-.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PR0',line=s))
      #
      # pin 21: PD7
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,.5*d,0))
      self.pad.append(point(c,.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD7',line=s))
      #
      # pin 22: PD6
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,1.5*d,0))
      self.pad.append(point(c,1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD6',line=s))
      #
      # pin 23: PD5
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,2.5*d,0))
      self.pad.append(point(c,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD5',line=s))
      #
      # pin 24: PD4
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,3.5*d,0))
      self.pad.append(point(c,3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD4',line=s))
      #
      # pin 25: PD3
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,3.5*d,c,0))
      self.pad.append(point(3.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD3',angle=90,line=s))
      #
      # pin 26: PD2
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,2.5*d,c,0))
      self.pad.append(point(2.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD2',angle=90,line=s))
      #
      # pin 27: PD1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,1.5*d,c,0))
      self.pad.append(point(1.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD1',angle=90,line=s))
      #
      # pin 28: PD0
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,.5*d,c,0))
      self.pad.append(point(.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD0',angle=90,line=s))
      #
      # pin 29: PA7
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-.5*d,c,0))
      self.pad.append(point(-.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA7',angle=90,line=s))
      #
      # pin 30: PA6
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-1.5*d,c,0))
      self.pad.append(point(-1.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA6',angle=90,line=s))
      #
      # pin 31: PA5
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-2.5*d,c,0))
      self.pad.append(point(-2.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA5',angle=90,line=s))
      #
      # pin 32: AVCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-3.5*d,c,0))
      self.pad.append(point(-3.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'AVCC',angle=90,line=s))

class ATmega88_TQFP(part):
   def __init__(self,value=''):
      c = .18
      d = .031
      s = 0.004
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: PD3/PCINT19/OC2B/INT1
      #
      self.shape = translate(pad_TQFP_h,-c,3.5*d,0)
      self.pad.append(point(-c,3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1 PD3',line=s))
      #
      # pin 2: PD4/PCINT20/XCK/T0
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,2.5*d,0))
      self.pad.append(point(-c,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD4',line=s))
      #
      # pin 3: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,1.5*d,0))
      self.pad.append(point(-c,1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 4: VCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,.5*d,0))
      self.pad.append(point(-c,.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC',line=s))
      #
      # pin 5: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-.5*d,0))
      self.pad.append(point(-c,-.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 6: VCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-1.5*d,0))
      self.pad.append(point(-c,-1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC',line=s))
      #
      # pin 7: PB6/PCINT6/XTAL1/TOSC1
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-2.5*d,0))
      self.pad.append(point(-c,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB6',line=s))
      #
      # pin 8: PB7/PCINT7/XTAL2/TOSC2
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-3.5*d,0))
      self.pad.append(point(-c,-3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB7',line=s))
      #
      # pin 9: PD5/PCINT21/OC0B/T1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-3.5*d,-c,0))
      self.pad.append(point(-3.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD5',angle=90,line=s))
      #
      # pin 10: PD6/PCINT22/OC0A/AIN0
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-2.5*d,-c,0))
      self.pad.append(point(-2.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD6',angle=90,line=s))
      #
      # pin 11: PD7/PCINT23/AIN1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-1.5*d,-c,0))
      self.pad.append(point(-1.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD7',angle=90,line=s))
      #
      # pin 12: PB0/PCINT0/CLKO/ICP1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-.5*d,-c,0))
      self.pad.append(point(-.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB0',angle=90,line=s))
      #
      # pin 13: PB1/PCINT1/OC1A
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,.5*d,-c,0))
      self.pad.append(point(.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB1',angle=90,line=s))
      #
      # pin 14: PB2/PCINT2/-SS/OC1B
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,1.5*d,-c,0))
      self.pad.append(point(1.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB2',angle=90,line=s))
      #
      # pin 15: PB3/PCINT3/OC2A/MOSI
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,2.5*d,-c,0))
      self.pad.append(point(2.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB3',angle=90,line=s))
      #
      # pin 16: PB4/PCINT4/MISO
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,3.5*d,-c,0))
      self.pad.append(point(3.5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB4',angle=90,line=s))
      #
      # pin 17: PB5/SCK/PCINT5
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-3.5*d,0))
      self.pad.append(point(c,-3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB5',line=s))
      #
      # pin 18: AVCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-2.5*d,0))
      self.pad.append(point(c,-2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'AVCC',line=s))
      #
      # pin 19: ADC6
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-1.5*d,0))
      self.pad.append(point(c,-1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'ADC6',line=s))
      #
      # pin 20: AREF
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-.5*d,0))
      self.pad.append(point(c,-.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'AREF',line=s))
      #
      # pin 21: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,.5*d,0))
      self.pad.append(point(c,.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND',line=s))
      #
      # pin 22: ADC7
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,1.5*d,0))
      self.pad.append(point(c,1.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'ADC7',line=s))
      #
      # pin 23: PC0/ADC0/PCINT8
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,2.5*d,0))
      self.pad.append(point(c,2.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC0',line=s))
      #
      # pin 24: PC1/ADC1/PCINT9
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,3.5*d,0))
      self.pad.append(point(c,3.5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC1',line=s))
      #
      # pin 25: PC2/ADC2/PCINT10
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,3.5*d,c,0))
      self.pad.append(point(3.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC2',angle=90,line=s))
      #
      # pin 26: PC3/ADC3/PCINT11
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,2.5*d,c,0))
      self.pad.append(point(2.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC3',angle=90,line=s))
      #
      # pin 27: PC4/ADC4/SDA/PCINT12
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,1.5*d,c,0))
      self.pad.append(point(1.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC4',angle=90,line=s))
      #
      # pin 28: PC5/ADC5/SCL/PCINT13
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,.5*d,c,0))
      self.pad.append(point(.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC5',angle=90,line=s))
      #
      # pin 29: PC6/-RESET/PCINT14
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-.5*d,c,0))
      self.pad.append(point(-.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC6',angle=90,line=s))
      #
      # pin 30: PD0/RXD/PCINT16
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-1.5*d,c,0))
      self.pad.append(point(-1.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD0',angle=90,line=s))
      #
      # pin 31: PD1/TXD/PCINT17
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-2.5*d,c,0))
      self.pad.append(point(-2.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD1',angle=90,line=s))
      #
      # pin 32: PD2/INT0/PCINT18
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-3.5*d,c,0))
      self.pad.append(point(-3.5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD2',angle=90,line=s))

class ATmega644_TQFP(part):
   def __init__(self,value=''):
      c = .235
      d = .031
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: PB5/PCINT13/MOSI
      #
      self.shape = translate(pad_TQFP_h,-c,5*d,0)
      self.pad.append(point(-c,5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'*MOSI (1)'))
      #
      # pin 2: PB6/PCINT14/MISO
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,4*d,0))
      self.pad.append(point(-c,4*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'MISO'))
      #
      # pin 3: PB7/PCINT15/SCK
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,3*d,0))
      self.pad.append(point(-c,3*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK'))
      #
      # pin 4: -RESET
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,2*d,0))
      self.pad.append(point(-c,2*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'-RESET'))
      #
      # pin 5: VCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,d,0))
      self.pad.append(point(-c,d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 6: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,0,0))
      self.pad.append(point(-c,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 7: XTAL2
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-d,0))
      self.pad.append(point(-c,-d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'XTAL2'))
      #
      # pin 8: XTAL1
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-2*d,0))
      self.pad.append(point(-c,-2*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'XTAL1'))
      #
      # pin 9: PD0/PCINT24/RXD0
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-3*d,0))
      self.pad.append(point(-c,-3*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RXD0'))
      #
      # pin 10: PD1/PCINT25/TXD0
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-4*d,0))
      self.pad.append(point(-c,-4*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'TXD0'))
      #
      # pin 11: PD2/PCINT26/INT0
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,-c,-5*d,0))
      self.pad.append(point(-c,-5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD2'))
      #
      # pin 12: PD3/PCINT27/INT1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-5*d,-c,0))
      self.pad.append(point(-5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD3'))
      #
      # pin 13: PD4/PCINT28/OC1B
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-4*d,-c,0))
      self.pad.append(point(-4*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD4'))
      #
      # pin 14: PD5/PCINT28/OC1A
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-3*d,-c,0))
      self.pad.append(point(-3*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD5'))
      #
      # pin 15: PD6/PCINT30/OC2B/ICP
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-2*d,-c,0))
      self.pad.append(point(-2*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD6'))
      #
      # pin 16: PD7/PCINT31/OC2A
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-d,-c,0))
      self.pad.append(point(-d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PD7'))
      #
      # pin 17: VCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,0,-c,0))
      self.pad.append(point(0,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 18: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,d,-c,0))
      self.pad.append(point(d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 19: PC0/PCINT16/SCL
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,2*d,-c,0))
      self.pad.append(point(2*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC0'))
      #
      # pin 20: PC1/PCINT17/SDA
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,3*d,-c,0))
      self.pad.append(point(3*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC1'))
      #
      # pin 21: PC2/PCINT18/TCK
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,4*d,-c,0))
      self.pad.append(point(4*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC2'))
      #
      # pin 22: PC3/PCINT19/TMS
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,5*d,-c,0))
      self.pad.append(point(5*d,-c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC3'))
      #
      # pin 23: PC4/TDO/PCINT20
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-5*d,0))
      self.pad.append(point(c,-5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC4'))
      #
      # pin 24: PC5/TDI/PCINT21
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-4*d,0))
      self.pad.append(point(c,-4*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC5'))
      #
      # pin 25: PC6/TOSC1/PCINT22
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-3*d,0))
      self.pad.append(point(c,-3*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC6'))
      #
      # pin 26: PC7/TOSC2/PCINT23
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-2*d,0))
      self.pad.append(point(c,-2*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PC7'))
      #
      # pin 27: AVCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,-d,0))
      self.pad.append(point(c,-d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'AVCC'))
      #
      # pin 28: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,0,0))
      self.pad.append(point(c,0,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 29: AREF
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,d,0))
      self.pad.append(point(c,d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'AREF'))
      #
      # pin 30: PA7/ADC7/PCINT7
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,2*d,0))
      self.pad.append(point(c,2*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA7'))
      #
      # pin 31: PA6/ADC6/PCINT6
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,3*d,0))
      self.pad.append(point(c,3*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA6'))
      #
      # pin 32: PA5/ADC5/PCINT5
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,4*d,0))
      self.pad.append(point(c,4*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA5'))
      #
      # pin 33: PA4/ADC4/PCINT4
      #
      self.shape = add(self.shape,translate(pad_TQFP_h,c,5*d,0))
      self.pad.append(point(c,5*d,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA4'))
      #
      # pin 34: PA3/ADC3/PCINT3
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,5*d,c,0))
      self.pad.append(point(5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA3'))
      #
      # pin 35: PA2/ADC2/PCINT2
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,4*d,c,0))
      self.pad.append(point(4*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA2'))
      #
      # pin 36: PA1/ADC1/PCINT1
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,3*d,c,0))
      self.pad.append(point(3*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA1'))
      #
      # pin 37: PA0/ADC0/PCINT0
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,2*d,c,0))
      self.pad.append(point(2*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PA0'))
      #
      # pin 38: VCC
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,d,c,0))
      self.pad.append(point(d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VCC'))
      #
      # pin 39: GND
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,0,c,0))
      self.pad.append(point(0,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 40: PB0/XCK0/T0/PCINT8
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-d,c,0))
      self.pad.append(point(-d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB0'))
      #
      # pin 41: PB1/T1/CLKO/PCINT9
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-2*d,c,0))
      self.pad.append(point(-2*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB1'))
      #
      # pin 42: PB2/AIN0/INT2/PCINT10
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-3*d,c,0))
      self.pad.append(point(-3*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB2'))
      #
      # pin 43: PB3/AIN1/OC0A/PCINT11
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-4*d,c,0))
      self.pad.append(point(-4*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB2'))
      #
      # pin 44: PB4/-SS/OC0B/PCINT12
      #
      self.shape = add(self.shape,translate(pad_TQFP_v,-5*d,c,0))
      self.pad.append(point(-5*d,c,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'PB4'))

TSSOP_pad_width = 0.040
TSSOP_pad_height = 0.011
TSSOP_pad_dy = 0.026
TSSOP_pad_dx = 0.120
pad_TSSOP = cube(-TSSOP_pad_width/2.0,TSSOP_pad_width/2.0,-TSSOP_pad_height/2.0,TSSOP_pad_height/2.0,0,0)

class TRC102(part):
   #
   # RFM TRC102 ISM transceiver
   #
   def __init__(self,value=''):
      self.value = value
      self.pad = [point(0,0,0)]
      self.labels = []
      #
      # pin 1: SDI
      #
      self.shape = translate(pad_TSSOP,-TSSOP_pad_dx,3.5*TSSOP_pad_dy,0)
      self.pad.append(point(-TSSOP_pad_dx,3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'1 SDI'))
      #
      # pin 2: SCK
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SCK'))
      #
      # pin 3: nCS
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'nCS'))
      #
      # pin 4: SDO
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'SDO'))
      #
      # pin 5: IRQ
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'IRQ'))
      #
      # pin 6: DATA/nFSEL
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'DATA'))
      #
      # pin 7: CR
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CR'))
      #
      # pin 8: CLKOUT
      #
      self.shape = add(self.shape,translate(pad_TSSOP,-TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.pad.append(point(-TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'CLKOUT'))
      #
      # pin 9: Xtal/Ref
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'Xtal'))
      #
      # pin 10: RESET
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RESET'))
      #
      # pin 11: GND
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'GND'))
      #
      # pin 12: RF_P
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,-0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RF_P'))
      #
      # pin 13: RF_N
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,0.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RF_N'))
      #
      # pin 14: VDD
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,1.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'VDD'))
      #
      # pin 15: RSSIA
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,2.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'RSSIA'))
      #
      # pin 16: nINT/DDET
      #
      self.shape = add(self.shape,translate(pad_TSSOP,TSSOP_pad_dx,3.5*TSSOP_pad_dy,0))
      self.pad.append(point(TSSOP_pad_dx,3.5*TSSOP_pad_dy,0))
      self.labels.append(self.text(self.pad[-1].x,self.pad[-1].y,self.pad[-1].z,'nINT'))

class CBA(part):
   #
   # CBA logo
   #
   def __init__(self,r=.02):
      self.value = ''
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 3*r
      self.shape = cylinder(0,0,0,0,r)
      self.shape = add(self.shape,translate(cylinder(0,0,0,0,r),-d,d,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),-d,0,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),-d,-d,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),0,-d,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),d,-d,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),d,0,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),d,d,0))
      self.shape = add(self.shape,translate(cube(-r,r,-r,r,0,0),0,d,0))

class fab(part):
   def __init__(self,r=.05):
      self.value = ''
      self.pad = [point(0,0,0)]
      self.labels = []
      d = 1.8*r
      l = 3.5*r
      h = r/2.
      self.shape = rectangle(-d,d,-d,d)
      self.shape = subtract(self.shape,circle(0,0,r))
      self.shape = subtract(self.shape,rectangle(-l,0,-h,h))
      self.shape = add(self.shape,rectangle(d,l,-h,h))
      self.shape = add(self.shape,circle(l,0,r))
      self.shape = add(self.shape,circle(-l,0,r))

#
# define board
#

width = .68 # board width
height = .82 # board height
x = 1 # x origin
y = 1 # y origin
zt = 0 # top z
zb = -0.06 # bottom z
w = .015 # wire width
mask = .004 # solder mask size

pcb = PCB(x,y,width,height,mask)

IC1 = ATtiny1614('IC1\nt1614')
pcb = IC1.add(pcb,x+.21,y+.5)

C1 = C_1206('C1 1uF')
pcb = C1.add(pcb,IC1.x,IC1.pad[1].y+.08)

pcb = wire(pcb,w,
   C1.pad[1],
   point(IC1.pad[1].x,C1.y),
   IC1.pad[1])

J1 = header_FTDI('J1\nFTDI')
pcb = J1.add(pcb,x+width-.23,IC1.y-.05)

pcb = wire(pcb,w,
   J1.pad[1],
   point(IC1.pad[14].x,J1.pad[1].y),
   point(IC1.pad[14].x,C1.y),
   C1.pad[2])

pcb = wire(pcb,w,
   J1.pad[1],
   point(IC1.pad[14].x,J1.pad[1].y),
   IC1.pad[14])

pcb = wire(pcb,w,
   J1.pad[3],
   point(J1.x+.1,J1.pad[3].y),
   point(J1.x+.1,C1.y+.06),
   point(C1.pad[1].x,C1.y+.06),
   C1.pad[1])

J2 = header_UPDI('J2 UPDI')
pcb = J2.add(pcb,IC1.x,y+.23,angle=90)

pcb = wire(pcb,w,
   J2.pad[1],
   point(IC1.x+.02,J2.pad[1].y+.08),
   point(IC1.x+.02,IC1.pad[10].y),
   IC1.pad[10])

pcb = wire(pcb,w,
   J2.pad[2],
   point(IC1.x-.02,J2.pad[2].y+.08),
   point(IC1.x-.02,IC1.pad[14].y),
   IC1.pad[14])

pcb = wire(pcb,w,
   IC1.pad[7],
   point(IC1.pad[7].x,J2.y-.1),
   point(IC1.pad[14].x,J2.y-.1),
   point(IC1.pad[14].x,J1.pad[5].y),
   J1.pad[5])

pcb = wire(pcb,w,
   IC1.pad[6],
   point(IC1.pad[6].x-.07,IC1.pad[6].y),
   point(IC1.pad[6].x-.07,J2.y-.13),
   point(J1.x+.1,J2.y-.13),
   point(J1.x+.1,J1.pad[4].y),
   J1.pad[4])

#
# select output
#

outputs = {}
if (output == "top, labels, and exterior"):
   outputs["function"] = add(add(color(Tan,pcb.board),pcb.labels),
      color(White,pcb.exterior))
   outputs["layers"] = [zt]
elif (output == "top, labels, holes, and exterior"):
   outputs["function"] = add(add(color(Tan,pcb.board),pcb.labels),
      color(White,add(pcb.exterior,pcb.holes)))
   outputs["layers"] = [zt]
elif (output == "top, bottom, labels, and exterior"):
   outputs["function"] = add(add(color(Tan,pcb.board),pcb.labels),
      color(White,pcb.exterior))
   outputs["layers"] = [zb,zt]
elif (output == "top, bottom, labels, holes, and exterior"):
   outputs["function"] = add(add(color(Tan,
      subtract(pcb.board,pcb.holes)),pcb.labels),
      color(White,pcb.exterior))
   outputs["layers"] = [zb,zt]
elif (output == "top traces"):
   outputs["function"] = color(White,pcb.board)
   outputs["layers"] = [zt]
elif (output == "top traces and exterior"):
   outputs["function"] = color(White,add(pcb.board,pcb.exterior))
   outputs["layers"] = [zt]
elif (output == "top traces, holes, and exterior"):
   outputs["function"] = color(White,
      add(add(pcb.board,pcb.exterior),pcb.holes))
   outputs["layers"] = [zt]
elif (output == "bottom traces reversed"):
   outputs["function"] = color(White,
      reflect_x(pcb.board,2*x+width))
   outputs["layers"] = [zb]
elif (output == "bottom traces reversed and exterior"):
   outputs["function"] = color(White,
      reflect_x(add(pcb.board,pcb.exterior),2*x+width))
   outputs["layers"] = [zb]
elif (output == "interior"):
   outputs["function"] = color(White,pcb.interior)
   outputs["layers"] = [zt]
elif (output == "exterior"):
   outputs["function"] = color(White,pcb.exterior)
   outputs["layers"] = [zt]
elif (output == "holes"):
   outputs["function"] = color(White,
      subtract(add(pcb.exterior,pcb.interior),pcb.holes))
   outputs["layers"] = [zb]
elif (output == "holes and interior"):
   outputs["function"] = color(White,
      subtract(pcb.interior,pcb.holes))
   outputs["layers"] = [zb]
elif (output == "solder mask"):
   outputs["function"] = color(White,pcb.mask)
   outputs["layers"] = [zt]
else:
   print("oops -- don't recognize output")

#
# set limits and parameters
#

border = 0.05
outputs["xmin"] = x-border # min x to render
outputs["xmax"] = x+width+border # max x to render
outputs["ymin"] = y-border # min y to render
outputs["ymax"] = y+height+border # max y to render
outputs["mm_per_unit"] = 25.4 # use inch units
outputs["type"] = "RGB" # use RGB color

#
# send output
#

json.dump(outputs,sys.stdout)
