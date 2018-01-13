/* not able to compile because Employee class is in python file */

import java.io.*;

class obj_des_java
{
	public static void main(String args[])throws Exception
	{
	 try{
		ObjectInputStream o = new ObjectInputStream(new FileInputStream("file7.txt"));
		Employee e;
		while ((e = (Employee) e.readObject()) != null)
				e.display();
		}finally{
		o.close();
	}
	}
}
