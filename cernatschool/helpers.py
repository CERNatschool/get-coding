#!/usr/bin/env python
# -*- coding: utf-8 -*-

#...for the MATH.
import numpy as np

#...for the plotting.
import pylab as plt

#...for the colours.
from matplotlib import colorbar, colors

def make_frame_image(xs, ys, Cs):
    """ Create a figure displaying the frame data. """

    ## The minimum x value.
    x_min = 0

    ## The maximum x value.
    x_max = 256

    ## The minimum y value.
    y_min = 0

    ## The maximum y value.
    y_max = 256

    ## The width of the frame.
    w = 256

    ## The height of the frame.
    h = 256

    ## The maximum count value.
    C_max = 1

    # We add this just in case there are no pixels supplied.
    if len(Cs) > 0:
        C_max = max(Cs)

    # Create the figure.
    plt.close('all')

    ## The default size of the figure [inches].
    fig_size = 5.0

    ## The figure for the frame.
    fig = plt.figure(1, figsize=(fig_size*1.27, fig_size), dpi=150, facecolor='w', edgecolor='w')

    ## The frame axes.
    figax = fig.add_subplot(111, axisbg='#222222')

    # Add the frame background (blue).
    figax.add_patch(plt.Rectangle((0,0),256,256,facecolor='#82bcff'))

    # Add a grid.
    plt.grid(1)

    # Select the "hot" colour map for the pixel counts and add a
    # colour bar to indicate the count value for each pixel.
    #
    cmap = plt.cm.hot
    #
    colax, _ = colorbar.make_axes(plt.gca())
    #
    col_max = 10*(np.floor(C_max/10.)+1)
    #
    colorbar.ColorbarBase(colax,cmap=cmap,norm=colors.Normalize(vmin=0,vmax=col_max))

    # Loop over the pixels and add them to the figure.
    for i, x in enumerate(xs):
        ## The scaled count value (for the colour map).
        scaled_C = float(Cs[i])/float(col_max)

        # Rather than use, say, a 2D histogram for the pixels, we add
        # a coloured square to the plot for each pixel.
        figax.add_patch(plt.Rectangle((xs[i],ys[i]),1,1,edgecolor=cmap(scaled_C),facecolor=cmap(scaled_C)))

    ## The frame border width [pixels].
    b = 3

    # Set the axis limits based on the cluster radius.
    figax.set_xlim([0 - b, 256 + b])
    figax.set_ylim([0 - b, 256 + b])

    #return fig
