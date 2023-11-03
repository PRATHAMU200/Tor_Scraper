# Tor Scraper

## Overview

Tor Scraper is a Python-based web scraping tool that checks the availability of .onion links using the Tor network. It allows you to quickly identify whether a given .onion link is up or down, making it useful for monitoring the status of hidden services on the Tor network.

## Features

- Check the availability of .onion links.
- Utilize the Tor network for anonymous scraping.
- Multi-threaded for efficiency.
- Retrieve the title of live websites.

## Prerequisites

Before using Tor Scraper, make sure you have the following dependencies installed:

- [Python](https://www.python.org/) (Python 3 recommended)
- [Requests](https://pypi.org/project/requests/) library
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) library
- [Colorama](https://pypi.org/project/colorama/) library

## Usage

### Checking .onion Links

To check the status of .onion links, use the `-F` flag to specify the file containing the links:

```
python OnionStatus.py -F links.txt
```
You can also specify the number of threads to use with the -T flag:
```
python OnionStatus.py -F links.txt -T 20
```
Web Scraping
The scraper.py script allows you to scrape links from a given .onion website and save them to a file. Use the -u flag to specify the website URL and the -o flag to specify the output file:
```
python scraper.py -u http://example.onion -o output.txt
```
