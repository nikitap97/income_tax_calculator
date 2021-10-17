from flask import Flask, request, jsonify
import pandas as pd
from flask import jsonify
app=Flask(__name__)

def income_tax(income):
    print("income tax calculator function called  ")
    if income <= 250000:  #2 Lakh 50 thousand
        tax = 0
        print("income <= 250000")
    elif 250000<= income <=500000:
        tax = (income) * 0.05
        print("250000<= income <=500000")
    elif income <= 500000: #5 Lakh
        tax = (income - 250000) * 0.1
        print("250000<= income <=500000")
    elif income <= 750000: #7 lakh 50 thousand
        tax = (income - 500000) * 0.10 + 12500
        print("income <= 750000")
    elif income <= 1000000: #10 Lakh
        tax = (income - 750000) * 0.15 + 37500
        print("income <= 1000000")
    elif income <= 1250000: #12 lakh 50 thousand
        tax = (income - 1000000) * 0.20 + 75000
        print("income <= 1250000")
    elif income <= 1500000: #15 lakh
        tax = (income - 1250000) * 0.25 + 125000
        print("income <= 1500000")
    else:
        tax = (income - 1500000) * 0.30 + 187500
        print("income is above 15 lakhs")
    return tax



@app.route("/calc", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        data = request.get_json()

        df= pd.DataFrame(data["data"])

        l = list(df["CREDIT"].values)


        income = sum(l)

        tax1 = income_tax(income)
        print("tax amount is :" ,tax1, "Rupees")
        d = {
        "income" : float(income),
        "Tax" : float(tax1)
        }
        return jsonify(d)



if __name__ == "__main__":
    app.run()
