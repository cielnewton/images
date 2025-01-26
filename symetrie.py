import matplotlib.image as mpimg
import numpy as np

def symetrie(nom):
    image = mpimg.imread(nom)
    nbl, nbc, nbcoul = image.shape
    newimage = np.zeros((nbl, nbc, nbcoul))  # Crée une nouvelle image vide de la même taille
    
    # Début du traitement
    for ligne in range(nbl):
        for colonne in range(nbc):
            for couleur in range(nbcoul):
                # Inversion des colonnes (symétrie horizontale)
                newimage[ligne, colonne, couleur] = image[ligne, nbc - 1 - colonne, couleur]
    
    return newimage

# Appel de la fonction symétrie sur l’image stinkbug.png
imagesymetrie = symetrie('stinkbug.png')
mpimg.imsave('monimagesymetrie.png', imagesymetrie)
