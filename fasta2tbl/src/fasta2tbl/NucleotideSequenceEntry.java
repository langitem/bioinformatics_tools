package fasta2tbl;

public class NucleotideSequenceEntry {
	String defline;
	String nucleotideSequence;
	
	// no argument constructor
	public NucleotideSequenceEntry() {
		this.defline = "";
		this.nucleotideSequence = "";
	}
	
	// initialize an entry
	public NucleotideSequenceEntry(String defln, String sequence) {
		this.defline = defln;
		this.nucleotideSequence = sequence;
	}
	
	public void setDefline (String defln) {
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
		this.nucleotideSequence += additionalSequence;
	}

}
