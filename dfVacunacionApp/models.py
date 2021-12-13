from django.db import models

# Create your models here.
import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)

results = client.get("gt2j-8ykr", limit=1000000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

