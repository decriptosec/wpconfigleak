# WPConfigLeak

![WPConfigLeak Logo](wpconfigleak.png)

WPConfigLeak is a tool to search for leaked wp-config.php backups on websites.

## Features

- ANSI colors
- Supports list of URLs
- Supports list of URLs received by pipe
- Automatically saves leaked files

## Installation

To install and run WPConfigLeak, simply clone the repository and ensure you have Python installed on your machine.

```bash
git clone https://github.com/decriptosec/wpconfigleak.git
cd wpconfigleak
```

## Usage

Below are some examples of how to use the tool.

### Example 1: Extract from URL

```bash
python wpconfigleak.py -u https://website.com
```

### Example 2: Extract from URL list

```bash
python wpconfigleak.py -uL url_list.txt
```

### Example 3: Extract from URL list pipe

```bash
cat url_list.txt | python wpconfigleak.py
```

## Command-Line Options

```plaintext
  -h, --help            show this help message and exit
  -u URL, --url URL     WordPress website URL.
  -uL URL_LIST, --url-list URL_LIST
                        Website wordlist URL
```

## Contributing

Feel free to fork this repository and submit a pull request for any features, improvements, or bug fixes. We appreciate your contributions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

## Websites

[LinkedIn](https://www.linkedin.com/in/jsvf/)
[DecriptoSec](https://decriptosec.com)
[LinkedIn Page](https://www.linkedin.com/company/decriptosec/)

## Contact

If you have any questions or feedback, reach out at **[support@decriptosec.com](https://discord.gg/BbxSzgKJKt)**.

---

Happy WP-Config Hunting! 🔒✨