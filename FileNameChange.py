import os

directory = 'icon'

[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('_', ' ').lower()) for f in os.listdir(directory)]