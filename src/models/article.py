from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.config.database import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), nullable=True)
    author = Column(String(50), nullable=True)
    title = Column(String(50), nullable=True)
    description = Column(String(50), nullable=True)
    url = Column(String(50), nullable=True)
    urlToImage = Column(String(50), nullable=True)
    publishedAt = Column(String(50), nullable=True)
    content = Column(String(50), nullable=True)
    source_id = Column(String(50), nullable=True)
    source_name = Column(String(50), nullable=True)

    __table_args__ = (UniqueConstraint("title", "author", name="_title_author_uc"),)

    def __init__(
        self,
        nickname: str,
        author: str,
        title: str,
        description: str,
        url: str,
        urlToImage: str,
        publishedAt: str,
        content: str,
        source_id: str,
        source_name: str,
    ):
        self.nickname = nickname
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        self.source_id = source_id
        self.source_name = source_name

    def __repr__(self):
        """
        Returns string representation of Article object
        """
        return f"(Article {self.title} by {self.author})"
