import __init__
from views.view import subscribers_view
from models.database import engine
from models.model import Subscribers
from datetime import datetime
from decimal import Decimal

class UI:
    def __init__(self):
        self.subscribers_service = subscribers_view(engine)

    def add_subscription(self):
        empresa = input('Empresa: ')
        site = input('Site: ')
        data_assinatura = datetime.strptime(input('Data de assinatura: '), '%d/%m/%Y')
        valor = Decimal(input('Valor: '))
        subscribers = Subscribers(empresa=empresa, site=site, data_assinatura=data_assinatura, valor=valor)
        self.subscribers_service.create(subscribers)  # Corrigido: passando a instância do subscriber
        print('Assinatura adicionada com sucesso.')

    def delete_subscription(self):
        subscribers = self.subscribers_service.list_all()  # Corrigido: usar subscribers_service
        print('Escolha qual assinatura deseja excluir:')
        for i in subscribers:
            print(f'[{i.id}] -> {i.empresa}')
        choice = int(input('Escolha a assinatura (ID): '))
        self.subscribers_service.delete(choice)  # Corrigido: passando o ID da assinatura para deletar
        print('Assinatura excluída com sucesso.')

    def total_value(self):
        total = self.subscribers_service.total_value()  # Corrigido: chamada para total_value
        print(f'Seu valor total mensal em assinaturas: {total}')

    def start(self):
        while True:
            print(''' 
            [1] -> Adicionar assinatura
            [2] -> Remover assinatura
            [3] -> Valor total
            [4] -> Gastos últimos 12 meses
            [5] -> Sair
            ''')
            choice = int(input('Escolha uma opção: '))
            if choice == 1:
                self.add_subscription()
            elif choice == 2:
                self.delete_subscription()
            elif choice == 3:
                self.total_value()
            elif choice == 4:
                self.subscribers_service.gen_chart()  # Corrigido: chamar gen_chart da subscribers_service
            else:
                break


if __name__ == '__main__':
    UI().start()
