# Email Information Checker

The Email Information Script is a Python tool designed to provide detailed information about an email address. This script checks the validity of an email address, retrieves domain-related details, and performs advanced validations such as DNS MX record checks and SMTP server reachability.

# Features

- **Email Format Validation**: Checks if the email address follows standard formatting rules.
- **MX Records Lookup**: Retrieves Mail Exchange (MX) records for the domain of the email address.
- **IP Address Resolution**: Resolves the IP address associated with the domain.
- **Email Validity Check**: Validates the email address using multiple checks including DNS and SMTP verification.
- **Colorful Output**: Uses color-coded output to enhance readability of the results.

# Installation

To use this script, ensure you have the following Python packages installed:
```sh
pip install dnspython validate-email-address colorama
```

# Usage

Run the script from the command line with the email address as a command-line argument:
```sh
python email_info.py example@example.com
```
Replace **example@example.com** with the email address you want to check.

# Example Output

```yaml
=========================================================
[⁓] email: example@example.com
[⁓] user: example
[⁓] domain: example.com
[⁓] mx_records: ['mx.example.com.']
[⁓] ip_address: 93.184.216.34
[⁓] valid: True
[⁓] mx_validation: True
[⁓] smtp_check: True
=========================================================
```

# Contributing

Contributions are welcome! Please open an **issue** or submit a **pull request** if you have suggestions or improvements.
