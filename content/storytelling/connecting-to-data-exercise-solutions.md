# Connecting to Data Exercises

1. In your mySQL client, query the database `telco_normalized`, joining all tables together into a single table which you will then export to a csv and save on your local drive. Do NOT use the telco_churn database. 


```mysql

select 
    details.customer_id
    , details.gender
    , details.senior_citizen
    , details.partner
    , details.dependents
    , churn.churn_month
    , pay.monthly_charges
    , pay.total_charges
    , pay.payment_type_id
    , paytype.payment_type
    , contract.paperless_billing
    , contract.contract_type_id
    , contype.contract_type
    , signup.signup_date
    , sub.phone_service
    , sub.multiple_lines
    , sub.internet_service_type_id
    , ist.internet_service_type
    , sub.online_security
    , sub.online_backup
    , sub.device_protection
    , sub.tech_support
    , sub.streaming_tv
    , sub.streaming_movies
from telco_normalized.customer_details details
left join customer_churn churn on details.customer_id = churn.customer_id
left join customer_payments pay on details.customer_id = pay.customer_id
left join customer_contracts contract on details.customer_id = contract.customer_id
left join customer_signups signup on details.customer_id = signup.customer_id
left join customer_subscriptions sub on details.customer_id = sub.customer_id
left join internet_service_types ist on sub.internet_service_type_id = ist.internet_service_type_id
left join payment_types paytype on pay.payment_type_id = paytype.payment_type_id
left join contract_types contype on contract.contract_type_id = contype.contract_type_id;
```


6 Calculated field = 'Estimated Tenure (months)', Calculation:  [Total Charges]/[Monthly Charges]

7. Calculated field = 'Customer Status', Calculation: IF  ISNULL([Churn Month]) THEN 'churned' ELSE 'active' END
