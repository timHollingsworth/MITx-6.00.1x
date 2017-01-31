list_words = ['<a href="http://url.com/{}">{}</a>'.format(a,a) for item in l for a in item.split(' ')]
print(list_words)
