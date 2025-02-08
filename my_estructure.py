class UniqueNumbers:
    def __init__(self):
        self.numbers = set()  # Usamos um conjunto para armazenar os números

    def add_number(self, number):
        if self.is_duplicate(number):
            return False  # Número repetido
        else:
            self.numbers.add(number)
            return True  # Número inédito

    def is_duplicate(self, number):
        return number in self.numbers  # Verificação manual (poderia ser implementada sem usar "in")