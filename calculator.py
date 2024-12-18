class FinancialCalculator:
    def __init__(self):
        self.transactions = [] 
        self.balance = 0        

    def add_income(self, amount, description="Доход"):
        if amount <= 0:
            raise ValueError("Сумма дохода должна быть положительной!")
        self.transactions.append({"type": "доход", "amount": amount, "description": description})
        self.balance += amount
        return f"Доход на сумму {amount} руб. успешно добавлен!"

    def add_expense(self, amount, description="Расход"):
        if amount <= 0:
            raise ValueError("Сумма расхода должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств для добавления расхода.")
        self.transactions.append({"type": "расход", "amount": amount, "description": description})
        self.balance -= amount
        return f"Расход на сумму {amount} руб. успешно добавлен!"

    def get_balance(self):
        return f"Текущий баланс: {self.balance} руб."

    def get_transactions(self):
        result = "Список всех транзакций:\n"
        for transaction in self.transactions:
            result += f"- {transaction['type'].capitalize()}: {transaction['amount']} руб. ({transaction['description']})\n"
        return result 

    def get_transactions_as_list(self): 
        return self.transactions
