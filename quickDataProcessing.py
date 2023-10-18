import scipy.io as scio
    
scio.savemat("./res/"+tid+".mat", {
    "vel":avel,
    "pos":apos,
})

data = scio.loadmat(filePath)