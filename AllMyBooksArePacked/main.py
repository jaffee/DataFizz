import os
import amazon_parser
import box
from pprint import pprint

def parse(open_file, things_to_pull):
    data = open_file.read()
    res = {}
    for key,func in things_to_pull.items():
        res[key] = func(data)
    return res

def main():
    results = []
    for filename in os.listdir("data"):
        if filename.endswith(".html"):
            results.append(parse(open("./data/" + filename, 'r'), amazon_parser.things_to_pull))

    pprint(results)
#    print box.box(results)


if __name__ == "__main__":
    main()
