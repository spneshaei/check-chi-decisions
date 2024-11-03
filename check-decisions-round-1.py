# check-decisions-round-1.py

# This code will check if the rejection and revise-and-resubmit decisions are correct for the first round of reviews at CHI.
# This script is only validated to be used by the subcommittee chairs for the first round of reviews at CHI 2024; it might need changes for other iterations of the conference.
# There is no guarantee provided of any kind for the code; use it only in addition to checking the results manually.

# Developed by Seyed Parsa Neshaei on November 2024
# Let me know via GitHub issues if you found any bugs or have any suggestions!

import pandas as pd

# Load the data exported from PCS
data = pd.read_csv('Submissions.csv')

papers_without_scores_by_both_1AC_and_2AC = []
papers_without_meta_review_scores = []
papers_not_ready_for_round_1_reviews = []
papers_that_should_be_RR_but_are_not = []
papers_that_should_be_X1_but_are_not = []
currently_rr_papers = []
currently_x1_papers = []

# Iterate over the rows
for (i, row) in data.iterrows():
    if str(row['Decision']) == 'RR':
        currently_rr_papers.append(row['ID'])
    elif str(row['Decision']) == 'X1':
        currently_x1_papers.append(row['ID'])
    committee_scores_parts = str(row['CommitteeScore']).split(', ')
    if len(committee_scores_parts) != 2:
        if not ('DR' in str(row['Decision']) or 'Incomplete' in str(row['Decision'])):
            if str(row['Pscore']).strip() != "":
                papers_without_scores_by_both_1AC_and_2AC.append(row['ID'])
            else:
                papers_without_meta_review_scores.append(row['ID'])
    else:
        should_paper_be_RR = True
        if 'X' in str(committee_scores_parts[0]) and 'X' in str(committee_scores_parts[1]):
            should_paper_be_RR = False
        if str(row['PRound 1 Reviews Ready to be Sent to Authors']) != 'R1ready':
            papers_not_ready_for_round_1_reviews.append(row['ID'])
        else:
            if should_paper_be_RR and str(row['Decision']) != 'RR' and str(row['Decision']).strip() != '':
                papers_that_should_be_RR_but_are_not.append(row['ID'])
            elif not should_paper_be_RR and str(row['Decision']) != 'X1' and str(row['Decision']).strip() != '':
                papers_that_should_be_X1_but_are_not.append(row['ID'])

found_at_least_one_error = False
if len(papers_without_meta_review_scores) != 0:
    print('Paper IDs without meta-review scores:', papers_without_meta_review_scores, f'(a total of {len(papers_without_meta_review_scores)} papers)')
    found_at_least_one_error = True
if len(papers_without_scores_by_both_1AC_and_2AC) != 0:
    print('Paper IDs without a committee member score (other than 1AC):', papers_without_scores_by_both_1AC_and_2AC, f'(a total of {len(papers_without_scores_by_both_1AC_and_2AC)} papers)')
    found_at_least_one_error = True
if len(papers_not_ready_for_round_1_reviews) != 0:
    print('Paper IDs that are not yet designated as ready for round 1 reviews by 1AC, but have committee scores submitted:', papers_not_ready_for_round_1_reviews, f'(a total of {len(papers_not_ready_for_round_1_reviews)} papers)')
    found_at_least_one_error = True
if len(papers_that_should_be_RR_but_are_not) != 0:
    print('Paper IDs that should be RR but are not:', papers_that_should_be_RR_but_are_not, f'(a total of {len(papers_that_should_be_RR_but_are_not)} papers)')
    found_at_least_one_error = True
if len(papers_that_should_be_X1_but_are_not) != 0:
    print('Paper IDs that should be X1 but are not:', papers_that_should_be_X1_but_are_not, f'(a total of {len(papers_that_should_be_X1_but_are_not)} papers)')
    found_at_least_one_error = True

if not found_at_least_one_error:
    print('No errors found in the decisions for the first round of reviews based on the error conditions checked by the script.\n')

print("General statistics:")
print(f"Number of papers currently with RR decision: {len(currently_rr_papers)}")
print(f"Number of papers currently with X1 decision: {len(currently_x1_papers)}")
print(f"Total number of papers: {len(data)}")

