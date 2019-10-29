from flask import Blueprint
from flask import render_template
from flask import request

from application.main.token_utils import noun_frequency_count, word_frequency_count
from application.main.github_utils import get_repo_all, get_repo_filter

# Blueprint Configure
main_blueprint = Blueprint(
    'main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET'])
def index():
    """ Token Count page Route """
    return render_template('main/tokenizer.html', nouns=noun_frequency_count(), words=word_frequency_count())


@main_blueprint.route('/crawling', methods=['GET'])
def github_crawling():
    """ Github Crawling page Route """
    return render_template('main/crawling.html', repo_list=get_repo_all(), search_by='')


@main_blueprint.route('/search', methods=['GET'])
def github_search():
    """ Github Search page Route """
    search_by = request.args.get('searchBy')
    query = request.args.get('query')
    return render_template('main/crawling.html', repo_list=get_repo_filter(search_by, query), search_by=search_by)


@main_blueprint.route('/kmeans', methods=['GET'])
def kmeans():
    """ K-Means pasge Route """
    return render_template('main/kmeans.html')
