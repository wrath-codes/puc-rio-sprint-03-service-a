# flake8: noqa F405, F841
from flask import redirect, request
from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI, Tag
from sqlalchemy.exc import IntegrityError

from src.config.database import DBConnectionHandler, create_db
from src.models import Article
from src.schemas import *

# Defines API Info
info = Info(
    title="My Articles API",
    version="1.0.0",
    description="A simple API to manage articles served by NewsAPI",
)

# Setup app and API
app = OpenAPI(
    __name__,
    info=info,
)


# Setup CORS
CORS(app)

# Define API Tags
home_tag = Tag(name="Home", description="Go to API Documentation Style Selector")
articles_tag = Tag(name="Articles", description="Articles API")


@app.get("/", tags=[home_tag])
def home():
    """
    Redirects to API Documentation OpenAPI3
    """

    return redirect("/openapi")


@app.post(
    "/articles",
    tags=[articles_tag],
    description="Adds an article to the database",
    responses={
        "201": ArticleViewSchema,
        "409": ErrorSchema,
        "400": ErrorSchema,
    },
)
def add_article():
    """
    Adds an article to the database
    """
    form = request.get_json()
    newArticle = Article(
        nickname=form.get("nickname"),
        author=form.get("author"),
        title=form.get("title"),
        url=form.get("url"),
        urlToImage=form.get("urlToImage"),
        publishedAt=form.get("publishedAt"),
        source=form.get("source"),
    )

    try:
        with DBConnectionHandler() as db_conn:
            exists = (
                db_conn.session.query(Article).filter_by(url=newArticle.url).first()
            )

            if exists:
                return {"message": "Article already exists"}, 409
            db_conn.session.add(newArticle)
            db_conn.session.commit()
            db_conn.session.refresh(newArticle)

            return show_article(newArticle), 201

    except IntegrityError as e:
        db_conn.session.rollback()
        return {"message": "Article already exists"}, 409

    except Exception as e:
        db_conn.session.rollback()
        return {"message": "Something went wrong"}, 400

    finally:
        db_conn.session.close()


@app.get(
    "/articles",
    tags=[articles_tag],
    description="Returns all articles from the database",
    responses={
        "200": ArticleListSchema,
        "404": ErrorSchema,
    },
)
def get_articles():
    """
    Returns all articles from the database
    """
    with DBConnectionHandler() as db_conn:
        articles = db_conn.session.query(Article).all()

        if not articles:
            return {"articles": [], "totalResults": 0}, 200

        return show_articles(articles), 200


@app.get(
    "/articles/",
    tags=[articles_tag],
    description="Returns a single article from the database",
    responses={
        "200": ArticleViewSchema,
        "404": ErrorSchema,
    },
)
def get_article(query: ArticleSearchByIdSchema):
    """
    Returns a single article from the database
    """
    with DBConnectionHandler() as db_conn:
        article = db_conn.session.query(Article).filter_by(id=query.id).first()

        if not article:
            return {"message": "Article not found"}, 404

        return show_article(article), 200


@app.delete(
    "/articles/",
    tags=[articles_tag],
    description="Deletes a single article from the database",
    responses={
        "200": ArticleDeleteResponseSchema,
        "404": ErrorSchema,
    },
)
def delete_article():
    """
    Deletes a single article from the database
    """
    deleted_id = request.get_json().get("id")
    with DBConnectionHandler() as db_conn:
        article = db_conn.session.query(Article).filter_by(id=deleted_id).first()
        deleted_id = article.id
        if not article:
            return {"message": "Article not found"}, 404

        db_conn.session.delete(article)
        db_conn.session.commit()

        return {"message": "Article Deleted Successfully", "id": deleted_id}, 200


@app.put(
    "/articles/",
    tags=[articles_tag],
    description="Updates the nickname of an article in the database",
    responses={
        "200": ArticleViewSchema,
        "404": ErrorSchema,
    },
)
def update_article_nickname():
    """
    Updates the nickname of an article in the database
    """
    form = request.get_json()
    article_id = form.get("id")
    nickname = form.get("nickname")
    with DBConnectionHandler() as db_conn:
        article = db_conn.session.query(Article).filter_by(id=article_id).first()

        if not article:
            return {"message": "Article not found"}, 404

        article.nickname = nickname
        db_conn.session.commit()
        db_conn.session.refresh(article)

        return show_article(article), 200


if __name__ == "__main__":
    with app.app_context():
        # Create database if it does not exist
        print("Setting up database...")
        create_db()
        print("Database setup completed...")
        print("Starting API server...")
        app.run(debug=True, host="0.0.0.0", port=4200, use_reloader=True)
