#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig, ax = plt.subplots()

##initialisation
N=3
G=1
P_ini=np.array([[0,1],[2,0],[2,2]])
V_ini=np.array([[0,0],[1,1],[0,-1]])
M=np.array([1,2,3])
dt=1
(P_tp,P_tav)=(V_ini*dt+P_ini,P_ini)

def evol_position(P_tav,P_tp,M,dt,N):
    """
    renvoie l'évolution de P la matrice des positions à l'intant présent
    P_Tav: matrice coordonées passées
    P_tp : matrice coordonées futures
    M: matrice des masses
    dt : pas de temps
    N : nombre de corps
    """
    MG=M*M.reshape(N,1)
    MG=MG[:,:,np.newaxis]
    Diff=P_tp[np.newaxis,:,:]-P_tp[:,np.newaxis,:]
    Dis=np.sqrt(Diff[:,:,0]**2+Diff[:,:,1]**2)
    Dis=Dis[:,:,np.newaxis]
    (P_tp,P_tav)=(G*dt**2*np.sum(np.nan_to_num(Diff*MG/(Dis**3)), axis=0)+2*P_tp-P_tav,P_tp)
    return P_tp,P_tav


def get_new_position(P_tp):
    (P_tp,P_tav)=evol_position(P_tp,P_tav,M,dt,N)
    Xs = P_tp[:,0]
    Ys = P_tp[:,1]
    print(Xs)
    return [Xs, Ys]


scat = ax.scatter(P_tp[0], P_tp[1])


def animate(t):
    # une variable globale est une variable utilisée dans une fonction mais dont la modification de la valeur a une portée globale (donc extérieure à la fonction)

    global P_tp
    global P_tav
    P_tp = get_new_position(P_tp)

    # update the scatter plot:
    # le np.stack sert ici à mettre les positions dans la bonne shape
    data = np.stack(P_tp).T
    scat.set_offsets(data)
    return scat

ani = animation.FuncAnimation(fig=fig, func=animate, interval=100)
plt.show()

