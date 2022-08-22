import webbrowser


def open_youtube():
    return webbrowser.open('https://www.youtube.com/')


def search_query(search_obj):
    return webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(search_obj))
