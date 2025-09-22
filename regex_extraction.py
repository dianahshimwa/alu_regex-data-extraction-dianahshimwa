import re

# Regex patterns
patterns = {
    "emails": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "urls": r"https?:\/\/(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:\/\S*)?",
    "phone_numbers": r"(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}",
    "credit_cards": r"(?:\d{4}[- ]?){3}\d{4}",
    "time": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

# Read text samples from file
with open("test_strings.txt", "r") as f:
    text = f.read()

# Extraction
for label, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{label}: {matches}")
