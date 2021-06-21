#!pip install mlxtend
import pandas as pd
from helpers import helpers as bkanber
from mlxtend.frequent_patterns import apriori, association_rules

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

df_ = pd.read_excel("online_retail_II.xlsx", sheet_name="Year 2010-2011")
df = df_.copy()
df = bkanber.retail_data_prep(df)

rules_grm = bkanber.create_rules(df, country="Germany")

bkanber.check_id(df, 21987)
bkanber.check_id(df, 23235)
bkanber.check_id(df, 22747)

bkanber.arl_recommender(rules_grm, 21987, 1)
bkanber.arl_recommender(rules_grm, 23235, 1)
bkanber.arl_recommender(rules_grm, 22747, 1)

bkanber.check_id(df, 21988)
#['PACK OF 6 SKULL PAPER PLATES']
bkanber.check_id(df, 23244)
#['ROUND STORAGE TIN VINTAGE LEAF']
bkanber.check_id(df, 22746)
#["POPPY'S PLAYHOUSE LIVINGROOM "]