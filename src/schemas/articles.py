from typing import List, Optional

from pydantic import BaseModel


class ArticleSchema(BaseModel):
    """
    Defines the schema of an newly created Article
    """

    author: Optional[str] = "Unknown"
    nickname: Optional[str] = "Unknown"
    title: Optional[str] = "Article Title"
    description: Optional[str] = "Article Description"
    url: Optional[str] = "Article URL"
    urlToImage: Optional[str] = "Article URL to Image"
    publishedAt: Optional[str] = "Article Published At"
    content: Optional[str] = "Article Content"
    source_id: Optional[str] = "Article Source ID"
    source_name: Optional[str] = "Article Source Name"


class ArticleViewSchema(BaseModel):
    """
    Defines the schema of an Article to be inserted into the database
    """

    author: Optional[str] = "Unknown"
    nickname: Optional[str] = "Unknown"
    title: Optional[str] = "Article Title"
    description: Optional[str] = "Article Description"
    url: Optional[str] = "Article URL"
    urlToImage: Optional[str] = "Article URL to Image"
    publishedAt: Optional[str] = "Article Published At"
    content: Optional[str] = "Article Content"
    source_id: Optional[str] = "Article Source ID"
    source_name: Optional[str] = "Article Source Name"


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

    source_name: str = "Unknown"


class ArticleSearchByIdSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by id
    """

    id: int = "Unknown"


class ArticleSearchByNicknameSchema(BaseModel):
    """
    Defines the schema of an Article to be searched by nickname
    """

    nickname: str = "Unknown"


class ArticleUpdateNicknameSchema(BaseModel):
    """
    Defines the schema of an Article to have its nickname updated
    """


class ArticleDeleteResponseSchema(BaseModel):
    """
    Defines the schema of an Article to be deleted by id
    """

    message: str = "Article Deleted Successfully"
    id: int = "Unknown"


class ArticleListSchema(BaseModel):
    """
    Defines the schema of a list of articles
    """

    articles: List[ArticleSchema]
    totalResults: int


def show_articles(articles: List[ArticleSchema]):
    """
    Returns a list of articles
    """
    result = []

    for article in articles:
        result.append(
            {
                "author": article.author,
                "title": article.title,
                "description": article.description,
                "url": article.url,
                "urlToImage": article.urlToImage,
                "publishedAt": article.publishedAt,
                "content": article.content,
                "source_id": article.source_id,
                "source_name": article.source_name,
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
        "author": article.author,
        "title": article.title,
        "description": article.description,
        "url": article.url,
        "urlToImage": article.urlToImage,
        "publishedAt": article.publishedAt,
        "content": article.content,
        "source_id": article.source_id,
        "source_name": article.source_name,
    }
