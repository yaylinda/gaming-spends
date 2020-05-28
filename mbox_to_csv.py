import csv
import mailbox

"""

parser.py

Reads mbox archive from 'all_mail.mbox'.
Dumps relevant message content into 'content.csv' for further processing.

"relevant" meaning, if it's from the App Store or Play Store.

Ignores any exceptions and moves onto next message.

"""


def main():
    csv_file = open('content.csv', 'w')
    csv_writer = csv.writer(csv_file, delimiter=',')

    mbox = mailbox.mbox('all_mail.mbox')

    total = 0
    count = 0
    exceptions = 0

    for message in mbox:

        total = total + 1

        try:
            content = message.as_string()

            if ('no_reply@email.apple.com' in content or 'googleplay-noreply@google.com' in content):   
                count = count + 1
                print('Writing message content #%d' % count)
                csv_writer.writerow([content])
        except:
            exceptions = exceptions + 1
            print('An exception occurred. Skipping to next message...' % exceptions)

    print('Wrote %d messages to content.csv' % count)
    print('Encountered %d exceptions' % exceptions)
    print('Processed %d total messages' % total)


if __name__ == '__main__':
    main()