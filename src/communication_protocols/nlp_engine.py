import spacy

class NLPEngine:
    def __init__(self, model="en_core_web_sm"):
        """Initializes the NLP engine with a specified model."""
        self.nlp = spacy.load(model)

    def analyze_text(self, text):
        """Analyzes the text and returns linguistic features."""
        doc = self.nlp(text)
        analysis = {
            "tokens": [token.text for token in doc],
            "lemmas": [token.lemma_ for token in doc],
            "pos_tags": [token.pos_ for token in doc],
            "entities": [(ent.text, ent.label_) for ent in doc.ents]
        }
        return analysis

    def generate_response(self, input_text):
        """Generates a simple response based on input text."""
        doc = self.nlp(input_text)
        if any(token.lemma_ == "hello" for token in doc):
            return "Hello! How can I assist you today?"
        elif any(token.lemma_ == "bye" for token in doc):
            return "Goodbye! Have a great day!"
        else:
            return "I'm not sure how to respond to that."

# Example usage
if __name__ == "__main__":
    nlp_engine = NLPEngine()
    text = "Hello, I would like to know more about your services."
    
    # Analyze the text
    analysis = nlp_engine.analyze_text(text)
    print("Text Analysis:", analysis)

    # Generate a response
    response = nlp_engine.generate_response(text)
    print("Generated Response:", response)
