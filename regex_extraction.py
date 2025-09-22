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

# Function to find valid and invalid matches
def extract_matches(pattern, sample_text):
    all_words = re.findall(r"\S+", sample_text)
    valid = re.findall(pattern, sample_text)
    # Invalid = words in text that contain letters/numbers but don’t match regex
    invalid = [word.strip(",") for word in all_words if word not in valid and any(c.isalnum() for c in word)]
    return valid, invalid    

# Extraction
for label, pattern in patterns.items():
    valid, invalid = extract_matches(pattern, text)
    print(f"\n=== {label.upper()} ===")
    print(f"Valid matches ({len(valid)}): {valid}")
    print(f"Potential invalid or non-matching: {invalid}")