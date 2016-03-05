# pyWallaby
# adaptation of the KIPR Wallaby code to work with python.

# cd to project directory
swig -python -I/usr/include/wallaby/ wallaby.i
python setup.py build_ext --inplace
