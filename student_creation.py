student = ['mathan', 'vignesh', 'vishnu', 'rajesh', 'kamala', 'mahesh']

age = [20,31,20,24, 26, 26]

dept = ['CSE', 'IT', 'DS', 'MECH', 'IT', 'CSE']

maths = [80,90,99,98, 85, 94]
physics = [77,78,98,100, 75, 64]
chemistry = [85,80,88,91,84, 91]



out = [
    {
        'name': 'mathan',
        'age': 20,
        'dept': 'CSE',
        'marks': {
            "maths": 80,
            "physics": 85,
            "chemistry": 85
        },
    },
    {
        'name': 'vignesh',
        'age': 31,
        'dept': 'IT',
        'marks': {
            "maths": 80,
            "physics": 85,
            "chemistry": 85
        },
    },
    {
        'name': 'vishnu',
        'age': 20,
        'dept': 'DS',
        'marks': {
            "maths": 80,
            "physics": 85,
            "chemistry": 85
        },
    },
    {
        'name': 'rajesh',
        'age': 24,
        'dept': 'MECH',
        'marks': {
            "maths": 80,
            "physics": 85,
            "chemistry": 85
        },
    },
]


out = []

for idx,itr in enumerate(student):
    d = {}
    d['name'] = itr
    d['age'] = age[idx]
    d['dept'] = dept[idx]
    marks = {}
    marks['maths'] = maths[idx]
    marks['physics'] = physics[idx]
    marks['chemistry'] = chemistry[idx]
    d['marks'] = marks
    out.append(d)
print(out)

st = ''
mar = 0
for i in out:
    if mar < i['marks']['physics']:
        st = i['name']
        mar = i['marks']['physics']

print(st,mar)

c = []

mar = 0
stu = ''
for itr in out:
    if itr['dept'] == 'IT' and itr['marks']['maths'] > mar:
        mar = itr['marks']['maths']
        stu = itr['name']

print(mar,stu)