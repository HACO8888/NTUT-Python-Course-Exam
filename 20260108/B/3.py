from datetime import date


class Employee:
    def __init__(self, emp_id, name, emp_type):
        self.emp_id = emp_id
        self.name = name
        self.emp_type = emp_type

    def get_details(self):
        kind = "全職" if self.emp_type == "F" else "兼職"
        return f"編號: {self.emp_id} | 姓名: {self.name} | 類別: {kind}"


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, "F")
        self.monthly_salary = float(monthly_salary)

    def calculate_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, work_hours):
        super().__init__(emp_id, name, "P")
        self.hourly_rate = float(hourly_rate)
        self.work_hours = float(work_hours)

    def calculate_pay(self):
        return self.hourly_rate * self.work_hours


def load_staff(path):
    emps = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            if parts[0] == "F" and len(parts) == 4:
                emps.append(FullTimeEmployee(parts[1], parts[2], parts[3]))
            elif parts[0] == "P" and len(parts) == 5:
                emps.append(PartTimeEmployee(parts[1], parts[2], parts[3], parts[4]))
    return emps


def money(n):
    return f"{int(round(n)):,}"


def write_payroll(path, emps, year, month):
    lines = []
    lines.append(f"********** {year} 年 {month} 月份薪資轉帳清單 **********")
    total = 0.0
    for e in emps:
        pay = e.calculate_pay()
        total += pay
        lines.append(f"{e.get_details()} | 應領金額: {int(round(pay))}")
    lines.append("--------------------------------------------")
    lines.append(f"總計發放薪資總額：${money(total)}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    today = date.today()
    emps = load_staff("staff.txt")
    write_payroll("payroll.txt", emps, today.year, today.month)


if __name__ == "__main__":
    main()
