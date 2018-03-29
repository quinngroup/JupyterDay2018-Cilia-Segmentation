# Jupyter Day 2018: Cilia Segmentation

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/quinngroup/JupyterDay2018-Cilia-Segmentation/master?filepath=JupyterDayATL-2018.ipynb)

Talk title: *Reproducible Segmentation of Not-Quite-Objects*

Presentation materials for my talk on cilia segmentation for Jupyter Day ATL.

### Code Structure

The main content is in the `ipynb` notebook file.

The data needed by the analyses in the notebook are found in the `data` folder, which has two subfolders:
 - `videos` : three `npy` files that contain the grayscale videos
 - `segmaps` : three `npy` files that contain the black-and-white ground-truth segmentation masks for each video

You can load any of these data yourself using the `numpy.load` function.

The other folder is `spq`, which is a module containing some helper code for the analyses in the notebook.
 - `spq.widgets` has the full code needed for generating the variance-based threshold widgets
 - `spq.utils` has the parameter-scan versions of the same functions
 - `spq.evaluate` has the function that implements intersection-over-union for evaluating our predicted masks against the ground-truth

### How to run

The easiest way is to click the "launch binder" button at the top of this `README`. That will launch a new tab in your window and spin up this repository as an active Jupyter environment. It may take a few minutes but you should be able to re-run everything in the notebook, even editing to your heart's content.

If you want greater control, you can clone this notebook, make sure you have the prereqs installed (via `environment.yml`), and then simply `jupyter notebook` your way to success.

### Contributing

 - Tweet at me [@SpectralFilter](https://twitter.com/SpectralFilter)
 - Email me [spq@uga.edu](mailto:spq@uga.edu)
 - Open up a ticket here, I guess?
 - Smoke signals are cool too

### License

MIT
