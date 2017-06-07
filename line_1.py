from matplotlib import pyplot as plt
from matplotlib import rc
from nltk import FreqDist

words = ['morze', 'Polska', 'sklep', 'wiosna', 'morze', 'dziecko']
filenames = ["lord-jim.txt", "przedwiosnie.txt", "sklepy-cynamonowe.txt", "szewcy.txt", "ziemia-obiecana-tom-pierwszy.txt"]
titles = ["Lord Jim", "Przedwiośnie", "Sklepy cynamonowe", "Szewcy", "Ziemia obiecana Tom I"]

def line_plot(names, args):
    plt.title("Liczba wystąpień słów")
    plt.xlabel("Próbki")
    plt.ylabel("Liczba wystąpień")
    colors = ["b", "g", "r", "c", "m", "y", "k", "w"]

    a = 0
    for i in args:
        plt.plot(args[a], color=colors[a%len(colors)], label=titles[a])
        a += 1

    # plt.plot(args[0], color='r', label=titles[0])
    # plt.plot(args[1], color='b', label=titles[1])
    plt.legend()

    plt.grid()

    plt.xticks(range(len(names)), names, rotation=90)

    plt.tight_layout()
    plt.savefig('plot.png')
    plt.show()

def count_freq(fname):
    with open(fname, encoding="utf8") as fp:
        split_words = fp.read().split()
        freq_dist = FreqDist(split_words)
    return freq_dist

def return_values(words, freq):
    result = []
    for s in words:
        result.append(freq[s] if s in freq else 0)
    return result


def make_plot(words, args):
    a = 0
    fre = []
    res = []
    for i in args:
        freq1 = count_freq(args[a])
        fre.append(freq1)
        res1 = return_values(words, fre[a])
        res.append(res1)
        a += 1


    line_plot(words, res)



def color_lines(texts):
    make_plot(words, filenames)

color_lines(filenames)