from ipywidgets import interact
from PIL import Image
import numpy as np
import scipy.ndimage as snd
import scipy.signal as sig

def std_threshold(video, thresholds = (0.0, 4.0, 0.1)):
    """
    Widget function for the standard deviation -based pixel threshold.
    """
    vid_std = video.std(axis = 0)
    frame = video[0]
    threshold = vid_std.mean()
    def _show(t = 1.0):
        f = frame.copy()
        f[~(vid_std > threshold * t)] = 0
        return Image.fromarray(f)
    return interact(_show, t = thresholds)

def std_filter_threshold(video,
        multipliers = (0.0, 4.0, 0.1),
        filtersize = (1, 15, 2)):
    """
    Adds a drop-down for picking how the threshold is set.
    """
    vid_std = video.std(axis = 0)
    frame = video[0]
    def _show(filter, multiplier = 1.0, filtersize = 3):
        f = frame.copy()
        if filter == "mean":
            ff = snd.gaussian_filter(vid_std, sigma = filtersize)
        else:
            ff = sig.medfilt2d(vid_std, kernel_size = filtersize)
        threshold = ff.mean()
        f[~(ff > threshold * multiplier)] = 0
        return Image.fromarray(f)
    return interact(_show, filter = ["mean", "median"], multiplier = multipliers, filtersize = filtersize)
