import numpy as np
import scipy.signal as sig
import scipy.ndimage as snd

def std(video, threshold):
    """
    Applies a threshold on the mean of the standard deviation pixel intensity.
    """
    vid_std = video.std(axis = 0)
    mask = vid_std > vid_std.mean() * threshold
    prediction = np.zeros(shape = mask.shape)
    prediction[mask] = 1
    return prediction

def std_filter(video, multiplier, filter, filtersize):
    """
    Performs the prescribed variance-based filter.
    """
    vid_std = video.std(axis = 0)
    if filter == "mean":
        ff = snd.gaussian_filter(vid_std, sigma = filtersize)
    else:
        ff = sig.medfilt2d(vid_std, kernel_size = filtersize)
    threshold = ff.mean() * multiplier
    mask = ff > threshold
    prediction = np.zeros(shape = mask.shape)
    prediction[mask] = 1
    return prediction
