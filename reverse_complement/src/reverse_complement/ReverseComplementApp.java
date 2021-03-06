// Application class for reverse complementing 
package reverse_complement;

public class ReverseComplementApp {
	
	public static void main(String[] args) {
		
		String fastaFilename = "";
		if (args.length == 1) {
			fastaFilename = args[0];
		} else {
			System.out.println("Input one argument for the fasta filename!");
			System.exit(0);
		}
		
		ReadFasta readFastaFile = new ReadFasta();
		readFastaFile.openFastaFile(fastaFilename);
		readFastaFile.readFasta();
		readFastaFile.closeFasta();
	} // end of main method

}
