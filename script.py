import familiar
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

#Save data in variable
vein_pack_lifespans = familiar.lifespans(package='vein')
print(vein_pack_lifespans)

print(np.mean(vein_pack_lifespans))

#how far is the mean 71 from the data mean (far)
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test)

if (vein_pack_test.pvalue < 0.05):
  print("The Vein Pack Is Proven To Make You Live Longer!")
else:
  print("The Vein Pack Is Probably Good For You Somehow!")

artery_pack_lifespans = familiar.lifespans(package='artery')
print(artery_pack_lifespans)
print(np.mean(artery_pack_lifespans))

#Compare the mean of two data sets
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(package_comparison_results)

if (package_comparison_results.pvalue < 0.05):
  print("the Artery Package guarantees even stronger results!")
else:
  print("the Artery Package is also a great product!")

iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)

#Run Chi test
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)
print(iron_pvalue)

if (iron_pvalue < 0.05):
  print("The Artery Package Is Proven To Make You Healthier!")
else:
  print("While We Cant Say The Artery Package Will Help You I Bet Its Nice!")