# PGHcrime2DTree
Simple program that stores and processes Pittsburgh 1990s Crime Data using a 2D tree.
## Note
The main() and TwoDTreeDriver() are written to specifically parse crimefile.csv file. If you want to use the data structure with other file, you should change these two functions
## Included in this repository
- crimefile.csv - Pittsburgh 1990s Crimes Data
- TwoDTree.py - main program
- PGHCrimes.kml - example output of option 6
## How to run
Run the following command

`% python TwoDTree.py`

The following prompt would appear. Follow the prompt instruction
```
Crime file loaded into 2d tree with 27218 records.
What would you like to do?
1: inorder
2: pre-order
3: level-order
4: post-order
5: reverse level-order
6: search for points within range
7: search for nearest neighbor
8: quit
```

Option 6 will ouput .kml file that can be load into Google Earth (given correct input). An example .kml file is included in this repository
