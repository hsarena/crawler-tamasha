from sqlalchemy.orm import sessionmaker
from tamasha.models import TamashaDB, db_connect, create_table

class TamashaPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        tamashadb = TamashaDB()
        tamashadb.category = item['category']
        tamashadb.title = item['title']
        tamashadb.link = item['link']
        tamashadb.date_added = item['date_added']
        tamashadb.publisher = item['publisher']
        tamashadb.publisher_logo = item['publisher_logo']
        tamashadb.description = item['description']
        tamashadb.tags = item['tags']
        tamashadb.thumbnail = item['thumbnail']

        try:
            session.add(tamashadb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item