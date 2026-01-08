import json


class Account:
    def __init__(self, acc_id, balance):
        self.acc_id = acc_id
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount

    def to_dict(self):
        return {"acc_id": self.acc_id, "balance": self.balance}


def load_accounts(filename):
    accounts = {}
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        for item in data:
            acc = Account(item["acc_id"], item["balance"])
            accounts[acc.acc_id] = acc
    return accounts


def process_transactions(accounts, filename, log_filename):
    with open(filename, "r", encoding="utf-8") as file, open(
        log_filename, "w", encoding="utf-8"
    ) as log_file:
        for line in file:
            from_acc_id, to_acc_id, amount_str = line.strip().split(",")
            amount = float(amount_str)
            from_acc = accounts.get(from_acc_id)
            to_acc = accounts.get(to_acc_id)
            if from_acc and to_acc:
                if from_acc.withdraw(amount):
                    to_acc.deposit(amount)
                    log_file.write(
                        f"[SUCCESS] {from_acc_id} transferred {amount} to {to_acc_id}.\n"
                    )
                else:
                    log_file.write(
                        f"[FAILED] {from_acc_id} failed to transfer {amount} to {to_acc_id} (Insufficient balance).\n"
                    )


def save_accounts(accounts, filename):
    data = [acc.to_dict() for acc in accounts.values()]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    accounts = load_accounts("accounts.json")
    process_transactions(accounts, "transactions.txt", "log.txt")
    save_accounts(accounts, "accounts_updated.json")
