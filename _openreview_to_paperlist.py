#!/usr/bin/env python3

import argparse
import collections
import csv
import os
import shutil
import sys
import urllib.request
import yaml

def key_accessor(k):
	def get_item(d):
		return d[k]
	return get_item

def cleanup_authors(d):
	return ", ".join(d["authors"].split("|"))

def get_paperhash(d):
	return d["paperhash"].replace("|", "-") + ".pdf"

FIELD_NAMES = {
	"title": key_accessor("title"),
	"authors": cleanup_authors,
	"tldr": key_accessor("TL;DR"),
	"abstract": key_accessor("abstract"),
	"decision": key_accessor("decision"),
	"pdf": key_accessor("pdf"),
	"pdf_file": get_paperhash
}
	


def load_data(f):
	reader = csv.DictReader(f)
	return [ { name: value(line) for name, value in FIELD_NAMES.items()} 
		for line in reader
		if line["decision"] != "Reject"]

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Scrape papers from openreview")
	parser.add_argument("input_file", default=sys.stdin, nargs="?", help="File to read data from")
	parser.add_argument("output_file", default=sys.stdout, nargs="?", help="File to write to")
	parser.add_argument("--pdf-dir", help="Directory to import pdfs to")
	args = parser.parse_args()

	if args.input_file is sys.stdin:
		data = load_data(args.input_file)
	else:
		with open(args.input_file, 'r') as f:
			data = load_data(f)

	if args.pdf_dir is not None:
		for d in data:
			url = f"https://openreview.net{d['pdf']}" 
			outfile = os.path.join(args.pdf_dir, d['pdf_file'])
			with urllib.request.urlopen(url) as response, open(outfile, 'wb') as out_file:
				shutil.copyfileobj(response, out_file)
			del d['pdf']

	if args.output_file is not sys.stdout:
		args.output_file = open(args.output_file, "w")

	yaml.safe_dump(sorted(data, key=lambda d: d["title"]), args.output_file, sort_keys=False)


