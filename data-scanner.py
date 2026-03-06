import re
with open("data.txt","r") as file:
    text =file.read()
 
email_regex= r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
card_regex=r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b" 
ip_regex=r"\b\d{1,3}(?:\.\d{1,3}){3}\b"

found = False
if re.search(email_regex,text):
    print("Email detected")
    found=True
if re.search(card_regex,text):
    print("Creditcard found")
    found=True
if re.search(ip_regex,text):
    print("IP found")    
    found=True
if not found:
    print("No sentimale data are found")
    found=False    
if found:
    print("⚠️\nWARNING: Sensitive personal data detected!")
    print("According to GDPR(General Data Proctection Regulation) such data should only be processed or shard with authoized persons.")
else:
    print("No sensitive data found.")
