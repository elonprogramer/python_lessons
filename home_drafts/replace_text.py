import re

text = "Дві подружки, що відправились у дорожню пригоду, змагаються за увагу красунчика застрягши в аеропорту через негоду. Коли їхній літак змінюється через попередження про ураган, дві самотні найкращі подругиMYMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY. NEXT AVAILABLE IN  23 HOURS 00 MINUTES 52 SECONDS VISIT HTTPS://MYMEMORY.TRANSLATED.NET/DOC/USAGELIMITS.PHP TO TRANSLATE MORE Дві подружки, що відправились у дорожню пригоду, змагаються за увагу красунчика застрягши в аеропорту через негоду."
bed_pattern = "MYMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY. NEXT AVAILABLE IN  \d+ HOURS 00 MINUTES \d+ SECONDS VISIT HTTPS://MYMEMORY.TRANSLATED.NET/DOC/USAGELIMITS.PHP TO TRANSLATE MORE"
new_pattern = " "
match = re.search(bed_pattern, text)
result = re.sub(bed_pattern, new_pattern, text)
print(text)
print("-----------------------------------")
print(result)
