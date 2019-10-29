from bs4 import BeautifulSoup
import http.client
import urllib.parse
from application.main.model import Github


class Crawing(object):
    def __init__(self, app, db):
        super(Crawing, self).__init__()
        self.app = app
        self.db = db

    def searcher(self, keyword, page):
        # github_table이 존재하면 제거 후 크롤링
        if self.db.engine.dialect.has_table(self.db.engine, 'github_table'):
            Github.__table__.drop(self.db.engine)

        Github.__table__.create(self.db.engine)

        conn = http.client.HTTPSConnection("github.com")
        for i in range(1, (page + 1)):
            encode_keyword = str(urllib.parse.urlencode({'q': keyword}))

            url = '/search?utf8=%E2%9C%93&' + encode_keyword + '&ref=simplesearch&p=' + str(i)

            conn.request('GET', url)
            data = conn.getresponse()

            soup = BeautifulSoup(data, 'html.parser')

            print('Github Current Page : ', i)
            repo_list = soup.select('.repo-list-item')
            self.parse(repo_list)

    def parse(self, repo_list):
        repo_info_dic = []
        for repo in repo_list:
            title = repo.select('h3 > a')[0].text
            tool = repo.select_one('span[itemprop=programmingLanguage]')
            star = repo.select_one('div.pl-2 a.muted-link')
            description = repo.select_one('h3 + p')
            tag = repo.select_one('div .topics-row-container')

            repo_info_dic.append({
                'title': title,
                'tool': "" if tool is None else tool.text,
                'star': "0" if star is None else ' '.join(repo.select('div.pl-2 a.muted-link')[0].text.split()),
                'description': "" if description is None else ' '.join(repo.select('h3 + p')[0].text.split()),
                'tag': "" if tag is None else ','.join(' '.join(tag.text.split()).split())
            })

        for repo in repo_info_dic:
            github = Github(
                title=repo['title'],
                tool=repo['tool'],
                star=repo['star'],
                description=repo['description'],
                tag=repo['tag'])

            self.db.session.add(github)
            self.db.session.commit()
