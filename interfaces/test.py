class InformalParserInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def extract_text(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        pass

class PdfParser(InformalParserInterface):
    """Extract text from a PDF"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides InformalParserInterface.extract_text()"""
        pass

class EmlParser(InformalParserInterface):
    """Extract text from an email"""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides InformalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override InformalParserInterface.extract_text()
        """
        pass

# Check if both PdfParser and EmlParser implement InformalParserInterface
print(f"issubclass(PdfParser, InformalParserInterface): {issubclass(PdfParser, InformalParserInterface)}")
print(f"issubclass(EmlParser, InformalParserInterface): {issubclass(EmlParser, InformalParserInterface)}")

# check mro: method resolution order for both inherited classes
print(f"PdfParser.__mro__: {PdfParser.__mro__}")
print(f"EmlParser.__mro__: {EmlParser.__mro__}")

print(f"type(EmlParser): {type(EmlParser)}")
