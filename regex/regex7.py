import re


def get_company_name(email: str):
    email_no_dot = re.sub(r'\.[a-z]+', '', email)
    email_no_at = re.sub(r'[a-z]+@', '', email_no_dot)
    return email_no_at

print(get_company_name('username@companyname.com'))