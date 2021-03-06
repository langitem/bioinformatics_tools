package reverse_complement;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class ReadFasta {
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
	public void readFasta() {
		// object to be written to the screen
		NucleotideSequenceEntry nucSeqEntry = new NucleotideSequenceEntry();

		// read sequence entries from file using Scanner object
		try {
			while(input.hasNextLine()) {
				String line = input.nextLine();
				if (line.matches("^>.*$")) {
					
					// if this is not the first entry
					if (!nucSeqEntry.getDefline().contentEquals("")) {
						System.out.printf("%s \n", nucSeqEntry.getReverseComplement());
					}
					
					String defline = line;
					nucSeqEntry.setDefline(defline);
					nucSeqEntry.setNucleotideSequence("");
					System.out.printf("\n%s, reverse complement\n", nucSeqEntry.getDefline());
				} else { // if it's not a defline
					
					if (!(nucSeqEntry.getDefline().contentEquals(""))) {
						String sequenceLine = line.replaceAll(" ", "");
						nucSeqEntry.append2nucleotideSequence(sequenceLine);
						//System.out.printf("%s", sequenceLine);
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
		
		// System.out.println(nucSeqEntry.getDefline());
		System.out.println(nucSeqEntry.getReverseComplement());
		
	} // end of readFasta
	
	public void closeFasta() {
		if (input != null) {
			input.close();
		}
	}

}
