package create_snp_context_sequence;

public class nucleotideSequenceEntry {
	private String sequenceId;
	private String nucleotideSequence;
	
	public String getSequenceId() {
		return sequenceId;
	}
	
	public void setSequenceId(String sequenceId) {
		this.sequenceId = sequenceId;
	}
	
	public String getNucleotideSequence() {
		return nucleotideSequence;
	}
	
	public void setNucleotideSequence(String nucleotideSequence) {
		this.nucleotideSequence = nucleotideSequence;
	}
	
	public void appendToNucleotideSequence(String additionalSequence) {
		StringBuilder nucleotideSequenceStringBuilder = new StringBuilder(nucleotideSequence);
		nucleotideSequenceStringBuilder.append(additionalSequence);
		this.nucleotideSequence = nucleotideSequenceStringBuilder.toString();
	}

}
