import __init__
from models.database import engine 
from models.model import Subscribers, Payment
from sqlmodel import Session, select
from datetime import date

class subscribers_view:
    def __init__(self, engine):
        self.engine = engine


    def create(self, subscribers: Subscribers):
        with Session(self.engine) as session:
            session.add(subscribers)
            session.commit()
            session.refresh(subscribers)

        return subscribers
    
    def list_all(self):
        with Session(self.engine) as session:
            statement = select(Subscribers)
            results = session.exec(statement).all()
            return results


    def _has_pay(self, results):
        for result in results:
            if result.date.month == date.today().month:
                return True
        return False
    
    def pay(self, subscriber: Subscribers):
        with Session(self.engine) as session:
            statement = select(Payment).join(Subscribers).where(Subscribers.empresa==subscriber.empresa)
            results = session.exec(statement).all()
        if self._has_pay(results):
            question = input('Essa conta já foi paga esse mês, deseja pagar novamente ? Y ou N')
        if not question.upper() == 'Y':
                return

        pay = Payment(subscriber_id=Subscribers.id)
        session.add(pay)
        session.commit()
        
    def payment(self, subscriber: Subscribers):
        with Session(self.engine) as session:
            statement = select(Payment).join(Subscribers).where(Subscribers.empresa==subscriber.empresa)
            results = session.exec(statement).all()
            print(results)


sv = subscribers_view(engine)
#subscribers = Subscribers(empresa="Disney", site="www.Disney.com.br", data_assinatura=date.today(), valor=200.0)
#sv.payment(subscriber)