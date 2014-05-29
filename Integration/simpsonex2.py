import numpy as np
#simpson ex2
size=100000000
fx=[];fz = [];fy = [];
hx=np.pi/(2*size)
hy=np.pi/size
hz=1/size
Ix=0;Iy=0;Iz=0;
xa=-np.pi/4		
ya=-np.pi/2
za=0
for i in (range (size)):	
	fz.append(za)
	za=za+hz
	fx.append(np.sin(xa))
	xa=xa+hx
	fy.append(np.cos(3*ya/2))
	ya=ya+hy
	if i==0 or i==size-1:
		Iz=Iz+fz[i]
		Ix=Ix+fx[i]
		Iy=Iy+fy[i]
	elif i%2==0:
		Iz=Iz+2*fz[i]
		Ix=Ix+2*fx[i]
		Iy=Iy+2*fy[i]
	else:
		Iz=Iz+4*fz[i]
		Ix=Ix+4*fx[i]
		Iy=Iy+4*fy[i]
Ix=Ix*(hx/3)
Iy=Iy*(hy/3)*Ix
Iz=Iz*(hz/3)*Iy
print (Iz)
