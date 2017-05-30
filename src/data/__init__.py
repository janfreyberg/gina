from pathlib import Path
import os

dataroot = Path('/') / 'data'/ 'group' / 'EEG' / 'GINA' / 'RAWDATA'

datafiles = list(dataroot.glob(pattern='*/*rest*.cnt'))

