import csv
from datetime import date


class Product:
    def __init__(self, p_id, name, stock, min_val):
        self.p_id = p_id
        self.p_name = name
        self.current_stock = int(stock)
        self.min_required = int(min_val)

    def needs_restock(self):
        return self.current_stock < self.min_required

    def get_shortage(self):
        return self.min_required - self.current_stock

    def update_stock(self, amount):
        self.current_stock += int(amount)


def load_inventory(path):
    products = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.reader(f)
        next(r, None)
        for row in r:
            if len(row) < 4:
                continue
            products.append(
                Product(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip())
            )
    return products


def build_restock_list(products):
    return [p for p in products if p.needs_restock()]


def write_report(path, items):
    lines = []
    lines.append("********** 採購建議清單 **********")
    lines.append(f"日期：{date.today().isoformat()}")
    lines.append("--------------------------------")
    for i, p in enumerate(items, 1):
        lines.append(f"{i}. [{p.p_id}] {p.p_name}")
        lines.append(f" - 當前庫存：{p.current_stock}")
        lines.append(f" - 建議採購數量：{p.get_shortage()}")
    lines.append("--------------------------------")
    lines.append(f"總計需補貨項目：{len(items)} 項")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    all_products = load_inventory("inventory.csv")
    to_buy = build_restock_list(all_products)
    write_report("restock_order.txt", to_buy)


if __name__ == "__main__":
    main()
