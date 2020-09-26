<p align="center">
    <a href="https://github.com/intsights/Braveblock">
        <img src="https://raw.githubusercontent.com/intsights/Braveblock/master/images/logo.png" alt="Logo">
    </a>
    <h3 align="center">
        A fast and easy adblockplus parser and matcher based on adblock-rust package
    </h3>
</p>


![license](https://img.shields.io/badge/MIT-License-blue)
![Python](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8-blue)
![OS](https://img.shields.io/badge/OS-Mac%20%7C%20Linux%20%7C%20Windows-blue)
![Build](https://github.com/intsights/Braveblock/workflows/Build/badge.svg)
[![PyPi](https://img.shields.io/pypi/v/Braveblock.svg)](https://pypi.org/project/Braveblock/)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built With](#built-with)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)


## About The Project

This library is a Python binding to the [adblock-rust](https://github.com/brave/adblock-rust) library that was written by Brave's browser team. The binding uses [pyo3](https://github.com/PyO3/pyo3) to interact with the rust package.


### Built With

* [pyo3](https://github.com/PyO3/pyo3)
* [adblock-rust](https://github.com/brave/adblock-rust)


### Installation

```sh
pip3 install braveblock
```


## Usage

```python
import braveblock


# Initialize the engine loaded with a rules list
# One can download easylist and load its lines into the engine
braveblock.Adblocker(
    rules=[
        "-advertisement-icon.",
        "-advertisement/script.",
    ]
)

# This function checks whether the specified url should be blocked
adblocker.check_network_urls(
    url="http://example.com/-advertisement-icon.",
    source_url="http://example.com/helloworld",
    request_type="image",
)
```


## License

Distributed under the MIT License. See `LICENSE` for more information.


## Contact

Gal Ben David - gal@intsights.com

Project Link: [https://github.com/intsights/Braveblock](https://github.com/intsights/Braveblock)
