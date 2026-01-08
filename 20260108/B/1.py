import csv


class Record:
    def __init__(self, date, desc, amount):
        self.date = date
        self.description = desc
        self.amount = float(amount)

    def is_income(self):
        return self.amount > 0

    def is_expense(self):
        return self.amount < 0

    def to_string(self):
        tag = "支出" if self.is_expense() else "收入"
        val = f"{int(self.amount)}" if self.is_income() else f"({int(self.amount)})"
        return f"[{tag}] {self.date}: {self.description} {val}"


def read_ledger(filepath):
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            if len(row) != 3:
                continue
            records.append(Record(row[0].strip(), row[1].strip(), row[2].strip()))
    return records


def summarize(records):
    income_cnt = 0
    expense_cnt = 0
    total_income = 0.0
    total_expense = 0.0
    for rec in records:
        if rec.is_income():
            income_cnt += 1
            total_income += rec.amount
        elif rec.is_expense():
            expense_cnt += 1
            total_expense += -rec.amount
    balance = total_income - total_expense
    return income_cnt, expense_cnt, total_income, total_expense, balance


def money(n):
    return f"${int(round(n)):,}"


def write_summary(filepath, stats):
    income_cnt, expense_cnt, total_income, total_expense, balance = stats
    status = "財務狀況良好" if balance > 0 else "財務需注意"
    lines = [
        "=== 個人財務彙整報告 ===",
        f"總收入筆數：{income_cnt}",
        f"總支出筆數：{expense_cnt}",
        "-----------------------",
        f"總收入金額：{money(total_income)}",
        f"總支出金額：{money(total_expense)}",
        f"最終結餘：{money(balance)}",
        "=======================",
        f"狀態：{status}",
    ]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    records = read_ledger("ledger.csv")
    stats = summarize(records)
    write_summary("summary.txt", stats)


if __name__ == "__main__":
    main()
