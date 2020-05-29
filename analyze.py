import json

GOOGLE_PLAY_JSON = 'data/google_play.json'

def main():
    print('Analysing file: \'%s\'...' % GOOGLE_PLAY_JSON)

    google_play_json = open(GOOGLE_PLAY_JSON)
    google_play_data = json.load(google_play_json)

    purchase_titles = {}

    for item in google_play_data:
        title = item['purchaseHistory']['doc']['title']
        if '(' in title and ')' in title:
            title = title.split('(')[1].split(')')[0]

        purchase_titles

    print('\tFound %d unique Purchase Titles:')
    for

if __name__ == "__main__":
    main()
