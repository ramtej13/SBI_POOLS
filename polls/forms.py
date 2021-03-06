from django import forms
from .models import Contact_form

class Contact_Forms(forms.ModelForm):
    class Meta:
        model = Contact_form
        fields = ["paid_up_capital_1","Reserves_Funds","Reserve_Fund_2","Bills_payable_in_India5","Other_Reserves_2","Share_Premium_Accounts_2","Deposits_3","Current_Deposits_3","From_Banks1","From_Others","Savings_Deposits","Fixed_Deposits_33",
                  "From_Banks331","From_Others332","Savings_Deposits32","Borrowings_4","Borrowings_from_Banks_in_India_4", "Reserve_Bank_of_India_4",
                  "State_Bank_of_India_4","Associates_of_the_State_Bank_of_India_4","Other_Commercial_Bank_4","Co_operative_Banks4","Borrowings_from_Banks_outside_India4",
                  "Borrowings_from_financial_institution_in_india4","IDBI_SIDBI4","National_Bank_for_Agriculture_Rural_Development4","Export_Import_Bank_of_India4",
                  "Other_Financial_Institutions_NHB4","Borrowings_from_Financial_Institution_outside_India4","Other_Liabilities5","Drawn_by_Indian_Offices5",
                  "Drawn_by_Foreign5","Bills_payable_outside_India_5","Calls_received_in_advance_5","Miscellaneous_liabilities_5","Branch_Adjustments_6",
                  "Among_offices_in_India_6","With_offices_outside_6","Total_Demand_Time_7","Balance_of_profit_8","Balance_of_profit_1",
                  "Balance_of_profit_2","Balance_of_profit_3","Balance_of_profit_4","Balance_of_profit_5","Total_Liabilities",

                  "Cash_in_hand","Balances_with_the_Reserve_Bank_of_India","Balances_with_other_Banks_in_India_in_Current_Account","SBI31","Associates_of_the_State_Bank_of_India",
                  "Other_Commercial_Banks","Co_operative_Banks34","Money_at_call_Short_Notice","With_Commerical_Banks","With_Co_operative_Banks","With_Other_Financial_Institutions","Investments",
                  "Treasury_Bills","Other_Central_Government_Securites","State_Government_Securities","Other_approved_securities","Shares_debentures_of_companies","Fixed_Deposits_with_Banks","Other_Investments_in_India",
                  "Bills_purchased","Inland_bills_purchased","Foreign_Bills_purchased","Export_bills_drawn_in_India","Import_Bills_drawn_on_payable_in_India",
                  "Other_Foreign_bills_purchase_discounted","Payable_in_India","Payable_outside_India","Loans_Advances","Loans_advances_cash_credis_overdrafts","Due_from_banks","Co_operative_banks_in_India","Commercial_Banks_in_India","Banks_Outside_India","Premised","Branch_adjustments",
                  "Among_offices_in_India","With_offices_outside_India","Capitalised","Non_banking","Other_tangible_assets","Total_Assets"]
