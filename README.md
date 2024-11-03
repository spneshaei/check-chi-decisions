# Check CHI Decisions

This script provides a quick way to validate that you, as a CHI 2024 Subcommittee Chair, have correctly assigned reject (X1) and revise-and-resubmit (RR) decisions in the first round of reviews.

In addition, the script will also let you know about the papers without an 1AC (meta-review) or 2AC score and the papers that have committee scores but are not marked as `R1ready` by the AC. It also provides general statistics on the number of papers decided as X1 or RR.

This script is developed by Seyed Parsa Neshaei on November 2024. This script is only validated to be used by the subcommittee chairs for the first round of reviews at CHI 2024; it might need changes for other iterations of the conference. There is no guarantee provided of any kind for the code; use it only in addition to checking the results manually. Let me know via GitHub issues if you found any bugs or have any suggestions!

## How to use the script

1. Clone this GitHub repository or download it as a ZIP file and extract it.

2. Go to the directory where you have the `check-decisions-round-1.py` file using your Terminal.

3. Install the necessary package (`pandas`) if you don't have it already installed from our provided requirements file, by running `pip install -r requirements.txt` in your Terminal.

4. Export the CSV file from the Submissions page in the Chairing tab in your PCS account and save it with the name of `Submissions.csv` in the same directory as the script.

5. Run the script by typing `python check-decisions-round-1.py` in your Terminal.

