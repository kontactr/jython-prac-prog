import java.io.*;
import java.util.*;
public class ProcessWriter {
    public static void main(String[] args) throws Exception {
        ProcessBuilder builder = new ProcessBuilder("java", "Test");
        builder.directory(new File("C:\\Users\\Sony\\Desktop\\jython-prac-prog\\network"));
        Process process = builder.start();

        OutputStream stdin = process.getOutputStream(); // <- Eh?
        InputStream stdout = process.getInputStream();

        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout));
        BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(stdin));

        writer.write("Sup buddy");
		writer.write("Sup buddy");
		writer.write("Sup buddy");
		writer.write("Sup buddy");
        writer.flush();
        writer.close();

        Scanner scanner = new Scanner(stdout);
        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }
    }
}