import json

def main():
    google_play_json = open('data/google_play.json')
    google_play_data = json.load(google_play_json)

    data = []

    for item in google_play_data:
        datum = {}

        purchase_history = item['purchaseHistory']

        invoice_price = purchase_history['invoicePrice']
        if len(invoice_price) > 0:
            datum['cost'] = float(invoice_price.split('$')[1])
        else:
            datum['cost'] = 0

        purchase_time = purchase_history['purchaseTime']
        datum['date'] = purchase_time.split('T')[0]

        datum['full_title'] = purchase_history['doc']['title']

        title = purchase_history['doc']['title']
        if '(' in title and ')' in title:
            title = title.split('(')[1].split(')')[0]

        datum['title'] = title
        
        data.append(datum)

        print(datum)
        print('\n')


if __name__ == '__main__':
    main()
