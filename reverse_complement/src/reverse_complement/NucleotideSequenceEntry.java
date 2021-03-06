package reverse_complement;


public class NucleotideSequenceEntry {
	private String defline;
	private String nucleotideSequence;
	
	// no argument constructor
	public NucleotideSequenceEntry () {
		this.defline = "";
		this.nucleotideSequence = "";
	}
	
	// initialize an entry
	public NucleotideSequenceEntry(String defln, String sequence) {
		this.defline = defln;
		this.nucleotideSequence = sequence;
	}
	
	public void setDefline(String defln) {
		this.defline = defln;
	}
	
	public String getDefline() {
		return defline;
	}
	
	public void setNucleotideSequence(String sequence) {
		this.nucleotideSequence = sequence;
	}
	
	public String getNucleotideSequence() {
		return nucleotideSequence;
	}
	
	public void append2nucleotideSequence(String additionalSequence) {
		String additionalSequenceQcd = additionalSequence.replaceAll("\\s+", ""); // remove spaces
		this.nucleotideSequence += additionalSequenceQcd;
	}
	
	public String getReverseComplement() {
		// capitalize each nucleotide
		String nuclSeqCapitalized = this.nucleotideSequence.toUpperCase();
		
		// reverse the nucleotide string:
		String nucSeqReversed = "";
		for (int i=nuclSeqCapitalized.length() - 1; i != -1; i--) {
			nucSeqReversed += nuclSeqCapitalized.charAt(i);
		}
		
		
		// Complement each nucleotide in the string:
		StringBuilder nuclSeqRevCompl = new StringBuilder();
		for (int i=0; i < nucSeqReversed.length(); ++ i) {
			char nucleotide = nucSeqReversed.charAt(i);
			switch(nucleotide) {
			case 'A':
				nuclSeqRevCompl.append('T');
				break;
			case 'C':
				nuclSeqRevCompl.append('G');
				break;
			case 'G':
				nuclSeqRevCompl.append('C');
				break;
			case 'T':
				nuclSeqRevCompl.append('A');
				break;
			} // end switch
			
		}
		
		return nuclSeqRevCompl.toString();
	} // end of getReverseComplement method

}
