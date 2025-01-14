import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
#plt.rcParams['animation.ffmpeg_path'] = 'D:/portableSoftware/ShareX/ShareX/Tools/ffmpeg.exe'

interval = 50 # ms, time between animation frames

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.35)

ax.set_aspect('equal')
plt.xlim(-1.4*40,1.4*40)
plt.ylim(-1.4*40,1.4*40)
#plt.grid()
t = np.linspace(0, 2*np.pi, 2000)
delta = 1
e =2
n=10
RD=40
rd=5
#plt.grid()
## draw pin
l0, = ax.plot([], [], 'r-')
l1, = ax.plot([], [], 'r-')
l2, = ax.plot([], [], 'r-')
l3, = ax.plot([], [], 'r-')        
l4, = ax.plot([], [], 'r-')
l5, = ax.plot([], [], 'r-')
l6, = ax.plot([], [], 'r-')
l7, = ax.plot([], [], 'r-') 
l8, = ax.plot([], [], 'r-')
l9, = ax.plot([], [], 'r-')
l10, = ax.plot([], [], 'r-') 
l11, = ax.plot([], [], 'r-')
l12, = ax.plot([], [], 'r-')
l13, = ax.plot([], [], 'r-')        
l14, = ax.plot([], [], 'r-')
l15, = ax.plot([], [], 'r-')
l16, = ax.plot([], [], 'r-')
l17, = ax.plot([], [], 'r-') 
l18, = ax.plot([], [], 'r-')
l19, = ax.plot([], [], 'r-')
l20, = ax.plot([], [], 'r-') 
l21, = ax.plot([], [], 'r-')
l22, = ax.plot([], [], 'r-')
l23, = ax.plot([], [], 'r-')        
l24, = ax.plot([], [], 'r-')
l25, = ax.plot([], [], 'r-')
l26, = ax.plot([], [], 'r-')
l27, = ax.plot([], [], 'r-') 
l28, = ax.plot([], [], 'r-')
l29, = ax.plot([], [], 'r-')
l30, = ax.plot([], [], 'r-') 
l31, = ax.plot([], [], 'r-')
l32, = ax.plot([], [], 'r-')
l33, = ax.plot([], [], 'r-')        
l34, = ax.plot([], [], 'r-')
l35, = ax.plot([], [], 'r-')
l36, = ax.plot([], [], 'r-')
l37, = ax.plot([], [], 'r-') 
l38, = ax.plot([], [], 'r-')
l39, = ax.plot([], [], 'r-')
l40, = ax.plot([], [], 'r-') 


for i in range(int(10)):
    x = (5*np.sin(t)+ 40*np.cos(2*i*np.pi/10))
    y = (5*np.cos(t) + 40*np.sin(2*i*np.pi/10))
    if i == 0:
        l0, = ax.plot(x, y,'r-')
    if i == 1:
        l1, = ax.plot(x, y,'r-')
    if i == 2:
        l2, = ax.plot(x, y,'r-')
    if i == 3:
        l3, = ax.plot(x, y,'r-')        
    if i == 4:
        l4, = ax.plot(x, y,'r-')
    if i == 5:
        l5, = ax.plot(x, y,'r-')
    if i == 6:
        l6, = ax.plot(x, y,'r-')
    if i == 7:
        l7, = ax.plot(x, y,'r-')  
    if i == 8:
        l8, = ax.plot(x, y,'r-')
    if i == 9:
        l9, = ax.plot(x, y,'r-')
    if i == 10:
        l10, = ax.plot(x, y,'r-') 
    if i == 11:
        l11, = ax.plot(x, y,'r-')
    if i == 12:
        l12, = ax.plot(x, y,'r-')
    if i == 13:
        l13, = ax.plot(x, y,'r-')        
    if i == 14:
        l14, = ax.plot(x, y,'r-')
    if i == 15:
        l15, = ax.plot(x, y,'r-')
    if i == 16:
        l16, = ax.plot(x, y,'r-')
    if i == 17:
        l17, = ax.plot(x, y,'r-')  
    if i == 18:
        l18, = ax.plot(x, y,'r-')
    if i == 19:
        l19, = ax.plot(x, y,'r-')
    if i == 20:
        l20, = ax.plot(x, y,'r-')
    if i == 21:
        l21, = ax.plot(x, y,'r-')
    if i == 22:
        l22, = ax.plot(x, y,'r-')
    if i == 23:
        l23, = ax.plot(x, y,'r-')        
    if i == 24:
        l24, = ax.plot(x, y,'r-')
    if i == 25:
        l25, = ax.plot(x, y,'r-')
    if i == 26:
        l26, = ax.plot(x, y,'r-')
    if i == 27:
        l27, = ax.plot(x, y,'r-')  
    if i == 28:
        l28, = ax.plot(x, y,'r-')
    if i == 29:
        l29, = ax.plot(x, y,'r-')
    if i == 30:
        l30, = ax.plot(x, y,'r-') 
    if i == 31:
        l31, = ax.plot(x, y,'r-')
    if i == 32:
        l32, = ax.plot(x, y,'r-')
    if i == 33:
        l33, = ax.plot(x, y,'r-')        
    if i == 34:
        l34, = ax.plot(x, y,'r-')
    if i == 35:
        l35, = ax.plot(x, y,'r-')
    if i == 36:
        l36, = ax.plot(x, y,'r-')
    if i == 37:
        l37, = ax.plot(x, y,'r-')  
    if i == 38:
        l38, = ax.plot(x, y,'r-')
    if i == 39:
        l39, = ax.plot(x, y,'r-')
    if i == 40:
        l40, = ax.plot(x, y,'r-')

def draw_pin_init():
    l0.set_data([0], [0])
    l1.set_data([0], [0])
    l2.set_data([0], [0])  
    l3.set_data([0], [0])
    l4.set_data([0], [0])
    l5.set_data([0], [0])
    l6.set_data([0], [0])
    l7.set_data([0], [0])
    l8.set_data([0], [0])
    l9.set_data([0], [0])
    l10.set_data([0], [0])
    l11.set_data([0], [0])
    l12.set_data([0], [0])  
    l13.set_data([0], [0])
    l14.set_data([0], [0])
    l15.set_data([0], [0])
    l16.set_data([0], [0])
    l17.set_data([0], [0])
    l18.set_data([0], [0])
    l19.set_data([0], [0])
    l20.set_data([0], [0])
    l21.set_data([0], [0])
    l22.set_data([0], [0])  
    l23.set_data([0], [0])
    l24.set_data([0], [0])
    l25.set_data([0], [0])
    l26.set_data([0], [0])
    l27.set_data([0], [0])
    l28.set_data([0], [0])
    l29.set_data([0], [0])
    l30.set_data([0], [0])
    l31.set_data([0], [0])
    l32.set_data([0], [0])  
    l33.set_data([0], [0])
    l34.set_data([0], [0])
    l35.set_data([0], [0])
    l36.set_data([0], [0])
    l37.set_data([0], [0])
    l38.set_data([0], [0])
    l39.set_data([0], [0])
    l40.set_data([0], [0])  

def draw_inner_pin_init():
    p0.set_data([0], [0])
    p1.set_data([0], [0])
    p2.set_data([0], [0])  
    p3.set_data([0], [0])
    p4.set_data([0], [0])
    p5.set_data([0], [0])
    p6.set_data([0], [0])
    p7.set_data([0], [0])
    p8.set_data([0], [0])
    p9.set_data([0], [0])

def pin_update(n,d,D,phis):
    for i in range(int(n)):    
        xa = (d/2*np.sin(t)+ D/2*np.cos(2*i*np.pi/n))
        ya = (d/2*np.cos(t) + D/2*np.sin(2*i*np.pi/n))

        #x = xa*np.cos(-phi/(n)+np.pi/(n)) - ya * np.sin(-phi/(n)+np.pi/(n))  + e*np.cos(phi)
        #y = xa*np.sin(-phi/(n)+np.pi/(n)) + ya * np.cos(-phi/(n)+np.pi/(n))  + e*np.cos(phi)

        x = (xa )*np.cos(-phis/(n)+np.pi/(n))-(ya )*np.sin(-phis/(n)+np.pi/(n))  + e*np.cos(phis)
        y = (xa )*np.sin(-phis/(n)+np.pi/(n))+(ya )*np.cos(-phis/(n)+np.pi/(n))  + e*np.sin(phis)

        if i == 0:
            l0.set_data(x,y)
        if i == 1:
            l1.set_data(x,y)
        if i == 2:
            l2.set_data(x,y)
        if i == 3:
            l3.set_data(x,y)        
        if i == 4:
            l4.set_data(x,y)
        if i == 5:
            l5.set_data(x,y)
        if i == 6:
            l6.set_data(x,y)
        if i == 7:
            l7.set_data(x,y)  
        if i == 8:
            l8.set_data(x,y)
        if i == 9:
            l9.set_data(x,y)
        if i == 10:
            l10.set_data(x,y)
        if i == 11:
            l11.set_data(x,y)
        if i == 12:
            l12.set_data(x,y)           
        if i == 13:
            l13.set_data(x,y)        
        if i == 14:
            l14.set_data(x,y)
        if i == 15:
            l15.set_data(x,y)
        if i == 16:
            l16.set_data(x,y)
        if i == 17:
            l17.set_data(x,y)
        if i == 18:
            l18.set_data(x,y)
        if i == 19:
            l19.set_data(x,y)
        if i == 20:
            l20.set_data(x,y)
        if i == 21:
            l21.set_data(x,y)
        if i == 22:
            l22.set_data(x,y)
        if i == 23:
            l23.set_data(x,y)        
        if i == 24:
            l24.set_data(x,y)
        if i == 25:
            l25.set_data(x,y)
        if i == 26:
            l26.set_data(x,y)
        if i == 27:
            l27.set_data(x,y)  
        if i == 28:
            l28.set_data(x,y)
        if i == 29:
            l29.set_data(x,y)
        if i == 30:
            l30.set_data(x,y)
        if i == 31:
            l31.set_data(x,y)
        if i == 32:
            l32.set_data(x,y)           
        if i == 133:
            l33.set_data(x,y)        
        if i == 34:
            l34.set_data(x,y)
        if i == 35:
            l35.set_data(x,y)
        if i == 36:
            l36.set_data(x,y)
        if i == 37:
            l37.set_data(x,y)
        if i == 38:
            l38.set_data(x,y)
        if i == 39:
            l39.set_data(x,y)
        if i == 40:
            l40.set_data(x,y)


## draw inner_pin
p0, = ax.plot([], [], 'y-')
p1, = ax.plot([], [], 'y-')
p2, = ax.plot([], [], 'y-')
p3, = ax.plot([], [], 'y-')        
p4, = ax.plot([], [], 'y-')
p5, = ax.plot([], [], 'y-')
p6, = ax.plot([], [], 'y-')
p7, = ax.plot([], [], 'y-') 
p8, = ax.plot([], [], 'y-')
p9, = ax.plot([], [], 'y-')


for i in range(int(6)):
    x = (5*np.sin(t)+ 20*np.cos(2*i*np.pi/6))
    y = (5*np.cos(t) + 20*np.sin(2*i*np.pi/6))
    if i == 0:
        p0, = ax.plot(x, y,'y-')
    if i == 1:
        p1, = ax.plot(x, y,'y-')
    if i == 2:
        p2, = ax.plot(x, y,'y-')
    if i == 3:
        p3, = ax.plot(x, y,'y-')        
    if i == 4:
        p4, = ax.plot(x, y,'y-')
    if i == 5:
        p5, = ax.plot(x, y,'y-')
    if i == 6:
        p6, = ax.plot(x, y,'y-')
    if i == 7:
        p7, = ax.plot(x, y,'y-')  
    if i == 8:
        p8, = ax.plot(x, y,'y-')
    if i == 9:
        p9, = ax.plot(x, y,'y-')



def inner_pin_update(n,N,rd,Rd,phi):
    for i in range(int(n)):    
        x = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1))
        y = (rd*np.sin(t)+ Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + (rd*np.cos(t) + Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1))
        if i == 0:
            p0.set_data(x,y)
        if i == 1:
            p1.set_data(x,y)
        if i == 2:
            p2.set_data(x,y)
        if i == 3:
            p3.set_data(x,y)        
        if i == 4:
            p4.set_data(x,y)
        if i == 5:
            p5.set_data(x,y)
        if i == 6:
            p6.set_data(x,y)
        if i == 7:
            p7.set_data(x,y)  
        if i == 8:
            p8.set_data(x,y)
        if i == 9:
            p9.set_data(x,y)

## draw drive_pin
a = 5*np.sin(t)
b = 5*np.cos(t) 
d0, = ax.plot(a, b,'k-', lw=2)

def drive_pin_update(r):
    x = r*np.sin(t)
    y = r*np.cos(t)
    d0.set_data(x,y)


#inner circle:
inner_circle1, = ax.plot([], [], 'r-', lw=2)
inner_circle2, = ax.plot([], [], 'r-', lw=2)
inner_circle3, = ax.plot([], [], 'r-', lw=2)
inner_circle4, = ax.plot([], [], 'r-', lw=2)        
inner_circle5, = ax.plot([], [], 'r-', lw=2)
inner_circle6, = ax.plot([], [], 'r-', lw=2)
inner_circle7, = ax.plot([], [], 'r-', lw=2)
inner_circle8, = ax.plot([], [], 'r-', lw=2) 
inner_circle9, = ax.plot([], [], 'r-', lw=2)
inner_circle10, = ax.plot([], [], 'r-', lw=2)

def draw_inner_circle_init():
    inner_circle10.set_data([0], [0])
    inner_circle1.set_data([0], [0])
    inner_circle2.set_data([0], [0])  
    inner_circle3.set_data([0], [0])
    inner_circle4.set_data([0], [0])
    inner_circle5.set_data([0], [0])
    inner_circle6.set_data([0], [0])
    inner_circle7.set_data([0], [0])
    inner_circle8.set_data([0], [0])
    inner_circle9.set_data([0], [0])


for i in range(6):
    x = (rd+e)*np.cos(t)+0.5*RD*np.cos(2*i*np.pi/6)+e
    y = (rd+e)*np.sin(t)+0.5*RD*np.sin(2*i*np.pi/6)
    if i==0:
        inner_circle1, = ax.plot(x,y,'r-')
    if i==1:
        inner_circle2, = ax.plot(x,y,'r-')
    if i==2:
        inner_circle3, = ax.plot(x,y,'r-')
    if i==3:
        inner_circle4, = ax.plot(x,y,'r-')
    if i==4:
        inner_circle5, = ax.plot(x,y,'r-')
    if i==5:
        inner_circle6, = ax.plot(x,y,'r-')
    if i==6:
        inner_circle7, = ax.plot(x,y,'r-')
    if i==7:
        inner_circle8, = ax.plot(x,y,'r-')
    if i==8:
        inner_circle9, = ax.plot(x,y,'r-')
    if i==9:
        inner_circle10, = ax.plot(x,y,'r-')   

def update_inner_circle(e,n,N,rd,Rd, phi):
    
    for i in range(int(n)):
        x = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.cos(-phi/(N-1)) - ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.sin(-phi/(N-1)) + e*np.cos(phi)
        y = ((rd+e)*np.cos(t)+Rd*np.cos(2*i*np.pi/n))*np.sin(-phi/(N-1)) + ((rd+e)*np.sin(t)+Rd*np.sin(2*i*np.pi/n))*np.cos(-phi/(N-1)) + e*np.sin(phi)
        if i==0:
            inner_circle1.set_data(x,y)
        if i==1:
            inner_circle2.set_data(x,y)
        if i==2:
            inner_circle3.set_data(x,y)
        if i==3:
            inner_circle4.set_data(x,y)
        if i==4:
            inner_circle5.set_data(x,y)
        if i==5:
            inner_circle6.set_data(x,y)
        if i==6:
            inner_circle7.set_data(x,y)
        if i==7:
            inner_circle8.set_data(x,y)
        if i==8:
            inner_circle9.set_data(x,y)
        if i==9:
            inner_circle10.set_data(x,y)
 
##inner pinA:
inner_pinA, = ax.plot([0],[0],'r-')
dotA, = ax.plot([0],[0], 'ro', ms=5)

def update_inner_pinA(e,Rm, phi):
    x = (Rm+e)*np.cos(t)+e*np.cos(phi)
    y = (Rm+e)*np.sin(t)+e*np.sin(phi)
    inner_pinA.set_data(x,y)
    
    x1 = (Rm+e)*np.cos(phi)+e*np.cos(phi)
    y1 = (Rm+e)*np.sin(phi)+e*np.sin(phi)
    #self.line.set_data([0,x1],[0,y1])
    dotA.set_data(x1, y1)


##inner pinC:
inner_pinC, = ax.plot([0],[0],'r-.')


def update_inner_pinC(e,D, phi):
    x = (D/2)*np.cos(t)+e*np.cos(phi)
    y = (D/2)*np.sin(t)+e*np.sin(phi)
    inner_pinC.set_data(x,y)






##ehypocycloidD:

ehypocycloidD, = ax.plot([0],[0],'b-')
edotD, = ax.plot([0],[0], 'bo', ms=5)

def update_ehypocycloidD(e,n,D,d, phis):
    RD=D/2
    rd=d/2
    rc = (n+1)*(RD/n)
    rm = (RD/n)
    #xa = (rc-rm)*np.cos(t)+e*np.cos((rc-rm)/rm*t)
    #ya = (rc-rm)*np.sin(t)-e*np.sin((rc-rm)/rm*t)
    #dxa = (rc-rm)*(-np.sin(t)-(e/rm)*np.sin((rc-rm)/rm*t))
    #dya = (rc-rm)*(np.cos(t)-(e/rm)*np.cos((rc-rm)/rm*t))    
    xa = (rc-rm)*np.cos(t)+e*np.cos((n)*t)
    ya = (rc-rm)*np.sin(t)-e*np.sin((n)*t)

    dxa = (rc-rm)*(-np.sin(t)-(e/rm)*np.sin((n)*t))
    dya = (rc-rm)*(np.cos(t)-(e/rm)*np.cos((n)*t))


    x = (xa - (rd)/np.sqrt(dxa**2 + dya**2)*(-dya))*np.cos( np.pi/(n+1)) - (ya - (rd)/np.sqrt(dxa**2 + dya**2)*dxa)*np.sin( np.pi/(n+1)) 
    y = (xa - (rd)/np.sqrt(dxa**2 + dya**2)*(-dya))*np.sin( np.pi/(n+1)) + (ya - (rd)/np.sqrt(dxa**2 + dya**2)*dxa)*np.cos( np.pi/(n+1))


    ehypocycloidD.set_data(x,y)

    #self.eline.set_data([e*np.cos(phis),x[0]],[e*np.sin(phis),y[0]])
    edotD.set_data(x[0], y[0])


##ehypocycloid_Pin1:


ehypocycloid_Pin1, = ax.plot([0],[0],'g-')
edot_Pin1, = ax.plot([0],[0], 'go', ms=5)

def update_ehypocycloid_Pin1(e,n,D,d, phis):

    RD=D/2
    rd=d/2
    rc = (n+1)*(RD/n)
    rm = (RD/n)
    xa = (rc-rm)*np.cos(t)-e*np.cos((n-1)*t)
    ya = (rc-rm)*np.sin(t)+e*np.sin((n-1)*t)

    dxa = (rc-rm)*(-np.sin(t)+(e/rm)*np.sin((n-1)*t))
    dya = (rc-rm)*(np.cos(t)+(e/rm)*np.cos((n-1)*t))

    xa1 = (xa - (rd-e)/np.sqrt(dxa**2 + dya**2)*(-dya))
    ya1 = (ya - (rd-e)/np.sqrt(dxa**2 + dya**2)*dxa)

    x = (xa1 )*np.cos(-phis/(n))-(ya1 )*np.sin(-phis/(n))  + e*np.cos(phis)  #旋转 + 自转
    y = (xa1 )*np.sin(-phis/(n))+(ya1 )*np.cos(-phis/(n))  + e*np.sin(phis)

       
    
    ehypocycloid_Pin1.set_data(x,y)

    #self.eline.set_data([e*np.cos(phis),x[0]],[e*np.sin(phis),y[0]])
    edot_Pin1.set_data(x[0], y[0])



axcolor = 'lightgoldenrodyellow'

ax_fm = plt.axes([0.25, 0.27, 0.5, 0.02], facecolor=axcolor)
ax_Rm = plt.axes([0.25, 0.24, 0.5, 0.02], facecolor=axcolor)
ax_n = plt.axes([0.25, 0.21, 0.5, 0.02], facecolor=axcolor)
ax_Rd = plt.axes([0.25, 0.18, 0.5, 0.02], facecolor=axcolor)
ax_rd = plt.axes([0.25, 0.15, 0.5, 0.02], facecolor=axcolor)
ax_e = plt.axes([0.25, 0.12, 0.5, 0.02], facecolor=axcolor)
ax_N = plt.axes([0.25, 0.09, 0.5, 0.02], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.06, 0.5, 0.02], facecolor=axcolor)
ax_D = plt.axes([0.25, 0.03, 0.5, 0.02], facecolor=axcolor)

sli_fm = Slider(ax_fm, 'fm', 10, 100, valinit=50, valstep=delta)
sli_Rm = Slider(ax_Rm, 'Rm', 1, 10, valinit=5, valstep=delta)
sli_n = Slider(ax_n, 'n', 3, 10, valinit=6, valstep=delta)
sli_Rd = Slider(ax_Rd, 'Rd', 1, 40, valinit=20, valstep=delta)
sli_rd = Slider(ax_rd, 'rd', 1, 10, valinit=5, valstep=delta)
sli_e = Slider(ax_e, 'e', 0.1, 10, valinit=2, valstep=delta/10)
sli_N = Slider(ax_N, 'N', 3, 40, valinit=10, valstep=delta)
sli_d = Slider(ax_d, 'd', 2, 20, valinit=10,valstep=delta)
sli_D = Slider(ax_D, 'D', 5, 100, valinit=80,valstep=delta)

def update(val):
    sfm = sli_Rm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    ax.set_xlim(-1.4*0.5*sD,1.4*0.5*sD)
    ax.set_ylim(-1.4*0.5*sD,1.4*0.5*sD)



sli_fm.on_changed(update)
sli_Rm.on_changed(update)
sli_Rd.on_changed(update)
sli_n.on_changed(update)
sli_rd.on_changed(update)
sli_e.on_changed(update)
sli_N.on_changed(update)
sli_d.on_changed(update)
sli_D.on_changed(update)

resetax = plt.axes([0.85, 0.01, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sli_fm.reset()    
    sli_Rm.reset()
    sli_n.reset()
    sli_rd.reset()
    sli_Rd.reset()    
    sli_e.reset()
    sli_N.reset()
    sli_d.reset()
    sli_D.reset()

button.on_clicked(reset)

def animate(frame):
    sfm = sli_fm.val
    sRm = sli_Rm.val
    sRd = sli_Rd.val
    sn = sli_n.val
    srd = sli_rd.val    
    se = sli_e.val
    sN = sli_N.val
    sd = sli_d.val
    sD = sli_D.val
    frame = frame+1
    phi = 2*np.pi*frame/sfm


    draw_pin_init()
    draw_inner_pin_init()
    draw_inner_circle_init()
    pin_update(sN,sd,sD,phi)
    update_inner_pinA(se,sRm, phi)

    inner_pin_update(sn,sN,srd,sRd,phi)
    drive_pin_update(sRm)
    update_inner_circle(se,sn,sN,srd,sRd, phi)


    update_ehypocycloidD(se,sN,sD,sd, phi)
    update_inner_pinC(se,sD, phi)

    update_ehypocycloid_Pin1(se,sN,sD,sd, phi)
    fig.canvas.draw_idle()



ani = animation.FuncAnimation(fig, animate,frames=sli_fm.val*(sli_N.val-1), interval=interval)
dpi=100
##un-comment the next line, if you want to save the animation as gif:
#hypo.animation.save('myhypocycloid.gif', writer='pillow', fps=10, dpi=75)
#ani.save('myGUI1.mp4', writer="ffmpeg",dpi=dpi)
plt.show()