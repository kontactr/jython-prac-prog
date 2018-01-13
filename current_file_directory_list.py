from glob import glob
import os
print ("Files :-")
print (glob(os.getcwd()+"/*"))
#for directory
print ("\nDirectory :-")
print (glob(os.getcwd()+"/*/"))
