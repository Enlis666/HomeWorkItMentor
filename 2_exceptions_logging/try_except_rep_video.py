def main():
    d = {'website': 'google', 'url': 'google.com'}
    try:
        data = d['url']
    except KeyError:
        data = 'https://'
    else:
        data = data.upper()
    print(data)


if __name__ == '__main__':
    main()
