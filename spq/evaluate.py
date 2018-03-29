def iou(ypred, ytrue):
    """
    Evaluates the overlap of the predicted mask with the ground-truth mask.
    Cilia versus non-cilia are indicated by 1 and 0, respectively.

    Parameters
    ----------
    ypred : array, shape (N, M)
        Binary predicted segmentation mask.
    ytrue : array, shape (N, M)
        Binary ground-truth segmentation mask.

    Returns
    -------
    iou : float
        Intersection-over-union. This is literally the fraction of pixels
        between the two masks that overlap, divided by the total number of
        pixels encompassed by the two masks. 1 = perfect, 0 = fail.
    """
    # Calculate the number of intersecting and union pixels.
    mask_pred = (ypred == 1)
    mask_true = (ytrue == 1)
    inter = (mask_true & mask_pred).sum()
    union = (mask_true | mask_pred).sum()
    iou = float(inter) / float(union)
    return iou
