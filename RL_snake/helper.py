import matplotlib.pyplot as plt
from IPython import display
import time

plt.ion()
plt.figure(1)

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Scores')
    plt.plot([i+1 for i in range(len(scores))], scores, '-g')
    plt.plot([i+1 for i in range(len(mean_scores))], mean_scores, '-b')
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.pause(0.1)









