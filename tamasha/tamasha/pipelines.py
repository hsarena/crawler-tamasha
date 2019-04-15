from sqlalchemy.orm import sessionmaker
from tamasha.models import TamashaDB, db_connect, create_table
from datetime import  datetime

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
        now = datetime.now()
        formated_date = now.strftime('%Y-%m-%d %H:%M:%S')
        tamashadb.category = item['category']
        tamashadb.title = item['title']
        tamashadb.link = item['link']
        tamashadb.date_added = item['date_added']
        tamashadb.publisher = item['publisher']
        tamashadb.publisher_logo = item['publisher_logo']
        tamashadb.description = item['description']
        tamashadb.tags = item['tags']
        tamashadb.thumbnail = item['thumbnail']
        tamashadb.url = item['url']
        tamashadb.qr = item['qr']
        tamashadb.embed = item['embed']
        tamashadb.created_date = formated_date

        try:
            session.add(tamashadb)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item