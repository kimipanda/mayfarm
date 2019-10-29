def get_repo_all():
    from application.main.model import Github
    return Github.query.all()


def get_repo_filter(search_by, query):
    from application.main.model import Github

    if 'title' in search_by:
        github = Github.query.filter(Github.title.like('%' + query + '%')).all()
    else:
        github = Github.query.filter(Github.tag.like('%' + query + '%')).all()

    return github
