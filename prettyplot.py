import matplotlib.pyplot as plt
import numpy as np
import seaborn.apionly as sns


axis_grey = (0.6, 0.6, 0.6)
titlesize = 20
fontsize = 14
labelsize = 16
figsize = (10, 7.5)


def set_figuresize():
    """
Set the size of a figure.
Default is (10, 7.5)
    """

    params = {"figure.figsize": figsize}

    plt.rcParams.update(params)


def set_legend(legend=None, ax=None):
    """
Set legend and legend options.

Parameters
----------
Optional arguments
legend : list | None
    legend list. If None only legend options are set, no legend is added.
    Default is None
ax : matplotlib.axis
    axis object, the axis object where to set the legend or legend options.
    Default is None
    """
    params = {
        "legend.frameon": True,
        "legend.numpoints": 1,
        "legend.scatterpoints": 1,
        "legend.fontsize": fontsize,
        "legend.handlelength": 2.2,
        "legend.borderpad": 0.5,
        "legend.framealpha": 2,
        "legend.fancybox": True
    }
    plt.rcParams.update(params)

    if legend is not None:
        if ax is None:
            plt.legend(legend)
        else:
            ax.legend(legend)


def set_font():
    """
Set font options. Note, uses latex.
    """
    params = {"text.usetex": True,
              "text.latex.preamble": r"\usepackage{lmodern}",
              "font.family": "lmodern",
              "font.weight": "normal"
              }

    plt.rcParams.update(params)


def set_linestyle():
    """
Set line style options
    """

    params = {"lines.linewidth": 2,
              "lines.marker": None,
              "lines.antialiased": True
              }

    plt.rcParams.update(params)


def set_tickstyle():
    """
Set tick style options
    """

    params = {"xtick.color": axis_grey,
              "ytick.color": axis_grey}

    plt.rcParams.update(params)


def set_axestyle():
    """
Set tick style options
    """

    params = {"axes.titlesize": titlesize,
              "axes.labelsize": labelsize,
              "axes.edgecolor": axis_grey,
              "axes.linewidth": 1
              }

    plt.rcParams.update(params)


# def set_grid(ax, bgcolor="#EAEAF2", linecolor="w", linestyle="-", linewidth=1.3):
#     """
# Set background color and grid line options
#
# Parameters
# ----------
# Required arguments
# ax : matplotlib.axis
#     axis object where the background color and grid line options are set
# bgcolor : str
#     background color
# linecolor : str
#     linecolor color
# linestyle : str
#     linestyle
# linewidth : float
#     linewidth
#     """
#     ax.set_axis_bgcolor(bgcolor)
#     ax.set_axisbelow("True")
#     ax.grid(True, color=linecolor, linestyle=linestyle, linewidth=linewidth,
#             zorder=0)

# def set_spines_colors(ax):
#     ax.spines["top"].set_edgecolor("None")
#     ax.spines["bottom"].set_edgecolor(axis_grey)
#     ax.spines["right"].set_edgecolor("None")
#     ax.spines["left"].set_edgecolor(axis_grey)

def spines_color(ax, edges={"top": "None", "bottom": axis_grey,
                            "right": "None", "left": axis_grey}):
    """
Set spines color

Parameters
----------
Required arguments
ax : matplotlib.axis
    axis object where the spine colors are set
edges : dictionary
    edges as keys with colors as key values
    """

    for edge, color in edges.items():
        ax.spines[edge].set_edgecolor(color)


def remove_ticks(ax):
    """
Remove ticks from right y axis and top x axis

Parameters
----------
Required arguments
ax : matplotlib.axis
    axis object where the ticks are removed
    """
    ax.tick_params(axis="x", which="both", bottom="on", top="off",
                   labelbottom="on", color=axis_grey, labelcolor="black",
                   labelsize=labelsize)

    ax.tick_params(axis="y", which="both", right="off", left="on",
                   labelleft="on", color=axis_grey, labelcolor="black",
                   labelsize=labelsize)


def get_colormap_tableu20(color=None):
    """
Get the Tableau20 colormap.

Parameters
----------
Optinal arguments
color : int
    returns #color from the Tableau20 colormap

Returns
----------
color : rgb tuple
    if color != None, then this color is returned
color : list of rgb tuples
    if color == None, then a list of rgb tuples is returned
    """

    tableau20 = [(31, 119, 180), (14, 199, 232), (255, 127, 14), (255, 187, 120),
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]


    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for i in range(len(tableau20)):
        r, g, b = tableau20[i]
        tableau20[i] = (r / 255., g / 255., b / 255.)

    if color is None:
        return tableau20
    else:
        color = color % len(tableau20)

        return tableau20[color]



# def get_colormap(nr_hues=6):
#     """
# Get the hls color palette from seaborn
#
# Parameters
# ----------
# Optional arguments
# nr_hues : int
#     the number of hues in the seaborn color palette.
#     Default is 6
#
#
# Returns
# ----------
# color : list of rgb tuples
#     """
#     return sns.color_palette("hls", nr_hues)
#
#
# def get_current_colormap():
#     """
# Get the current color palette
#
# Returns
# ----------
# color : list of rgb tuples
#     """
#     return sns.color_palette()


def set_title(title, ax=None):
    """
Set the title

Parameters
----------
Required arguments

title : str
   Title of the plot

Optional arguments

ax : matplotlib.axis object
    Axis object where to put the title
    """
    if ax is None:
        plt.title(title, fontsize=titlesize)
    else:
        ax.set_title(title, fontsize=titlesize)


def set_xlabel(xlabel, ax=None, color="black"):
    """
Set the x label

Parameters
----------
Required arguments

xlabel : str
   xlabel of the plot

Optional arguments

ax : matplotlib.axis object
    Axis object where to put the xlabel
color : matplotlib accepted color
    color of the label
    Default is "black"
    """
    if ax is None:
        plt.xlabel(xlabel, fontsize=labelsize, color=color)
    else:
        ax.set_xlabel(xlabel, fontsize=labelsize, color=color)


def set_ylabel(ylabel, ax=None, color="black"):
    """
Set the y label

Parameters
----------
Required arguments

ylabel : str
   ylabel of the plot

Optional arguments

ax : matplotlib.axis object
    Axis object where to put the ylabel
color : matplotlib accepted color
    color of the label
    Default is "black"
    """
    if ax is None:
        plt.ylabel(ylabel, fontsize=labelsize, color=color)
    else:
        ax.set_ylabel(ylabel, fontsize=labelsize, color=color)


def set_style(sns_style="darkgrid", nr_hues=6, palette=None):
    """
Set the style of a plot

Optional arguments

sns_style : str
    ["darkgrid" | "whitegrid" | "dark" | "white" | "ticks"]
    which seaborn style to use base.
    Default is "darkgrid"
nr_hues : int
    the number of hues in the seaborn color palette.
    Default is 6
palette : hls | husl | matplotlib colormap | seaborn color palette
    Set the matplotlib color cycle using a seaborn palette.
    Availible seaborn palette names:
        deep, muted, bright, pastel, dark, colorblind
    Other options:
        hls, husl, any named matplotlib palette, list of colors
    Matplotlib paletes can be specified as reversed palettes by appending "_r"
    to the name or as dark palettes by appending "_d" to the name.
    (These options are mutually exclusive, but the resulting list of colors
    can also be reversed).
    Default is "hsl"
    """
    sns.set_style(sns_style)

    if palette is None:
        sns.set_palette(get_colormap(nr_hues))
    else:
        sns.set_palette(palette)

    set_font()
    set_legend()
    set_figuresize()



def new_figure(sns_style="darkgrid", nr_hues=6, palette=None):
    """
Create a new figure

Optional arguments

sns_style : str
    ["darkgrid" | "whitegrid" | "dark" | "white" | "ticks"]
    which seaborn style to use base.
    Default is "darkgrid"
nr_hues : int
    the number of hues in the seaborn color palette.
    Default is 6
palette : hls | husl | matplotlib colormap | seaborn color palette
    Set the matplotlib color cycle using a seaborn palette.
    Availible seaborn palette names:
        deep, muted, bright, pastel, dark, colorblind
    Other options:
        hls, husl, any named matplotlib palette, list of colors
    Matplotlib paletes can be specified as reversed palettes by appending "_r"
    to the name or as dark palettes by appending "_d" to the name.
    (These options are mutually exclusive, but the resulting list of colors
    can also be reversed).
    Default is "hsl"

Returns
----------
ax : matplotlib.axis object
    """

    set_style(sns_style=sns_style, nr_hues=nr_hues, palette=palette)

    plt.figure()
    ax = plt.subplot(111)

    return ax



def prettyPlot(x=[], y=None, title="", xlabel="", ylabel="",
               color=None, sns_style="darkgrid", palette=None, nr_hues=6,
               ax=None, new_figure=True,
               linestyle="solid", linewidth=2, marker=None,
               **kwargs):
    """
prettyPlot

Creates pretty line plots, just a wrapper around matplotlib and seaborn.
Customizing several matplotlib options

Parameters
----------
Required arguments

x : list | array
   x values to plot

Optional arguments

y : list | array
   y values to plot
title : str
    Title of the plot.
    Default is ""
xlabel : str
    Xlabel of the plot.
    Default is ""
ylabel : str
    Ylabel of the plot.
    Default is ""
color : int
    Color of the line, given as a int.
    Uses #color from the current colormap
sns_style : str
    ["darkgrid" | "whitegrid" | "dark" | "white" | "ticks"]
    which seaborn style to use base.
    Default is "darkgrid"
palette : hls | husl | matplotlib colormap | seaborn color palette
    Set the matplotlib color cycle using a seaborn palette.
    Availible seaborn palette names:
        deep, muted, bright, pastel, dark, colorblind
    Other options:
        hls, husl, any named matplotlib palette, list of colors
    Matplotlib paletes can be specified as reversed palettes by appending "_r"
    to the name or as dark palettes by appending "_d" to the name.
    (These options are mutually exclusive, but the resulting list of colors
    can also be reversed).
    Default is "hsl"
nr_hues : int
    the number of hues to be used with the seaborn color palette
    #hues different colors
ax : matplotlib.axis object
    Axis object where to plot
    Default is None
new_figure : bool
    If a new figure should be made, or if the plot should be made
    ontop of the last existing plot.
    Default is True.
linestyle: str
    ["solid" | "dashed", "dashdot", "dotted" | (offset, on-off-dash-seq) | "-" | "--" | "-." | ":" | "None" | " " | ""]
linewidth : int
    width of the plotted lines.
    Default is 2
marker : accepted matplotlib marker
    marker for each plot point
**kwargs : unpacked dict
    arguments sent directly to matplotlib.bar()

Returns
----------
ax : matplotlib.axis object
    """

    set_style(sns_style, nr_hues=nr_hues, palette=palette)

    if ax is None:
        if new_figure:
            plt.figure()
            ax = plt.subplot(111)
        else:
            ax = plt.gca()


    if len(x) == 0:
        return ax

    spines_edge_color(ax)
    remove_ticks(ax)


    set_title(title, ax)
    set_xlabel(xlabel, ax)
    set_ylabel(ylabel, ax)


    if y is None:
        y = x
        x = range(len(y))


    if color is not None:
        colors = sns.color_palette()
        color = colors[color]


    ax.plot(x, y, linestyle=linestyle, marker=marker,
            markersize=8, markeredgewidth=2, linewidth=linewidth, antialiased=True,
            zorder=3, color=color, **kwargs)

    ax.yaxis.offsetText.set_fontsize(labelsize)
    ax.yaxis.offsetText.set_color("black")
    # ax.ticklabel_format(useOffset=False)


    # ax.set_xlim([min(x), max(x)])
    # ax.set_ylim([min(y), max(y)])


    return ax




# TODO updated doc string
def prettyBar(x, error=None, index=None, color=None,
              title="", xlabels=[], xticks=None, ylabel="",
              width=0.2, linewidth=0, ax=None, new_figure=True,
              sns_style="dark", palette=None, nr_hues=6,
              error_kw=None, **kwargs):
    """
Creates pretty bar plots, just a wrapper around matplotlib and seaborn.
Customizing several matplotlib options

Parameters
----------
Required arguments

x : list | array
   x values to plot

Optional arguments

error : list | array
    error for each x value
index : list | array
    x position of each bar

color : int
    Color of the line, given as a int.
    Uses #color from the current colormap
title : str
    Title of the plot.
    Default is ""
xlabels : list
    list of xlabels for the plot.
    Default is []
xticks : list | array
    position of each x label
ylabel : str
    ylabel of the plot.
    Default is ""
width : int
    width of each bar.
    Default is 0.2
linewidth : int
    width of line around each bar.
    Default is 0
ax : matplotlib.axis object
    Axis object where to plot
    Default is None
new_figure : bool
    If a new figure should be made, or if the plot should be made
    ontop of the last existing plot.
    Default is True.
sns_style : str
    ["darkgrid" | "whitegrid" | "dark" | "white" | "ticks"]
    which seaborn style to use base.
    Default is "dark"
palette : hls | husl | matplotlib colormap | seaborn color palette
    Set the matplotlib color cycle using a seaborn palette.
    Availible seaborn palette names:
        deep, muted, bright, pastel, dark, colorblind
    Other options:
        hls, husl, any named matplotlib palette, list of colors
    Matplotlib paletes can be specified as reversed palettes by appending "_r"
    to the name or as dark palettes by appending "_d" to the name.
    (These options are mutually exclusive, but the resulting list of colors
    can also be reversed).
    Default is "hsl"
nr_hues : int
    the number of hues to be used with the seaborn color palette
    #hues different colors
error_kw : dict
    Dictionary of kwargs to be passed to errorbar method.
    ecolor and capsize may be specified here rather than as independent kwargs.
**kwargs : unpacked dict
    arguments sent directly to matplotlib.bar(**kwargs)

Returns
----------
ax : matplotlib ax Object
    """

    set_style(sns_style, nr_hues=nr_hues, palette=palette)

    if ax is None:
        if new_figure:
            plt.figure()

            ax = plt.subplot(111)
        else:
            ax = plt.gca()

    spines_edge_color(ax)
    remove_ticks(ax)

    if index is None:
        try:
            index = np.arange(len(x))
        except TypeError:
            index = [0]

    if xticks is None:
        xticks = index


    if error_kw is None:
        error_kw = dict(ecolor=axis_grey, lw=2, capsize=10, capthick=2)

    if color is None:
        colors = sns.color_palette()
    else:
        colors = sns.color_palette()[color]

    ax.bar(index, x, yerr=error, color=colors, width=width,
           align="center", linewidth=linewidth, error_kw=error_kw,
           edgecolor=axis_grey, **kwargs)

    ax.set_xticks(xticks)
    ax.set_xticklabels(xlabels, fontsize=labelsize, rotation=0)

    # ax.set_xlim([min(x), max(x)])
    # ax.set_ylim([min(y), max(y)])

    set_title(title, ax)
    set_ylabel(ylabel, ax)


    return ax
