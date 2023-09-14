from typing import List, Optional

from pydantic import BaseModel


class ArticleSchema(BaseModel):
    """
    Defines the schema of an newly created Article
    """

    id: Optional[int] = 1
    author: Optional[str] = "Unknown"
    nickname: Optional[str] = "Unknown"
    title: Optional[str] = "Article Title"
    url: Optional[str] = "Article URL"
    urlToImage: Optional[str] = "Article URL to Image"
    publishedAt: Optional[str] = "Article Published At"
    source: Optional[str] = "Article Source Name"


class ArticleViewSchema(BaseModel):
    """
    Defines the schema of an Article to be inserted into the database
    """

    author: Optional[str] = "Unknown"
    nickname: Optional[str] = "Unknown"
    title: Optional[str] = "Article Title"
    url: Optional[str] = "Article URL"
    urlToImage: Optional[str] = "Article URL to Image"
    publishedAt: Optional[str] = "Article Published At"
    source: Optional[str] = "Article Source Name"


class ArticleSearchByAuthorSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by author
    """

    author: str = "Unknown"


class ArticleSearchByTitleSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by title
    """

    title: str = "Unknown"


class ArticleSearchBySourceSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by source
    """

    source: str = "Unknown"


class ArticleSearchByIdSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by id
    """

    id: int = 1


class ArticleSearchByNicknameSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by nickname
    """

    nickname: str = "Unknown"


class ArticleUpdateNicknameSchema(BaseModel):
    """
    Defines the schema of an Article to have its nickname updated
    """

    id: int = 1
    nickname: str = "Unknown Nickname"


class ArticleDeleteResponseSchema(BaseModel):
    """
    Defines the schema of an Article to be deleted by id
    """

    message: str = "Article Deleted Successfully"
    id: int = 1


class ArticleListSchema(BaseModel):
    """
    Defines the schema of a list of articles
    """

    articles: List[ArticleSchema]
    totalResults: int


class ArticleCheckExistsSchema(BaseModel):
    """
    Defines the schema of an existence of articles
    """

    url: str = "Article URL"


def show_articles(articles: List[ArticleSchema]):
    """
    Returns a list of articles
    """
    result = []

    for article in articles:
        result.append(
            {
                "id": article.id,
                "author": article.author,
                "title": article.title,
                "url": article.url,
                "urlToImage": article.urlToImage,
                "publishedAt": article.publishedAt,
                "source": article.source,
                "nickname": article.nickname,
            }
        )

    return {
        "articles": result,
        "totalResults": len(result),
    }


def show_article(article: ArticleSchema):
    """
    Returns a single article
    """
    return {
        "id": article.id,
        "author": article.author,
        "title": article.title,
        "url": article.url,
        "urlToImage": article.urlToImage,
        "publishedAt": article.publishedAt,
        "source": article.source,
        "nickname": article.nickname,
    }
