import numpy as np

size=800000
gy=[]
hy=np.pi/size
ya=-np.pi/2
Iy=0
hx=np.pi/(size*2)
Ix=0;
fxy=[]
xa=-np.pi/4

for i in (range (size)):

	gy.append(np.cos(3*ya/2))
	ya=ya+hy
	fxy.append(np.sin(xa))
	xa=xa+hx
	if i==0 or i==size-1:
		Iy=Iy+gy[i]
		Ix=Ix+fxy[i]
	elif i%2==0:
		Iy=Iy+2*gy[i]
		Ix=Ix+2*fxy[i]
	else:
		Iy=Iy+4*gy[i]
		Ix=Ix+4*fxy[i]

Ix=Ix*(hx/3)
Iy=Iy*(hy/3)*Ix

print (Iy)
