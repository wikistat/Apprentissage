import matplotlib.pyplot as plt
import numpy as np
import itertools
import random

#############
## SIGNAUX ##
#############

def plot_signaux(fig, x, y, signals, color_dic, nb_sample_per_activity, 
                 linestyle_per_activity, linewidth_per_activity, shuffle=False, figdim1 = 1, figdim2 = 1, legend=False):
    index = []
    for k,v in itertools.groupby(sorted(enumerate(y), key=lambda x : x[1]), key=lambda x : x[1]):
        lv = np.array(list(v))
        index.extend(lv[:nb_sample_per_activity[k],0].astype(int))
    index = sorted(index)  
    
    x_range = range(x.shape[1])

    
    data_plot = list(zip(x[index], y[index]))
    if shuffle:
        random.shuffle(data_plot)
    for isignal, signal in enumerate(signals):
        labels=[]
        ax = fig.add_subplot(figdim1, figdim2 ,isignal+1)
        for values,label in data_plot:  
            color = color_dic[label]
            lw = linewidth_per_activity[label]
            ls = linestyle_per_activity[label]
            if label in labels:
                ax.plot(x_range,values[:,isignal], color=color, linewidth=lw, linestyle=ls)
            else:
                ax.plot(x_range,values[:,isignal], color=color, linewidth=lw, linestyle=ls, label = label)
                labels.append(label)
        if legend :
            plt.legend(fontsize=15,ncol=2)
        ax.set_title(signal, fontsize=25)
    plt.tight_layout()
    
    
def plot_signal_per_activity(fig, X, Y, nb_sample, isignal, signals, color_dic):
    index_per_act = {}
    for k,v in itertools.groupby(sorted(enumerate(Y), key=lambda x : x[1]), key=lambda x : x[1]):
        lv = np.array(list(v))
        index_per_act.update({k : lv[:nb_sample,0].astype(int)})
    
    x_range = range(128)
    for i,(act, index) in enumerate(index_per_act.items()):
        ax = fig.add_subplot(3,2,i+1)
        for x in X[index,:,isignal]:
            ax.plot(x_range, x,color=color_dic[act], linewidth=1)
        ax.set_title(act)
    plt.suptitle(signals[isignal])
    plt.tight_layout()


#########
## ACP ##
#########

def plot_variance_acp(fig, acp, X_acp, whis=1.5): 
    ax = fig.add_subplot(1,2,1)
    ax.bar(range(10), acp.explained_variance_ratio_[:10]*100, align='center',
        color='grey', ecolor='black')
    ax.set_xticks(range(10))
    ax.set_ylabel("Variance")
    ax.set_title("", fontsize=35)
    ax.set_title("Percentage of explained variance \n on first components", fontsize=20)

    ax = fig.add_subplot(1,2,2)
    box=ax.boxplot(X_acp[:,0:10], whis=whis)
    ax.set_title("First components distributions", fontsize=20)

def plot_pca(ax, X, acp, nbc, nbc2, colors, markersizes):
    ax.scatter(X[:,nbc-1],X[:,nbc2-1],marker=".", color= colors, s=markersizes)
    ax.set_xlabel("PC%d : %.2f %%" %(nbc,acp.explained_variance_ratio_[nbc-1]*100), fontsize=15)
    ax.set_ylabel("PC%d : %.2f %%" %(nbc2,acp.explained_variance_ratio_[nbc2-1]*100), fontsize=15)

    
def plot_projection_acp(fig, X_acp, acp, colors=None, markersizes=None, color_dic = None):
    ax = fig.add_subplot(1,2,1)
    N = X_acp.shape[0]
    if colors is None:
        colors = ["black"]*N
    if markersizes is None:
        markersizes = [1]*N
    
    plot_pca(ax, X_acp, acp, 1, 2, colors, markersizes)
    ax.set_title("Projections on \n  first two components", fontsize=20)
    ax.set_xlim(X_acp[:,0].min()-5,X_acp[:,0].max()+5)
    ax.set_ylim(X_acp[:,1].min()-1,X_acp[:,1].max()+1)
    
    if not(color_dic is None):
        from matplotlib.lines import Line2D
        legend_elements = [Line2D([0], [0], color=color,marker=".", linestyle=None, markersize=15, label=act)for act, color in color_dic.items()]
        plt.legend(handles=legend_elements, fontsize=12, ncol=2)


    ax = fig.add_subplot(1,2,2)
    for f,(x1, x2) in enumerate(zip(acp.components_[0], acp.components_[1])):
        ax.text(x1,x2,str(f), horizontalalignment="center", verticalalignment="center", color="red")
    ax.set_xlim(acp.components_[0].min()-0.002,acp.components_[0].max()+0.002)
    ax.set_ylim(acp.components_[1].min()-0.01,acp.components_[1].max()+0.01)
    ax.set_title("Projections on \n  first two components", fontsize=20)
    
    
#####################
# Anomaly Detection #
#####################

def plot_decision_function(fig, ax, method, X, y_pred, s=40, method_name="SVM", colors=None, labels=None, markersizes=None):
    N = X.shape[0] 
    if colors==None:
        colors = ["black"]*N
    if labels==None:
        labels = [""]*N
    if markersizes==None:
        markersizes = [1]*N
    
    xx, yy = np.meshgrid(np.linspace(X[:,0].min()-5, X[:,0].max()+5, 500), 
                         np.linspace(X[:,1].min()-1, X[:,1].max()+1, 500))
    
    # plot the line, the points, and the nearest vectors to the plane
    if method_name=="LOF":
        Z = method._decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = method.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    if method_name == "SVM":
        Z_lim = 0
    elif method_name =="LOF":
        Z_lim = method.offset_
    else:
        Z_lim =  method.threshold_
    ax.contourf(xx, yy, Z, levels=[Z.min(), Z_lim, Z.max()], cmap=plt.cm.PuBu)
    
    if method_name!="IF":
        a = ax.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')


    for x1, x2, c, l, ms, yp in zip(X[:,0], X[:,1], colors, labels, markersizes, y_pred):
        marker = "." if yp==1 else "X"
        if l=="":
            ax.plot(x1,x2,marker=marker, color= c, markersize = ms)
        else:
            ax.plot(x1,x2,marker=marker, color=c, label=l, markersize = ms, linestyle = None)


    plt.axis('tight')
    ax.set_xlim(X[:,0].min()-5,X[:,0].max()+5)
    ax.set_ylim(X[:,1].min()-1,X[:,1].max()+1)
    plt.legend()
    

def plot_detection_result(fig, ax, CT, color_dic, s1=70, s2=150, normal_behaviour="WALKING"):
    y_lim = (-1.13,1.13)
    x_lim = [-5,815]
    N = CT.shape[0]
    CT_Normal = CT[CT.Anomaly==normal_behaviour]
    CT_Anormal = CT[CT.Anomaly!=normal_behaviour]
    N_anormal = CT_Anormal.shape[0]
    ax.scatter(CT_Normal.index, -CT_Normal.pred, s = s1, color="white", edgecolors="black", label = "Normal")
    ax.plot(x_lim, [0,0], color="black")

    xticks = []
    xtickslabel = []
    colors = []

    for i,(pred, label) in enumerate(CT_Anormal.values):
        x = int(i/N_anormal*N)
        xticks.append(x)
        xtickslabel.append(label)
        color = color_dic[label]
        colors.append(color)
        ax.plot([x,x] , y_lim, color=color, linestyle="dashed")
        color = "red" if pred==1 else "green"
        ax.scatter(x, -pred, s = s2, color=color, edgecolors="black")

    ax.set_xticks(xticks)
    ax.set_xticklabels(xtickslabel, rotation=45, fontsize=15)
    for xtick, color in zip(ax.get_xticklabels(), colors):
        xtick.set_color(color)
    ax.set_xlim(*x_lim)
    ax.set_ylim(y_lim)

    
###############
## Ondelette ##
###############


def coef_pyramid_plot(ax, coefs, first=0, scale='uniform'):
    n_levels = len(coefs)
    n = 2**(n_levels - 1) # assumes periodic

    if scale == 'uniform':
        biggest = [np.max(np.abs(np.hstack(coefs)))] * n_levels
    else:
        # multiply by 2 so the highest bars only take up .5
        biggest = [np.max(np.abs(i))*2 for i in coefs]

    for i in range(first,n_levels):
        x = np.linspace(2**(n_levels - 2 - i), n - 2**(n_levels - 2 - i), 2**i)
        ymin = n_levels - i - 1 + first
        yheight = coefs[i]/biggest[i]
        ymax = yheight + ymin
        ax.vlines(x, ymin, ymax, linewidth=1.1)

    ax.set_xlim(0,n)
    ax.set_ylim(first - 1, n_levels)
    ax.yaxis.set_ticks(np.arange(n_levels-1,first-1,-1))
    ax.yaxis.set_ticklabels(np.arange(first,n_levels))
    ax.tick_params(top=False, right=False, direction='out', pad=6)
    ax.set_ylabel("Levels", fontsize=14)
    ax.grid(True, alpha=.85, color='white', axis='y', linestyle='-')
    ax.set_title('Wavelet Detail Coefficients', fontsize=16,
            position=(.5,1.05))
    
    
def plot_boxplot_coef_per_signal(X, Y, N_plot_max, labels, activity_dic, color_dic, N_per_activity_train ):
    N_dim = X.shape[1]
    N_dim_plot = min(N_dim, N_plot_max)
    height = 4*N_dim_plot
    fig = plt.figure(figsize=(12,height))
    for i_dim in range(N_dim_plot):
        ax=fig.add_subplot(N_dim_plot,1,i_dim+1)
        X_i = X[:,i_dim]
        for i_act in range(1,7):
            label = activity_dic[i_act]
            color = color_dic[label]
            N_act = N_per_activity_train[i_act]
            X_i_act = X_i[Y==i_act]
            bplot = ax.boxplot(X_i_act, patch_artist=True, positions=[i_act])
            bplot["boxes"][0].set_facecolor(color)
            bplot["medians"][0].set_color("black")
            bplot["medians"][0].set_linewidth(2)
        ax.set_xlim(0.5,6.5)
        ax.set_xticks(range(1,7))
        xticks_label = labels if i_dim==N_dim_plot-1 else ['']*6
        ax.set_xticklabels(xticks_label, rotation=45, fontsize=12)
        
        
        
def plot_boxplot_coef_concat_per_signal(X, Y, labels, activity_dic, color_dic, N_per_activity_train):
    N_level = len(X)
    height = 4*N_level
    fig = plt.figure(figsize=(12,height))
    for i_level in range(N_level):
        ax=fig.add_subplot(N_level,1,i_level+1)
        X_level = X[i_level]
        N_dim = X_level.shape[1]
        for i_act in range(1,7):
            label = activity_dic[i_act]
            color = color_dic[label]
            N_act = N_per_activity_train[i_act]
            X_i_act = X_level[Y==i_act].reshape((N_act*N_dim,1))
            bplot = ax.boxplot(X_i_act, patch_artist=True, positions=[i_act])
            bplot["boxes"][0].set_facecolor(color)
            bplot["medians"][0].set_color("black")
            bplot["medians"][0].set_linewidth(2)
        ax.set_xlim(0.5,6.5)
        ax.set_xticks(range(1,7))
        xticks_label = labels if i_level==N_level-1 else ['']*6
        ax.set_xticklabels(xticks_label, rotation=45, fontsize=12)
        ax.set_title("Level : %d" %i_level)