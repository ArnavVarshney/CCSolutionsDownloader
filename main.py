import bs4 as bs
import requests

username = input('CodeChef Username: ')
len_username = len(username)

r = requests.get('https://www.codechef.com/users/' + username)

data = r.text

soup = bs.BeautifulSoup(data, 'html5lib')

problems = {'PRACTICE': []}

for link in soup.find_all('a'):
    x = str(link.get('href'))
    if 'status' in x and username in x:
        x = x[:len(x) - len_username - 1]
        ls = x.split('/')
        if len(ls) == 3:
            contest_code = 'PRACTICE'
            problem_code = str(ls[2])
        else:
            contest_code = str(ls[1])
            problem_code = str(ls[3])
        if contest_code not in problems:
            problems[contest_code] = []
        problems[contest_code].append(problem_code)

for i in problems:
    print(str(i) + ': ' + ''.join([str(j) + ', ' for j in problems[i]]))
