# Domain Availability Checker

This project is a Python-based tool to check the availability of domain names using the `python-whois` library.

## Features

- Checks the availability of domain names.
- Supports multiple domain names and TLDs.
- Uses multithreading for faster processing.

## Requirements

The project requires the following Python packages, as specified in `requirements.txt`:

- astroid==3.3.9
- colorama==0.4.6
- dill==0.4.0
- isort==6.0.1
- mccabe==0.7.0
- platformdirs==4.3.7
- pylint==3.3.6
- python-dateutil==2.9.0.post0
- python-whois==0.9.5
- six==1.17.0
- tomlkit==0.13.2

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using:

```bash
python main.py
```

### Customization

- **Domain List**: Modify the `domain_list` variable in `main.py` to include your desired domain names.
- **TLDs**: Modify the `tlds` variable in `main.py` to include your desired top-level domains.

## Example Output

```plaintext
mobix.com: AVAILABLE
zypix.com: NOT AVAILABLE
...
```

## License

This project is licensed under the MIT License.
