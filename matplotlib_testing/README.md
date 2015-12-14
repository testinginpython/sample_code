Simple example of testing matplotlib images using pytest-mpl:
https://pypi.python.org/pypi/pytest-mpl

The key function in the file ``test_mandelbrot.py`` is:

```
@pytest.mark.mpl_image_compare
def test_mandelbrot_image():
    image = mandelbrot_set()
    fig = plt.gcf()
    plt.imshow(image, origin='lower', extent=(x0, x1, y0,y1),
               cmap=cm.Greys_r, interpolation='nearest')
    return fig
```
As required by the plugin, the decorated function should return a
``fig`` object.

(The code for the mandelbrot set is taken from https://github.com/doingmathwithpython/code/tree/master/chapter6/solutions)
