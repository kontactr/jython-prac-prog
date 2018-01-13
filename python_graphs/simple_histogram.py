import matplotlib.pyplot as plt

def get_para():
    x = tuple(map(int, input("Bins: ").split(" ")))
    y = tuple(map(int,input("Data: ").split(" ")))
    return [x,y]

def plot_graph():
    x,y = get_para()
    plt.hist(y,bins=x,histtype="bar",label=input("Label-Name: "),cumulative=True,rwidth=0.8)
    plt.xlabel("X-Axis Name: ")
    plt.ylabel("Y-Axix Name: ")
    plt.title("Title: ")


def show_graph():
    plot_graph()
    plt.show()

if __name__ == "__main__":
    show_graph()



