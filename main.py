import requests
from bs4 import BeautifulSoup as bs

username = ''
password = ''
problems = {}
len_username = len(username)


def main():
    # Ask for input and get user's page
    global username, password
    username = input('CodeChef Username: ')
    password = input('CodeChef Password: ')

    try:
        s = requests.Session()
        payload = {'name': username, 'pass': password, 'form_id': 'new_login_form', 'op': 'Login',
                   'form_build_id': bs.find('input', attrs={'name': 'form_build_id'})['value']}
        r = s.post('https://www.codechef.com/', data=payload)
    except:
        print('Login Failed!')


def get_problems():
    r = requests.get('https://www.codechef.com/users/' + username)
    data = r.text
    soup = bs(data, 'html5lib')
    # Classify all problems according to their contests
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
            if contest_code not in problems.keys():
                problems[contest_code] = []
            problems[contest_code].append(problem_code)
    # for i in problems:
    #    print(str(i) + ': ' + ''.join([str(j) + ', ' for j in problems[i]]))


def extract_solutions():
    # Extract solutions
    for i in problems:
        for j in problems[i]:
            r = requests.get('https://www.codechef.com/' + i + '/status/' + j + ',' + username)
            data = r.text
            soup = bs(data, 'html5lib')


if __name__ == "__main__":
    main()
