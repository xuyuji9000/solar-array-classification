import matplotlib.pyplot as plt
from skimage import measure, color


class DrawContour(object):

    def __init__(self, contour_parameter):
        self.contour_parameter = contour_parameter

    def plot_contours(self, ax, contours):
        for n, contour in enumerate(contours):
            ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    def imshow(self, ax, img, **kwargs):
        ax.imshow(img, **kwargs)
        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])

    def plot_pair(self, plot, original_image):
        grey_image = color.rgb2gray(original_image)
        contours = measure.find_contours(grey_image, self.contour_parameter)

        self.imshow(plot[1], original_image)

        self.plot_contours(plot[0], contours)
        # TRICK: plt draw some strange color with gray image , we need to force gray rendering
        self.imshow(plot[0], grey_image, interpolation='nearest', cmap=plt.cm.gray)

    def plot(self, img_list):
        fig, ax = plt.subplots(2, len(img_list), figsize=(18, 6))
        ax = map(list, zip(*ax))  # INFO: transpose 2d array
        for i, img in enumerate(img_list):
            self.plot_pair(ax[i], img)
        plt.show()
        return ax