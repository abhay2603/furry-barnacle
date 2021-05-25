import pyshorteners as ps

link = 'https://www.linkedin.com/in/abhay-pratap-singh-96b121197'

s= ps.Shortener()

print(s.tinyurl.short(link))