from dataclasses import dataclass

@dataclass
class SpeechActFeatures:
    """Parameters to measure the linguistic agency of an AI."""
    semantic_understanding: float  # Scale: 0.0 to 1.0
    belief_like_states: float      # Scale: 0.0 to 1.0
    theory_of_mind: float          # Scale: 0.0 to 1.0
    normative_sanctionability: float # Scale: 0.0 to 1.0

class AgencyClassifier:
    def __init__(self):
        self.version = "V410"
        self.creator = "Master Shivam"

    def classify_linguistic_agency(self, features: SpeechActFeatures) -> str:
        """
        Classifies linguistic agency based on the provided feature scores.
        """
        # Calculating the average score
        total_score = (
            features.semantic_understanding + 
            features.belief_like_states + 
            features.theory_of_mind + 
            features.normative_sanctionability
        ) / 4

        if total_score < 0.2:
            return "NON-ASSERTER (Simulation Only - e.g., Talking Clock)"
        elif total_score < 0.5:
            return "PROTO-ASSERTER (LLM - Limited Understanding)"
        elif total_score < 0.7:
            return "PROTO-ASSERTER (LLM - Moderate Understanding)"
        elif total_score < 0.9:
            return "PROTO-ASSERTER (LLM - Advanced Understanding)"
        else:
            return "FULL-ASSERTER (Human - Complete Understanding)"

# --- Example Usage ---
if __name__ == "__main__":
    # Example scores for a highly advanced AI
    features = SpeechActFeatures(
        semantic_understanding=0.85, 
        belief_like_states=0.80, 
        theory_of_mind=0.75, 
        normative_sanctionability=0.80
    )
    
    classifier = AgencyClassifier()
    result = classifier.classify_linguistic_agency(features)
    print(f"Project: Mohini Omega {classifier.version}")
    print(f"Result: {result}")
