import operator
import pyautogui as gui
from functools import reduce

def regionMatchesColor(region, color, tolerance):
    """Check if the average color of the given region matches color.
    """
    im = gui.screenshot(region=region)
    im_data = list(im.getdata())

    count = len(im_data)
    total_color = reduce(lambda p1, p2: tuple(map(operator.add, p1, p2)), im_data)
    mean_color = (total_color[0] / count, total_color[1] / count, total_color[2] / count)

    color_diff = tuple(map(lambda a, b: abs(a - b), mean_color, color))

    return max(color_diff) <= tolerance
