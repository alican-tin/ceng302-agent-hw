TAX_MULTIPLIER = 1.15
DEFAULT_LOG_FILE = "log.txt"


def calculate_total(amount, multiplier=TAX_MULTIPLIER):
    return amount * multiplier


def format_total(value):
    return f"Total: {value:.2f}"


def append_log(values, log_file=DEFAULT_LOG_FILE):
    with open(log_file, "a", encoding="utf-8") as file:
        file.write(f"{values}\n")


def process_data(data, log_file=DEFAULT_LOG_FILE):
    totals = []

    for amount in data:
        total = calculate_total(amount)
        print(format_total(total))
        totals.append(total)

    append_log(totals, log_file=log_file)
    return totals
