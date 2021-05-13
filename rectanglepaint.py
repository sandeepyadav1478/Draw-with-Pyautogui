import pyautogui as po
import math
x=200
y=150
#po.doubleClick()

try:
  #Creating rectangles loop in paint
  distance=100
  po.moveTo(distance+50,distance/2+y)
  while distance>0:
    po.drag(distance,0,po.easeInQuad(0.2))
    distance-=2
    po.drag(0,distance,po.easeInBounce(0.2))
    po.drag(-distance,0,po.easeInBounce(0.2))
    distance-=2
    po.drag(0,-distance,po.easeInBounce(0.2))


  #creating trinangles loop in paint
  a=po.position()
  po.moveTo(902,57,duration=2)
  po.click()
  po.moveTo(a)
  po.moveTo(2*distance+50+x+50,distance+20+y+100) #just to stop overlap on previous surface
  distance=100
  while distance>0:
    po.drag(distance,0,po.easeInQuad(0.2))
    po.drag(-distance/2,distance,po.easeInOutBounce(0.2))
    po.drag(-(distance/2-4),-(distance-4),duration=0.2)
    distance-=8

  #creating circle in paint
  a=po.position()
  po.moveTo(820,57,duration=2)
  po.click()
  po.moveTo(a)
  po.moveTo(2*distance+300+x+70,distance+25+y+100)   #just to stop overlap on previous surface
  distance=10
  while distance>0:
    i=j=0
    q=distance
    s=q**2
    #q1
    while True:
      if j<q:
        j+=1
      else:
        break
      i=math.sqrt(s-j**2)
      po.drag(i,j)

    #sencond quarter
    j=0
    while True:
      if j<q:
        j+=1
      else:
        break
      i=math.sqrt(s-j**2)
      po.drag(-j,i)

    #third quarter
    j=0
    while True:
      if j<q:
        j+=1
      else:
        break
      i=math.sqrt(s-j**2)
      po.drag(-i,-j,po.easeInOutQuad(0))

    #forth quarter 
    j=0
    while True:
      if j<q:
        j+=1
      else:
        break
      i=math.sqrt(s-j**2)
      po.drag(j,-i,po.easeInOutQuad(0))
    #po.drag(q+1,q+1,po.easeInOutQuad(0.2))
    distance-=1
    po.move(0,distance)
except KeyboardInterrupt:
  print('Interrupted')
  pass