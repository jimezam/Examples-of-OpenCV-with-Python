# Install OpenCV

## Install using *virtualenv* and *virtualenvwrapper*

Create a new virtual environment called `opencv`.

```
$ mkvirtualenv opencv
```

Activate the `opencv` environment (not really needed after creation).

```
# workon opencv
```

Install the required packages using *pip*.

```
$ pip3 install opencv-contrib-python numpy
```

At the end, deactive the `opencv` environment.

```
$ deactivate
```

## Test the installation

```
(opencv) $ python3 -c "import cv2; print(cv2.__version__)"

4.4.0
```

# References

 - opencv-python in pip  
 https://pypi.org/project/opencv-python/
 - pip install opencv in PyImageSearch  
 https://www.pyimagesearch.com/2018/09/19/pip-install-opencv/
 - VirtualenvWrapper documentation  
 https://virtualenvwrapper.readthedocs.io/en/latest/