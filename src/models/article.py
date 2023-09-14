from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.config.database import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(500), nullable=True)
    author = Column(String(50), nullable=True)
    title = Column(String(500), nullable=True)
    url = Column(String(50), nullable=True)
    urlToImage = Column(String(50), nullable=True)
    publishedAt = Column(String(50), nullable=True)
    source = Column(String(50), nullable=True)

    __table_args__ = (UniqueConstraint("title", "author", name="_title_author_uc"),)

    def __init__(
        self,
        nickname: str,
        author: str,
        title: str,
        url: str,
        urlToImage: str,
        publishedAt: str,
        source: str,
    ):
        self.nickname = nickname
        self.author = author
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.source = source

    def __repr__(self):
        """
        Returns string representation of Article object
        """
        return f"""
        Article(
            id={self.id},
            nickname={self.nickname},
            author={self.author},
            title={self.title},
            url={self.url},
            urlToImage={self.urlToImage},
            publishedAt={self.publishedAt},
            source={self.source},
        )
        """
