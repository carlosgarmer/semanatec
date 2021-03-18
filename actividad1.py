import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def aplicador(frag, kernel):

    f_row, f_col = frag.shape
    k_row = len(kernel[0])
    k_col = len(kernel)
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += frag[row,col] *  kernel[row][col]
    return result

def con(imagen,kernel,padd):
    #Primero definir el tamaño de la imagen y del filtro
    imgFil,imgCol = imagen.shape
    kernelFil = len(kernel[0])
    kernelCol = len(kernel)
    paddf = 0
    if padd >0 :
        paddf = padd % 2

    final = np.zeros((imgFil- padd ,imgCol- padd))

    for fila in range(paddf, imgFil-padd):
        for col in range(paddf, imgCol-padd):
                final[fila, col] = aplicador(
                                    imagen[fila- paddf:fila -paddf+ kernelFil, 
                                    col -paddf :col -paddf+ kernelCol],kernel)
    plt.imshow(final, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernelFil, kernelCol))
    plt.show()

def main():
    ap = argparse.ArgumentParser()

    ap.add_argument("-img", "--foperand", required=True)
    ap.add_argument("-pad", "--soperand", required=True)
    args = vars(ap.parse_args())
    path = args['foperand']
    padd = int(args['soperand'])
    print(path)
    img = cv2.imread(path, 0) 
    kernel = [[1,0,1],[1,0,1],[1,0,1]]
    con(img,kernel,padd)

    return 0

main()

  