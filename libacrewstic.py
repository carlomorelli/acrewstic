from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

engine = create_engine('sqlite:///:memory:', echo=False)


class Store:

    def __init__(self):
        Task.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_item(self, index):
        query = self.session.query(Task).filter(Task.id == index).all()
        assert len(query) == 1
        return query[0].dumps()

    def fetch_all(self):
        query = self.session.query(Task).all()
        return [item.dumps() for item in query]

    def delete(self, index):
        query = self.session.query(Task).filter(Task.id == index).all()
        assert len(query) == 1
        self.session.delete(query[0])
        self.session.commit()
        query = self.session.query(Task).filter(Task.id == index).all()
        assert len(query) == 0

    def append_item(self, json_item):
        task = Task.loads(json_item)
        print "decoded: %s" % task
        self.session.add(task)
        self.session.commit()


class User(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return '<User(name=%s, fullname=%s, password=%s)>' % (self.name,
                                                              self.fullname,
                                                              self.password)


class Task(Base):

    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    done = Column(Boolean)

    def __repr__(self):
        return '<Task(title=%s, description=%s, done=%s)>' % (self.title,
                                                              self.description,
                                                              self.done)

    @staticmethod
    def loads(json_item):
        d = json.loads(json_item)
        assert 'title' in d
        assert 'description' in d
        assert 'done' in d
        return Task(title=d['title'], description=d['description'], done=d['done'])

    def dumps(self):
        d = {
            'title': self.title,
            'description': self.description,
            'done': self.done
        }
        return json.dumps(d)

if __name__ == "__main__":
    User.metadata.create_all(engine)
    Task.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    task1 = Task(title='i dont know',
                 description='various descriptions',
                 done=False)
    task2 = Task(title='i still dont know',
                 description='yada yada',
                 done=False)

    session.add_all([task1, task2])
    session.commit()

    query = session.query(Task).all()
    print "found %s items in db" % len(query)

    query = session.query(Task).filter(Task.title.in_(['i dont know', 'this i know'])).all()
    print "found %s items with specific title in db" % len(query)

    print task1 in session
    print task2 in session

    session.delete(task2)
    print "before commit task2 deletion"
    print task1 in session
    print task2 in session

    session.commit()
    print "after commit task2 deletion"
    print task1 in session
    print task2 in session
