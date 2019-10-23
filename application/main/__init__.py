from flask import Blueprint, render_template

# Blueprint Configure
main_blueprint = Blueprint(
    'main', __name__, template_folder='templates')


@main_blueprint.route('/', methods=['GET'])
def index():
    """ Token Count page Route """
    return render_template('main/tokenizer.html', title='Token Count')

@main_blueprint.route('/crawling', methods=['GET'])
def crawling():
    """ Crawling page Route """
    return render_template('main/crawling.html', title='Crawling')

@main_blueprint.route('/kmeans', methods=['GET'])
def kmeans():
    """ K-Means pasge Route """
    return render_template('main/kmeans.html', title='Kmeans')
    