def map_topic_to_irs(topic):
    mapping = {
        "constructive receipt": "IRS Publication 538 – Accounting Periods and Methods",
        "self employment tax": "IRS Publication 334 – Tax Guide for Small Business",
        "social security benefits": "IRS Publication 915 – Social Security Benefits",
        "qualified dividends": "IRS Publication 550 – Investment Income and Expenses",
        "qbi deduction": "IRS Publication 535 – Business Expenses"
    }

    for key in mapping:
        if key in topic.lower():
            return mapping[key]

    return "Refer to IRS Publication 17 – Your Federal Income Tax"
