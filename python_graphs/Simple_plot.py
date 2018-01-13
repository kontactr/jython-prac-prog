import matplotlib.pyplot as plt


def get_para():
    x , y = [] ,[]
    x = tuple(map(int,input("X-Axis: ").split(" ")))
    y = tuple(map(int,   input("Y-Axis: ").split(" ")))
    if (len(x) == len(y)):
        return [x,y,""]
    else:
        return [[],[],"Invalid Args: length must be same "]

def add_legend(plt):
    x,y,err = get_para()
    title = input("Legend Title: ")
    plt.plot(x,y)
    plt.legend(title)



def get_labels():
    x , y , z = input("X-Plot title: ") , input("Y-Plot title: ") , input("Graph Title: ")
    return [x,y,z]


def plot_graph():
    x , y , err = get_para()
    x_l , y_l , tit = get_labels()
    if(err == ""):
        plt.plot(x,y)
        plt.xlabel(x_l)
        plt.ylabel(y_l)
        plt.title(tit)
        add_legend(plt)
        plt.show()
    else:
        print (err)


if __name__ == "__main__":
    plot_graph()