from datetime import datetime
import re

with open('/home/Desktop/Downloads/RedNotebook-Export_allentries.txt', 'r') as f:
    text = f.read()
text = text.replace('dimanche, ', '').replace('lundi, ', '').replace('mardi, ', '').replace('mercredi, ', '').replace('jeudi, ', '').replace('vendredi, ', '').replace('samedi, ', '')
def convert_date(match):
    date_str = match.group(0)  # Get the matched date-like string
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')  # Convert to datetime object
    return date_obj.strftime('%Y/%m/%d')  # Format the date and return

pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'  # setting split pattern
modified_string = re.sub(pattern, convert_date, text)
split_pattern = '\n\n\s\s'
new_text = re.split(split_pattern, modified_string)   # splitting daily entries into individual files
for i in new_text:
    name = i.split('\n\n\s\s')
    form_name = name[0].replace('\n', '').replace(',', '').replace('/', '-')
    form_name = form_name[1:11]
    print(form_name)
    with open(f'/home/omd/Python/output_files/diary_import/{form_name}.md', 'a+') as f:
        f.write(i)

