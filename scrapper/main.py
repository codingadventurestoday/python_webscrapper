import sys 

from helper.crawl import get_html

def main():
    length = len(sys.argv)
    if length < 2:
        print('no website provided')
        sys.exit(1)
    elif length > 2:
        print('too many arguments provided')
        sys.exit(1)
    else:
        BASE_URL = sys.argv[1]
        print(f'starting crawl of: {BASE_URL}')
        print(get_html(BASE_URL))

if __name__ == "__main__":
    main()
