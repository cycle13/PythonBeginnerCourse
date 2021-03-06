import matplotlib
# Some adjustments to the axis labels, ticks and fonts
def load_xy_style(ax, xlabel='Time [UTC]', ylabel='Height [m]'):
    """
    Method that alters the apperance of labels on the x and y axis in place.

    Note:
        If xlabel == 'Time [UTC]', the x axis set to major 
        ticks every 3 hours and minor ticks every 30 minutes.

    Args:
        ax (matplotlib.axis) :: axis that gets adjusted
        **xlabel (string) :: name of the x axis label
        **ylabel (string) :: name of the y axis label

    """

    ax.set_xlabel(xlabel, fontweight='semibold', fontsize=15)
    ax.set_ylabel(ylabel, fontweight='semibold', fontsize=15)
    if xlabel == 'Time [UTC]':
        ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%H:%M'))
        ax.xaxis.set_major_locator(matplotlib.dates.HourLocator(interval=3))
        ax.xaxis.set_minor_locator(matplotlib.dates.MinuteLocator(byminute=[0, 30]))
        ax.yaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(500))
    ax.tick_params(axis='both', which='major', labelsize=14, width=3, length=4)
    ax.tick_params(axis='both', which='minor', width=2, length=3)


def load_cbar_style(cbar, cbar_label=''):
    """
    Method that alters the apperance of labels on the color bar axis in place.

    Args:
        ax (matplotlib.axis) :: axis that gets adjusted
        **cbar_label (string) :: name of the cbar axis label, Defaults to empty string.

    """
    cbar.ax.set_ylabel(cbar_label, fontweight='semibold', fontsize=15)
    cbar.ax.tick_params(axis='both', which='major', labelsize=14, width=2, length=4)

