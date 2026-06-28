def format_docs(docs):

    context_parts = []

    for doc in docs:

        context_parts.append(
            f"""
==================================================
SCHEME
==================================================

Scheme Name:
{doc.metadata.get("scheme_name", "Unknown Scheme")}

Department:
{doc.metadata.get("department", "N/A")}

Beneficiary:
{doc.metadata.get("beneficiary", "N/A")}

Benefit Type:
{doc.metadata.get("benefit_type", "N/A")}

Funding Pattern:
{doc.metadata.get("funding_pattern", "N/A")}

Source File:
{doc.metadata.get("source", "N/A")}

Content:
{doc.page_content}
"""
        )

    return "\n".join(context_parts)