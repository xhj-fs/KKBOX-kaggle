'''
last_1_is_churn', 'last_2_is_churn', 'last_3_is_churn', 'last_4_is_churn', 'last_5_is_churn',
'churn_rate', 'churn_count',
If one member had membership expire five times in the past,
for example 201603, 201604, 201605, 201606, and 201607,
"last_1_is_churn" means did this member churn in 201607 or not;
"last_2_is_churn" means did this member churn in 201606 or not; and so on.
'''

import pandas as pd
import datetime
from tqdm import tqdm

#transactions = pd.read_csv('trans_test.csv').reset_index(drop=True)
#transactions = pd.read_csv('sorted_trans_for_last.csv')

for reader in pd.read_csv('trans_test.csv',chunksize=10000):
    for chunk in reader:
        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
        chunk.columns = ['msno', 't_date', 'e_date']
        result = chunk[(chunk.ref.str.contains('^[a-zA-Z]+')) & (chunk.ref.str.len() > 80)]
        result.to_csv(out_f, index=False, header=False, mode='a')

msno = (transaction['msno'])
# transaction_date = row['transaction_date']
# membership_expire_date = row['membership_expire_date']
print(msno)

    

# result = pd.DataFrame()
# transaction_dates = []
# membership_expire_dates = []
# prev_msno = ''
# total_rows = len(transactions['msno'])

# def calc_churn(t_dates, e_dates, msno):

#     churn = 1
#     if (len(t_dates) >1):
#         if int(e_dates[-2]) / 100 >= 201703:  # if expiration data is 201703 onwards, treat as no churn
#             churn = 0
#         expired_date = datetime.datetime.strptime(str(e_dates[-2]), "%Y%m%d")
#         trans_date = datetime.datetime.strptime(str(t_dates[-1]), "%Y%m%d")
#         dif_d = (trans_date - expired_date).days
#         if (0 <= dif_d < 30):  # if some trans resubscribe
#             churn = 0

#     df = {'msno': [msno], 'last_1_is_churn': [churn]}
#     # df = pd.DataFrame(data=np.array([[1, 2, 3]]), columns=['msno','last_1_is_churn','last_2_is_churn','last_3_is_churn','last_4_is_churn','last_5_is_churn'])
#     return df


# for i, row in tqdm(transactions.iterrows(), total=total_rows):
#     msno = row['msno']
#     transaction_date = row['transaction_date']
#     membership_expire_date = row['membership_expire_date']

#     if (msno != prev_msno and prev_msno):
#         result = result.append(pd.DataFrame(data=calc_churn(transaction_dates,
#                                                             membership_expire_dates, prev_msno)))
#         transaction_dates.clear()
#         membership_expire_dates.clear()  # clear lists, start recording this new user id

#     transaction_dates.append(transaction_date)
#     membership_expire_dates.append(membership_expire_date)
#     prev_msno = msno

# result = result[['msno', 'last_1_is_churn']]
# result.to_csv('last_is_churns.csv', index=False)
