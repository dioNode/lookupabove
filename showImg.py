def showImg():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    img=mpimg.imread('out.png')
    imgplot = plt.imshow(img)
    plt.show()
