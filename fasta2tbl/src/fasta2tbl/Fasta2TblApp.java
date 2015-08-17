package fasta2tbl;

public class Fasta2TblApp {
	public static void main(String[] args) {
		String fastaFilename = "";
		if (args.length == 1) {
			fastaFilename = args[0];
			System.out.println(fastaFilename);
		} else {
			System.out.println("Input one argument for the fasta file!");
			System.exit(0);
		}
		
		ReadFastaFile readFastaFile = new ReadFastaFile();
		readFastaFile.openFastaFile(fastaFilename);
		readFastaFile.readFastaFile();
		readFastaFile.closeFastaFile();
		
	} // end main

}
