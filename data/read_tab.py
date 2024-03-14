from astropy.io import ascii

files = ['benjamin_tab5_ne1e2.txt',
         'benjamin_tab5_ne1e4.txt',
         'benjamin_tab5_ne1e6.txt'
]
for file in files:
    fd = ascii.read(file)
    print(fd)
