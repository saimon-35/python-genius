raw_survey_inputs = [
    "  ALICE SMITH ",
    " dhaka, BANGLADESH  ",
    "  mLOpS_ENGineer  ",
    "  LIAM,MAYA "
]

sanitized_records = []

# Clean each string using for loop
for item in raw_survey_inputs:

    cleaned_item = item.strip().lower()

    sanitized_records.append(cleaned_item)


# Print both lists
print(f"Raw Input: {raw_survey_inputs}")
print(f"Sanitized Production Input: {sanitized_records}")