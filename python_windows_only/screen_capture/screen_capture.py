import os

# windows only.
def capture(save_filename):
    import ImageGrab
    img = ImageGrab.grab()
    out = img.quantize(colors=16)
    out.save(save_filename)

if __name__ == '__main__':
    if os.name != 'nt':
        print "this script only works windows."
        exit(-1)
    capture('screen16.png')
