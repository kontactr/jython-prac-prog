import matplotlib.pyplot as plt


def get_para():
    x = tuple(map(float, input("X-Axis: ").split(" ")))
    y = tuple(map(float, input("Y-Axis: ").split(" ")))
    if len(y) == len(x):
        return [x, y, ""]
    else:
        return [[], [], "Invalid Args: Length Must Be Same."]


def add_legend():
    x, y, err = get_para()
    plt.bar(x, y,label=input("Label Name: "))
    plt.legend()


def get_titles():
    plt.xlabel("X-Title: ")
    plt.ylabel("Y-Title: ")
    plt.title("Grapg-Title: ")


def plot_graph():
    x, y, err = get_para()
    print(err)
    plt.bar(x, y,label=input("Label Name: "))


def main():
    plot_graph()
    add_legend()
    plt.show()


if __name__ == "__main__":
    main()
