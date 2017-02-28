# How to call this - python /works/Research/comparemod.py
import numpy as np
from scipy import stats

def askToContinue(message):
	while True:
		y = 'y';
		n = 'n';
		answer = input('type in (y) to continue, (n) to exit:')
		if answer.lower() == 'y':
			print(message)
			break
		elif answer.lower() == 'n':
			exit()
	

v, I = np.loadtxt("allnewloop09.data",usecols=[8,9],skiprows=5,unpack=True)

dm = 13.43

a= 0.13
a2 = 0.08

v=v+dm+0.12-0.04+a
I=I+dm+0.07+ a2
#13.43-DISTANCE MODULUS
#0.12/0.07 REDDENING FACTOR

vmi = v-I

vd, vmid = np.loadtxt("NGC0104R.RDVIQ.cal.adj.zpt",usecols=[3,5],skiprows=3,unpack=True)

import matplotlib.pyplot as plt

plt.xlim(-4,6)

plt.ylim(30,5)

plt.xlabel('Colour (V-I)')
plt.ylabel('Mag (V)')


plt.scatter(vmid,vd,s=1)
plt.scatter(vmi,v,color='red',s=1)

plt.show()

#*********************************************************************

askToContinue("To Clump/HGB")


import matplotlib.path as mplPath
bbPath = mplPath.Path(np.array([
                     (0.7337, 14.0346),
                     (0.8112, 13.1427),
                     (0.6395, 12.9587),
                     (0.5704, 13.8081),
                     (0.6604, 14.1621)]))

Keep = bbPath.contains_points(np.transpose([vmi, v]))
vmi_bump=vmi[Keep]
v_bump=v[Keep]

#condense?
Keep = bbPath.contains_points(np.transpose([vmid, vd]))
vmid_bump=vmid[Keep]
vd_bump=vd[Keep]

plt.xlabel('Colour (V-I)')
plt.ylabel('Mag (V)')


plt.scatter(vmid_bump,vd_bump)
plt.scatter(vmi_bump,v_bump,color='red')


plt.show()

vgs=-np.sort(-v_bump)
vgsd=-np.sort(-vd_bump)

plt.plot(vgs,(np.arange(len(vgs))+1.0)/len(vgs))
plt.plot(vgsd,(np.arange(len(vgsd))+1.0)/len(vgsd))

plt.xlabel('magnitude (V)')
plt.ylabel('star count')

plt.show()

#8888888888888888888888888888888888888888888888888888888888888888888


print(stats.ks_2samp(vgs, vgsd))

#88888888888888888888888888888888888888888888888888888888888888888888

askToContinue("To AGB")

#---------------------------AGB---------------------------------

bbPath = mplPath.Path(np.array([
                     (1.0954, 11.7346),
                     (0.9588, 12.2954),
                     (0.8696, 12.8256),
                     (0.8013, 13.3864),
                     (0.7593, 13.4986),
                     (-0.0177, 13.4986),
                     (0.5178, 11.0820)]))

Keep = bbPath.contains_points(np.transpose([vmi, v]))
vmi_bump=vmi[Keep]
v_bump=v[Keep]

Keep = bbPath.contains_points(np.transpose([vmid, vd]))
vmid_bump=vmid[Keep]
vd_bump=vd[Keep]


plt.scatter(vmid_bump,vd_bump)
plt.scatter(vmi_bump,v_bump,color='red')

plt.xlabel('Colour (V-I)')
plt.ylabel('Mag (V)')

plt.show()

#Keep = mag[bbPath.contains_points(np.array([vmi, v]) np.transpose([colour, mag])]

vgs=-np.sort(-v_bump)
vgsd=-np.sort(-vd_bump)

plt.plot(vgs,(np.arange(len(vgs))+1.0)/len(vgs))
plt.plot(vgsd,(np.arange(len(vgsd))+1.0)/len(vgsd))

plt.xlabel('magnitude (V)')
plt.ylabel('star count')

plt.show()

print(stats.ks_2samp(vgs, vgsd))


askToContinue("To RGB")

#-----------------------------RGB------------------------------------

bbPath = mplPath.Path(np.array([
                     (1.0942, 11.7873),
                     (0.8760, 12.7932),
                     (0.7488, 13.8383),
                     (0.6351, 15.5758),
                     (0.5897, 16.0592),
                     (1.7896, 16.3335),
                     (1.6669, 11.9832),
                     (1.1033, 11.6566)]))

Keep = bbPath.contains_points(np.transpose([vmi, v]))
vmi_bump=vmi[Keep]
v_bump=v[Keep]

Keep = bbPath.contains_points(np.transpose([vmid, vd]))
vmid_bump=vmid[Keep]
vd_bump=vd[Keep]


plt.scatter(vmid_bump,vd_bump)
plt.scatter(vmi_bump,v_bump,color='red')


plt.xlabel('Colour (V-I)')
plt.ylabel('Mag (V)')

plt.show()

#Keep = mag[bbPath.contains_points(np.array([vmi, v]) np.transpose([colour, mag])]

vgs=-np.sort(-v_bump)
vgsd=-np.sort(-vd_bump)

plt.plot(vgs,(np.arange(len(vgs))+1.0)/len(vgs))
plt.plot(vgsd,(np.arange(len(vgsd))+1.0)/len(vgsd))

plt.xlabel('magnitude (V)')
plt.ylabel('star count')

plt.show()

print(stats.ks_2samp(vgs, vgsd))







	
