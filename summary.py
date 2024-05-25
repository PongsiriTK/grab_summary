import pypdf as pdf


pdf_file = 'grab2023.pdf'
pdf_reader = pdf.PdfReader(pdf_file)

total_value = 0

for page in pdf_reader.pages:
    page_value = page.extract_text()
    text_array = page_value.split()
    text_array = [word.strip() for word in text_array]

    index = 62
    while index < len(text_array):
        value = text_array[index].replace(',', '')
        try:
            value = float(value)
            if value > 0:
                total_value += value
                print(value)
                break
        except ValueError:
            pass
        index += 1


print(total_value)
print(len(pdf_reader.pages))

