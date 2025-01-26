import numpy as np
import matplotlib.image as mpimg

def rotation(nom):
    image = mpimg.imread(nom)
    print(type(image))
    nbl, nbc, nbcoul = image.shape
    newimage = np.zeros((nbc, nbl, nbcoul))
    for ligne in range(nbl):
        for colonne in range(nbc):
            for couleur in range(nbcoul):
                #newimage[colonne, nbl - 1 - ligne, couleur] = image[ligne, colonne, couleur]
                newimage[colonne, ligne, couleur] = image[ligne, colonne, couleur]
    return newimage

# Lire l'image originale
imagetournee = rotation('canyon.png')

# Sauvegarder l'image tournée
mpimg.imsave('autre_canyon90.png', imagetournee)
