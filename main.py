import lxml.html as lx
import requests
from bs4 import BeautifulSoup as bs

username = ''
password = ''
problems = {}

with requests.session() as s:
    def main():
        # Ask for input and get user's page
        global username, password
        username = input('CodeChef Username: ')
        password = input('CodeChef Password: ')
        # Login to https://www.codechef.com (Credits: https://brennan.io/2016/03/02/logging-in-with-requests/)
        try:
            login = s.get('https://www.codechef.com/')
            login_html = lx.fromstring(login.text)
            hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
            form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
            form['name'] = username
            form['pass'] = password
            response = s.post('https://www.codechef.com/', data=form)
            if response.url == 'https://www.codechef.com/node':
                print('Logged in!')
            elif response.url == 'https://www.codechef.com/session/limit':
                print('Session limit reached! Logout of all active sessions before continuing!')
            else:
                print('Login failed!')
        except:
            print('Some error occurred!')


    def get_problems():
        len_username = len(username)
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
