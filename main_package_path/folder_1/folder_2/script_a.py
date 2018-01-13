#from ...folder_3 import script_c
#from main_package.folder_3 import script_c




"""


must add path for all packages
we add all paths in sys.path
so we can access modules in different locations


"""

import sys

print(sys.path)
#sys.path.append("C:\\Users\\Sony\\Desktop\\jython-prac-prog\\main_package_path\\folder_1")  optional import 
#sys.path.append("C:\\Users\\Sony\\Desktop\\jython-prac-prog\\main_package_path")  optional import
sys.path.append("C:\\Users\\Sony\\Desktop\\jython-prac-prog")



from main_package_path.folder_3 import script_c
from main_package_path.folder_1.folder_2 import *
print ("hello wolrd")
