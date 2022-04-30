import numpy
import cv2


def RemoveSquare(image, step=1, start=(0, 0), stop=None):
    if stop is None:
        stop = image.shape
    size = (stop[0] - start[0]) // 3
    center = (start[0] + size, start[1] + size)
    image[center[0] : center[0] + size, center[1] : center[1] + size] = 0
    if step == 1:
        return image
    for x in range(start[0], stop[0], size):
        for y in range(start[1], stop[1], size):
            if x != center[0] or y != center[1]:
                image = RemoveSquare(image, step - 1, (x, y), (x + size, y + size))
    return image


def CreateCarpet(steps, pixel_size=1):
    size = pixel_size * (3 ** steps)
    carpet = numpy.ones((size, size))
    return RemoveSquare(carpet, steps)


if __name__ == "__main__":
    carpet = CreateCarpet(5, 1)
    cv2.imshow("Carpet", carpet)
