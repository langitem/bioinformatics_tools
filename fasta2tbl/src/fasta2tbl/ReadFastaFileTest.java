package fasta2tbl;

public class ReadFastaFileTest {
	
	public static void main(String[] args) {
		ReadFastaFile application = new ReadFastaFile();
		application.openFastaFile();
		application.readFastaFile();
		application.closeFastaFile();
	}

}
