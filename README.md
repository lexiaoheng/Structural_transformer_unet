# Structural_transformer_unet
# 1.Dataset Preparation
    Create a folder named data in the root directory, and then create a folder named Synapse in this folder.
    In the Synapse folder, a folder named test_vol_h5 is used to store the validation set data, and a folder named train_npz is used to store the training set. All data         types are npz files, images and labels can be processed using npz.py in the root directory of the repository, see npz.py for details.
    After processing it into an npz file, use txtgenerator.py in the root directory of the library to generate a directory file of type txt and store it in                       ./lists/lists_Synapse. See the txtgenerator.py file for details.
    The labels of the test data are only used to generate the evaluation log.
# 2.configs.yaml
    Modify the parameters in the corresponding ./configs/configs.yaml according to your own data and model size requirements
# 3.train.py
    Modify the parameters in the corresponding ./train.py according to your own data and model size requirements.
Train and validation!
