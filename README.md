# 2D FFT

**Take the FFT of an image of a periodic structure, remove the periodic structure and generate a cleaned-up image without the periodic structure**

This Homework is seperated into three task groups (data collection, data preparation, and data presentation) and the same rules apply as in HW4.

## Task group 1 data collection (3 members)
Make sure your image is in compliance with the the license of this repository and add a appropiate NOTES for the repository.
Convert your image using the Pillow library into pandas (https://pypi.org/project/pillow/).
For the DataFrame use a common layout (columns and rows) and to add to the repository use `pandas.DataFrame.to_pickle` (see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_pickle.html)
- Take 3 pictures of different periodic structures and add a size marker in the image (e.g. a yard stick) and store it in a pandas dataframe that is exported to a pickle in the repository (1 member per picture due Tuesday 2pm)

## Task group 2 data preparation (6 members)
Work on one single data preparation module called `preparation.py`  that contains the following functions:
- function that reads in the pickle files from the data collection task and returns a pandas DataFrame.
Generate a 2D index / column header with the actual dimensions of the object in the picture using the size marker (1 member per picture due Thursday 2pm)
- write a function that cuts the images to a FFT suitable pixel number (1 member per picture due Thursday 2pm)
  
All following functions should assume as an input a pandas DataFrame with the index / column header the actual size of the object.
- Shifts the FFT data into a useful position 
- 2D fft / inverse fft using numpy and calculating the actual frequency in useful units (1 member due Monday 2pm)
- 2D windowing / unwindowing with a selection of windows (1 member due Wednesday 2pm)
- that removes a periodic pattern (1 member due Wednesday 2pm)

All functions must also include docstrings and unit tests in `test_preparation.py`

## Task group 3 data presentation (max 6 members)
Work on a single data analysis Jupyter notebook using functions from `preparation.py` that contain for each task below only *one plot*:

- One plot with the original frequency information with the removed part being highlighted (1 member per picture due 2nd Monday 2pm)
- One plot with the cleaned-up image (1 member per picture due 2nd Monday 2pm)


## Task group 4 maintainers (max 2 members)
- Reuse github actions for linting and unit tests
- Merge PR
- assign Reviews after member requests
  
---
## Grading

| Homework Points                  |                |              |            |
| -------------------------------- | -------------- | ------------ | ---------- |
|                                  |                |              |            |
| Interaction on project           |                |              |            |
| Category                         | min per person | point factor | max points |
| Commits                          | 1              | 1            | 1          |
| Pull requests                    | 1              | 4            | 4          |
| PR Accepted                      | 1              | 4            | 4          |
| Other PR reviewed (by request)   | 1              | 4            | 4          |     
| Issues                           | 1              | 1            | 1          | 
| Closed Issues                    | 1              | 1            | 1          |
| \# Conversations                 | 12             | 1/4          | 3          |
|                                  |                |              |            |
| Total                            |                |              | 18         |
|                                  |                |              |            |
| Shared project points            |                |              |            |
| \# Milestones                    | 12             | 1/4          | 3          |
|                                  |                |              |            |
| Total                            |                |              | 21         |
|                                  |                |              |            |
|                                  |                |              |            |
| Result                           |                |              |            |
| Task completion                  |                |              | 21         |
|                                  |                |              |            |
| Sum                              |                |              | 42         |
