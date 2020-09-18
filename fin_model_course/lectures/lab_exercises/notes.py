from build_tools.config import LAB_FOLDER_NAME
from lectures.lab_exercise import LabExerciseLecture
from lectures.model import LectureNotes, Lecture, LectureResource
from lectures.python_basics.notes import LECTURE_4_COMMON_RESOURCES
from schedule.main import LECTURE_2_NAME, LECTURE_3_NAME, LECTURE_4_NAME, LECTURE_5_NAME, LECTURE_6_NAME

LAB_LECTURE_4_COMMON_RESOURCES = [
    LECTURE_4_COMMON_RESOURCES[1],
    LectureResource(f'Slides - {LECTURE_4_NAME}',
                    static_url=f'generated/pdfs/S4 {LECTURE_4_NAME}.pdf'),
]

LAB_LECTURE_6_COMMON_RESOURCES = [
    LectureResource(f'Pandas and Visualization Labs',
                    static_url=f'{LAB_FOLDER_NAME}/Visualization/Pandas and Visualization Labs.ipynb'),
    LectureResource(f'Slides - {LECTURE_6_NAME}',
                    static_url=f'generated/pdfs/S6 {LECTURE_6_NAME}.pdf'),
]


def get_simple_retirement_lab_lecture() -> LabExerciseLecture:
    title = 'Extending a Simple Retirement Model'
    short_title = 'Vary Savings Rate Lab'
    youtube_id = 'KVVabq4n-ow'
    due_week = 2
    bullets = [
        [
            "Now we want to see the effect of savings rate on time until retirement, in addition to interest rate",
            "In both Excel and Python, calculate the years to retirement for savings rates of 10%, 25%, and 40%, "
            "and each of these cases with each of the interest rate cases, 4%, 5%, and 6%",
            f"Be sure that you drag formulas in Excel and use for loops in Python to accomplish this",
            "In total you should have 9 calculated years to retirement numbers, in each of the two models.",
        ]
    ]
    answers = [
        [
            "Martha has 61.1 years to retirement if she earns a 4% return and saves 10%.",
            "Martha has 41.0 years to retirement if she earns a 4% return and saves 25%.",
            "Martha has 31.9 years to retirement if she earns a 4% return and saves 40%.",
            "Martha has 53.3 years to retirement if she earns a 5% return and saves 10%.",
            "Martha has 36.7 years to retirement if she earns a 5% return and saves 25%.",
            "Martha has 29.0 years to retirement if she earns a 5% return and saves 40%.",
            "Martha has 47.6 years to retirement if she earns a 6% return and saves 10%.",
            "Martha has 33.4 years to retirement if she earns a 6% return and saves 25%.",
            "Martha has 26.7 years to retirement if she earns a 6% return and saves 40%.",
        ]
    ]
    resources = [
        LectureResource(
            'Simple Retirement Model Excel',
            static_url='Examples/Introduction/Excel/Simple Retirement Model.xlsx'
        ),
        LectureResource(
            'Simple Retirement Model Python',
            static_url='Examples/Introduction/Python/Simple Retirement Model.ipynb'
        ),
        LectureResource(f'Slides - {LECTURE_2_NAME}', static_url=f'generated/pdfs/S2 {LECTURE_2_NAME}.pdf'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_extend_dynamic_retirement_excel_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Excel Model'
    short_title = 'Dynamic Desired Cash in Excel'
    youtube_id = 'cM3uKsHXS3M'
    due_week = 2
    bullets = [
        [
            'We want to relax the assumption that the amount needed in retirement is given by '
            'a fixed amount of desired cash',
            'Add new inputs to the model, "Annual Cash Spend During Retirement" and "Years in Retirement"',
            'Calculate desired cash based on interest, cash spend, and years in retirement',
            'Use the calculated desired cash in the model to determine years to retirement',

        ]
    ]
    answers = [
        [
            r'If annual spend is 40k for 25 years in retirement, \$563,757.78 should be the retirement cash and there '
            r'should be 18 years to retirement.'
        ]
    ]
    resources = [
        LectureResource(
            'Dynamic Salary Retirement Model - Excel',
            static_url='Examples/Introduction/Excel/Dynamic Salary Retirement Model.xlsx'
        ),
        LectureResource(f'Slides - {LECTURE_3_NAME}',
                        static_url=f'generated/pdfs/S3 {LECTURE_3_NAME}.pdf'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_conditionals_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Conditionals'
    short_title = 'Python Conditionals Lab'
    youtube_id = 'T4LK0QgPbNA'
    due_week = 2
    bullets = [
        [
            f"The Jupyter notebook called Python Basics Lab contains "
            f"all of the labs for today's lecture",
            'Please complete the exercises under "Conditionals"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_lists_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Lists'
    short_title = 'Python Lists Lab'
    youtube_id = 'AViA3IBpXcc'
    due_week = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Please complete the exercises under "Working with Lists"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_functions_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Functions'
    short_title = 'Python Functions Lab'
    youtube_id = 'xOxJst-SMy8'
    due_week = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Please complete the exercises under "Functions"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_data_types_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Data Types'
    short_title = 'Python Data Types Lab'
    youtube_id = 'pyjfrIzdjgo'
    due_week = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Please complete the exercises under "Data Types"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_python_basics_classes_lab_lecture() -> LabExerciseLecture:
    title = 'Python Basics - Classes'
    short_title = 'Python Classes Lab'
    youtube_id = 'znxtmT66UAM'
    due_week = 3
    bullets = [
        [
            "Keep working off of Python Basics Lab.ipynb",
            'Make sure you have car_example.py in the same folder',
            'Please complete the exercises under "Working with Classes"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_4_COMMON_RESOURCES,
        LectureResource(
            'Car Class Example',
            static_url='Examples/Introduction/Python/car_example.py'
        ),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_extend_dynamic_retirement_python_lab_lecture() -> LabExerciseLecture:
    title = 'Determining Desired Cash in the Dynamic Salary Retirement Python Model'
    short_title = 'Dynamic Desired Cash in Python'
    youtube_id = ''
    due_week = 4
    bullets = [
        [
            'We want to relax the assumption that the amount needed in retirement is given by '
            'a fixed amount of desired cash',
            'Start from the completed retirement model Jupyter notebook Dynamic Salary Retirement Model.ipynb',
            'Add new inputs to the model, "Annual Cash Spend During Retirement" and "Years in Retirement"',
            'Calculate desired cash based on interest, cash spend, and years in retirement',
            'Use the calculated desired cash in the model to determine years to retirement',
        ]
    ]
    answers = [
        [
            r'If annual spend is 40k for 25 years in retirement, \$563,757.78 should be the retirement cash and there '
            r'should be 18 years to retirement.'
        ]
    ]
    resources = [
        LectureResource(
            'Dynamic Salary Retirement Model - Python',
            static_url='Examples/Introduction/Python/Dynamic Salary Retirement Model.ipynb'
        ),
        LectureResource(f'Slides - {LECTURE_5_NAME}',
                        static_url=f'generated/pdfs/S5 {LECTURE_5_NAME}.pdf'),
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_intro_to_pandas_lab_lecture() -> LabExerciseLecture:
    title = 'Getting Started with Pandas'
    short_title = 'Intro Pandas Lab'
    youtube_id = ''
    due_week = 5
    bullets = [
        [
            'Work off of the Jupyter notebook Pandas and Visualization Labs.ipynb',
            'Complete the lab exercises in the first section entitled "Pandas"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_6_COMMON_RESOURCES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_pandas_styling_lab_lecture() -> LabExerciseLecture:
    title = 'Styling Pandas DataFrames'
    short_title = 'Pandas Styling Lab'
    youtube_id = ''
    due_week = 5
    bullets = [
        [
            'Keep working with the same lab Jupyter Notebook',
            'Complete the lab exercises in the second section entitled "Pandas Styling"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_6_COMMON_RESOURCES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )


def get_intro_python_visualization_lab_lecture() -> LabExerciseLecture:
    title = 'Introduction to Graphing with Pandas'
    short_title = 'Intro Visualization Lab'
    youtube_id = ''
    due_week = 5
    bullets = [
        [
            'Keep working with the same lab Jupyter Notebook',
            'Complete the lab exercises in the final section entitled "Graphics"'
        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [
        *LAB_LECTURE_6_COMMON_RESOURCES
    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )



def get_lab_lecture() -> LabExerciseLecture:
    title = ''
    short_title = title
    youtube_id = ''
    due_week = 0
    bullets = [
        [

        ]
    ]
    answers = [
        [

        ]
    ]
    resources = [

    ]
    return LabExerciseLecture.from_seq_of_seq(
        title, bullet_content=bullets, answers_content=answers, short_title=short_title,
        youtube_id=youtube_id, resources=resources, due_week=due_week,
    )

