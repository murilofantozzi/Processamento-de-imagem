import numpy as np
import cv2
import random as rng


def main():
    img = cv2.imread('carro2.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binaria = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
    desfoque = cv2.GaussianBlur(binaria, (5, 5), 0)
 
 
    cv2.imshow('Imagem original', img)
    #cv2.imshow('Cinza', gray)
    cv2.imshow('Binaria', binaria)
    #cv2.imshow('Desfoque', desfoque)
       
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# CONTORNO
#_, contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# DISPLAY


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
