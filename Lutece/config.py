# Set the paginator number
PER_PAGINATOR_COUNT = 20

# Set the number of problem/status one page should be shown
PER_PAGE_COUNT = 20

# Set the source code max-length
'''
    Warning:
        + The change of MAX_SOURCECORE_LENGTH may need to change the submission.model, CharField's MaxLength is 64mb.
'''
MAX_SOURCECORE_LENGTH = 60000

# Tht list of language that Osiris current support.
'''
    Warning:
        + The change of SUPPORT_LANGUAGE_LIST may need to change the highlight css.
'''
SUPPORT_LANGUAGE_LIST=[
    'GNU G++17',
    'Clang 6.0.0',
    'GNU GCC 7.3',
    'Python 3.6.5',
    'Java 10',
    'Go 1.9.2',
    'Ruby 2.5.1',
    'Rust 1.25.0',
]

# basic checker from testlib.h
CHECKER_LIST=[
    'wcmp: compare sequences of tokens',
    'acmp: compare two doubles, maximal absolute error = 1.5E-6',
    'caseicmp: Single int64 checker with testcase-support',
    'casencmp: Many int64s checker with testcase-support',
    'casewcmp: Tokens checker with testcase-support',
    'dcmp: compare two doubles, maximal absolute or relative error = 1E-6',
    'fcmp: compare files as sequence of lines',
    'hcmp: compare two signed huge integers',
    'icmp: compare two signed int',
    'lcmp: compare files as sequence of tokens in lines' ,
    'ncmp: compare ordered sequences of signed int numbers' ,
    'rcmp: compare two doubles, maximal absolute error = 1.5E-6' ,
    'rcmp4: compare two sequences of doubles, max absolute or relative error = 1E-4' ,
    'rcmp6: compare two sequences of doubles, max absolute or relative  error = 1E-6' ,
    'rcmp9: compare two sequences of doubles, max absolute or relative error = 1E-9' ,
    'rncmp: compare two sequences of doubles, maximal absolute error = 1.5E-5' ,
    'uncmp: compare unordered sequences of signed int numbers' ,
]


# Judge Status and error code
JUDGE_RESULT = {
    'Waiting' : 0, # Waiting for judge
    'Preparing' : 1, # Submission has been fetched by one judge
    'Running' : 2,
    'Accepted' : 3,
    'Compile Error' : 4,
    'Wrong Answer' : 5,
    'Runtime Error' : 6,
    'Time Limit Exceeded' : 7,
    'Output Limit Exceeded' : 8,
    'Memory Limit Exceeded' : 9,
    'Judger Error' : 10,
}