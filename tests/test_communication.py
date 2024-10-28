import unittest
from communication_protocols.universal_protocol import UniversalProtocol
from communication_protocols.nlp_engine import NLPEngine

class TestUniversalProtocol(unittest.TestCase):
    def setUp(self):
        self.protocol = UniversalProtocol()

    def test_encode_message(self):
        message = "Hello, World!"
        encoded = self.protocol.encode_message(message, language="en")
        self.assertIn("version", encoded)
        self.assertIn("language", encoded)
        self.assertIn("content", encoded)

    def test_decode_message(self):
        message = "Hello, World!"
        encoded = self.protocol.encode_message(message, language="en")
        decoded = self.protocol.decode_message(encoded)
        self.assertEqual(decoded["content"], message)

class TestNLPEngine(unittest.TestCase):
    def setUp(self):
        self.nlp_engine = NLPEngine()

    def test_analyze_text(self):
        text = "Hello, I would like to know more about your services."
        analysis = self.nlp_engine.analyze_text(text)
        self.assertGreater(len(analysis["tokens"]), 0)
        self.assertGreater(len(analysis["entities"]), 0)

    def test_generate_response(self):
        response = self.nlp_engine.generate_response("Hello")
        self.assertEqual(response, "Hello! How can I assist you today?")
        response = self.nlp_engine.generate_response("Goodbye")
        self.assertEqual(response, "Goodbye! Have a great day!")

if __name__ == "__main__":
    unittest.main()
