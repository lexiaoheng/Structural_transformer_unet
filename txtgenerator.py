import glob

path = r'./data/Synapse/test_vol_h5/*.npz'
path2 = r'./lists/lists_Synapse/test_vol.txt'
files = glob.glob(path)
f = open(path2, 'w')
for i in files:
    name = i.split('\\')[-1]
    name = name[:-4]+'\n'
    f.write(name)
f.close()
