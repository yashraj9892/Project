import google
num_page = 3
search_results = google.search("index of serial the flash", num_page)
print(search_results.link)
