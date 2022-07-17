import numpy as np
from numba import jit


KERNEL_SIZE = 15


def nightvision(img):
    w = KERNEL_SIZE
    brightch = np.zeros((img.shape))
    padded = np.pad(
        img, ((int(w / 2), int(w / 2)), (int(w / 2), int(w / 2)), (0, 0)), "edge"
    )
    fill_brightch(brightch, padded, w)
    return brightch


@jit(nopython=True)
def fill_brightch(brightch, padded, w):
    for i, j in np.ndindex(brightch.shape[:2]):
        brightch[i, j, :] = np.max(padded[i : i + w, j : j + w, :])
