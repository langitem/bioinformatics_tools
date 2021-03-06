package fasta2tbl;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;


public class ReadFastaFile {
	private Scanner input;
	
	// open fasta file
	public void openFastaFile(String fastaFilename) {
		try {
			// input = new Scanner(new File("/Users/emanuellangit/Documents/coding_practice/sequence.fasta"));
			input = new Scanner(new File(fastaFilename));
		} catch(FileNotFoundException fileNotFoundException) {
			System.err.println("Error opening file");
			System.exit(1);
		}
		
	} // end of openFastaFile
	
	
	// read fasta file
	public void readFastaFile() {
		
		// object to be written to the screen
		NucleotideSequenceEntry nucSeqEntry = new NucleotideSequenceEntry();
		
		// read sequence entries from file using Scanner object
		try {
			while(input.hasNextLine()) {
				String line = input.nextLine();
				if (line.matches("^>.*$")) {
					String defline = line.replace(">", "");
					nucSeqEntry.setDefline(defline);
					nucSeqEntry.setNucleotideSequence("");
					System.out.printf("\n%s\t", nucSeqEntry.getDefline());
				} else {
					
					if (!(nucSeqEntry.getDefline().contentEquals(""))) {
						String sequenceLine = line.replaceAll(" ", "");
						nucSeqEntry.append2nucleotideSequence(sequenceLine);
						System.out.printf("%s", sequenceLine);
					}
				}
				
			} // end of while
		} catch(NoSuchElementException elementException) {
			System.err.println("File improperly formed.");
			input.close();
			System.exit(1);
		} catch(IllegalStateException stateException) {
			System.err.println("Error reading from file");
			System.exit(1);
		} // end catch

	} // end of readFastaFile
	
	// close file and terminate application
	public void closeFastaFile() {
		if (input != null) {
			input.close();
		}
	} // end closeFastaFile method

}
