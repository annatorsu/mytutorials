has_high_income=True
has_good_credit=False
if has_high_income  and has_good_credit:
    print("eligible for loan")
else:
    print("you are high risk")

    has_high_income=True
has_good_credit=False
if has_high_income  or has_good_credit:
    print("eligible for loan")
else:
    print("you are high risk")