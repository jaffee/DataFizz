import os
import amazon_parser
import box


def parse(open_file, things_to_pull):
    data = open_file.read()
    res = {}
    for key,func in things_to_pull.items():
        res[key] = func(data)

def main():
    results = []
    for filename in os.listdir("data"):
        if filename.endswith(".html"):
            results.append(parse(open(filename, 'r'), amazon_parser.things_to_pull))


    print box.box(results)
