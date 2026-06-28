import re

def extract_metadata(text: str):

    metadata = {}

    patterns = {
        "scheme_name": r"Scheme Title/Name:\s*(.+)",
        "department": r"Concerned Department:\s*(.+)",
        "beneficiary": r"Beneficiaries:\s*(.+)",
        "benefit_type": r"Types of Benefits:\s*(.+)",
        "funding_pattern": r"Funding Pattern:\s*(.+)"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            text,
            re.MULTILINE
        )

        metadata[key] = (
            match.group(1).strip()
            if match
            else ""
        )

    return metadata