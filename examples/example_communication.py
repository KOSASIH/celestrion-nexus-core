from communication_protocols.universal_protocol import UniversalProtocol
from communication_protocols.nlp_engine import NLPEngine

def main():
    # Initialize communication protocols
    universal_protocol = UniversalProtocol()
    nlp_engine = NLPEngine()

    # Example message to encode and decode
    message = "Hello, this is a test message."
    print("Original message:", message)

    # Encode the message
    encoded_message = universal_protocol.encode_message(message, language="en")
    print("Encoded message:", encoded_message)

    # Decode the message
    decoded_message = universal_protocol.decode_message(encoded_message)
    print("Decoded message:", decoded_message)

    # Analyze text using NLP
    text = "Hello, I would like to know more about your services."
    analysis = nlp_engine.analyze_text(text)
    print("Text Analysis:", analysis)

    # Generate a response based on input text
    response = nlp_engine.generate_response(text)
    print("Generated Response:", response)

if __name__ == "__main__":
    main()
