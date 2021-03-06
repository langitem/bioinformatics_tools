package create_snp_context_sequence;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class create_snp_context_sequence_app {
	public static void main(String[] args) {
		String filename = args[0];
/*
		try {
			BufferedReader lineReader = new BufferedReader(new FileReader(filename));
			String line = null;
			while ((line = lineReader.readLine()) != null) {
				System.out.println(line);
			}
			//System.out.println(lineReader);
		} catch (IOException e) {
			e.printStackTrace();
		}
*/		
		try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
			String line = null;
			while ((line = br.readLine()) != null) {
				System.out.println(line);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	} // end of main method
}
