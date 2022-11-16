# Plaid_django

Plaid​ is an account aggregation service where users can login with their bank credentials and plaid fetches last two years of transaction and account balance data for their bank account. This project is its implementation using Django.

* Item​ , a set of credentials (map of key value pairs) associated with a financial institution and a user.
- Users can have multiple Items for multiple financial institutions.
- Each ​Item​ can have many associated accounts, which hold information such as balance, name, and account type

<img src="https://user-images.githubusercontent.com/75966962/202279334-7f94676b-e460-42de-af0a-2fe727118bc5.jpg">

## Django rest Apis for signup, login and logout

`api/register/` - Create user using username, email and password

`api/login/` - Login using username and password

`api/logout/` - Logout using knox token


## Fetch and store data from Plaid Apis

`get_public_token/` - Get public token from Plaid

`get_access_token/` - Exchange public token with access token

`get_transactions/` - Get transactions from plaid api

`get_transactions_from_db/` - Fetch transactions saved in db

`get_account_balance/` - Get account details from plaid api

`get_account_balance_from_db/` - Fetch account details saved in db


## Webhooks
    
`webhook_test/` - Fire a test sandbox webhook 

`webhook_transactions/` - Transactions Webhook 


## Description

Databse is SQLite

Start the rabbitmq server - `rabbitmq-server`

Async tasks handled by celery - `celery -A plaid_django worker -l info`

Localhost exposed using ngrox for webhooks - `./ngrox http 8000`
