# Resume-Screening-and-scoring
It's a automatically resume screening and keywords scan-matching function.

The .ipynb file use NLP to do the function
ResumeReading-This step is like data reading and data cleaning of resumes. Specifically, I convert all files of various formats including pdf, word and so on into txt format, and then clean the text data into a unified text format, such as uppercase to lowercase, remove line changes, remove special symbols and so on.  

Keywords corpora: I built 3 corpora to build the keywords library. The first corpora is about the professional skills of data positions, and the second one is about the general skills of good candidates, and the last one is the job titles that can appear in the experience. All of these 3 corpora built the keywords library to be the basic of resume scoring function.  

This is the keywords scan-matching result:

![1655923921093](https://user-images.githubusercontent.com/102696094/175114374-d8d76277-d3f4-4456-8a02-33879cbcd9e4.png)

![1655923948894](https://user-images.githubusercontent.com/102696094/175114417-0d8073ae-c8b2-4b3c-9eb4-46b23992e695.png)



Keywords scan-matching and scoring: Then I use Spacy-PhraseMatcher in Spacy packages to do keywords scan-matching from keywords in resume to the keywords library we built and calculated the final score for each candidate by assigning different weights to corpora. This weight is determined by the client company.
