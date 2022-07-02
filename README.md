# Password-Leak-Processor
A simple Python script to detect emails for a given domain in a password leak file.

Takes the format username:password, 1 line per user/pass combination. This is the standard setup for most password leak files.

Intended for use by security analysts to detect any credentials for their organisation, with password obfuscation options for support tickets.

## Usage

- To open the script

``` bash
python pw_leak_processor.py [file path]
```

- Keyword should be a part of a domain, or whole domain excluding told.
    - For example, if searching testdomain[.]com, the keyword would be "testdomain"

- Choose if you want to obfuscate password (replace every character except start & end with asterisks (*)
