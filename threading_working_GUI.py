import requests
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import schedule
import PySimpleGUI as Sg
import threading


def check_forum():
    url = 'https://forums.eveonline.com/c/marketplace/sales-ads/'
    try:
        r = requests.get(url)
        open('forum.html', 'wb').write(r.content)
        r.raise_for_status()
    except HTTPError as hp:
        print(hp)


def write_topics(filename, html_file):
    state_1 = open(filename, 'r').read()
    with open(html_file) as f:
        src = f.read()
        soup = BeautifulSoup(src, 'lxml')
        topic_names = soup.find_all('a', class_='title raw-link raw-topic-link')
    with open(filename, 'w') as file:
        for item in topic_names:
            item_text = item.text
            item_url = item.get('href')
            print(f"{item_text}", file=file)
            print(f"{item_url}",  file=file)
    state_2 = open(filename, 'r').read()
    if state_1 != state_2:
        with open(filename, 'r') as file2:
            file2.readline(), file2.readline()
            print(' Last topic :',   file2.readline())
            print(' Link         :', file2.readline(), '\n')
    else:
        print(' Waiting for new topics...\n ')


def main():
    check_forum()
    write_topics(filename='topics.txt', html_file='forum.html')


def main_on_schedule():
    schedule.every(10).seconds.do(main)
    while True:
        schedule.run_pending()


def the_gui():
    Sg.theme('Sandy Beach')
    layout = [[Sg.Output(size=(80, 15), key='_output_')],
              [Sg.Button('Last topic'), Sg.Button('Follow Sales Ads'), Sg.Button('Stop following')],
              [Sg.Button('Exit')], ]

    window = Sg.Window('Sales Ads', layout=layout, size=(620, 330), resizable=True)

    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Last topic':
            open('topics.txt', 'wb')
            main()
        elif event == 'Follow Sales Ads':
            window['Last topic'].update(disabled=True)
            window['Follow Sales Ads'].update(disabled=True)
            open('topics.txt', 'wb')
            window.FindElement('_output_').Update('')
            print('The program is now working.\n ')
            threading.Thread(target=main_on_schedule).start()
        elif event == 'Stop following':
            window['Follow Sales Ads'].update(disabled=False)
    window.close()


if __name__ == '__main__':
    the_gui()
