"""
@file
@brief Graphs on population
"""

import numpy


def plot_population_pyramid(men, women, ax=None,
                            title="Population Pyramid",
                            xlabel="People",
                            ylabel="Age",
                            labels=('Men', 'Women', 'difference'),
                            **options):
    """
    create a population pyramid

    @param      men         men  (starting at 0)
    @param      women       women (starting at 0)
    @param      ax          existing ax to use or new ax if None
    @param      title       graph title
    @param      xlabel      x label
    @param      ylabel      y label
    @param      labels      series names
    @param      options     options to create the graph if ax is None
    @return                 ax
    """
    if ax is None:
        from matplotlib import pyplot as plt
        fig, ax = plt.subplots(**options)

    somme = men - women
    ValH = ax.barh(numpy.arange(len(men)), men, 1.0, label=labels[
                   0], color='b', linewidth=0, align='center')
    ValF = ax.barh(numpy.arange(len(women)), -women, 1.0,
                   label=labels[1], color='r', linewidth=0, align='center')
    diff, = ax.plot(somme, numpy.arange(len(women)), 'y', linewidth=2)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_ylim([0, 110])
    ax.legend((ValH[0], ValF[0], diff), labels)
    return ax
