import pandas as pd

customers = pd.read_csv('./data/Cust_Churn_Telco.csv')
customers.columns = ['customer_id', 'gender', 'senior_citizen', 'partner', 'dependents', 'tenure', 'phone_service', 'multiple_lines', 'internet_service', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract', 'paperless_billing', 'payment_method', 'monthly_charges', 'total_charges', 'churn']

# TODO: extract duplicate code to a named function
internet_types = list(customers.internet_service.unique())
lookup_internet_type = {type: (i + 1) for i, type in enumerate(internet_types)}
customers.internet_service = customers.internet_service.apply(lambda t: lookup_internet_type[t])
internet_service_types = pd.DataFrame([(i + 1, type) for i, type in enumerate(internet_types)], columns=['internet_service_type_id', 'internet_service_type'])
customers.rename(columns={'internet_service': 'internet_service_type_id'}, inplace=True)
internet_service_types.internet_service_type = internet_service_types.internet_service_type.apply(lambda s: 'None' if s == 'No' else s)

payment_types = list(customers.payment_method.unique())
lookup_payment_types = {type: (i + 1) for i, type in enumerate(payment_types)}
customers.rename(columns=dict(payment_method='payment_type_id'), inplace=True)
customers.payment_type_id = customers.payment_type_id.apply(lambda t: lookup_payment_types[t])
payment_types = pd.DataFrame([(i + 1, type) for i, type in enumerate(payment_types)], columns=['payment_type_id', 'payment_type'])

contract_types = list(customers.contract.unique())
lookup_contract_type = {type: (i + 1) for i, type in enumerate(contract_types)}
customers.contract = customers.contract.apply(lambda t: lookup_contract_type[t])
customers.rename(columns={'contract': 'contract_type_id'}, inplace=True)
contract_types = pd.DataFrame([(i + 1, type) for i, type in enumerate(contract_types)], columns=['contract_type_id', 'contract_type'])

