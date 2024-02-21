import pandas as pd
from sys import argv, exit
from os import path

if len(argv) < 2:
    print('Please pass the filepath to the grade report csv file.')
    exit(1)

if not path.exists(argv[1]):
    print(f'{argv[1]} not found!')
    exit(1)

df = pd.read_csv(argv[1])
df.present = df.present.apply(lambda x: 'Ok' if x else 'Missing')

print('''
<style>
@media print {
    hr { display: block; border: 0; page-break-after: always; }
}
</style>

''')

for name in df.name.unique():
    data = df[df.name == name][['file', 'present']].set_index('file')
    data.rename(columns={'present': 'status'}, inplace=True)
    s = '\n'.join([(' ' * 8) + line for line in str(data).split('\n')])
    print(f'# Exercises')
    print()
    print(f'- name: {name}')
    print(f'- repo: ds-methodologies-exericses')
    print()
    print(s)
    print()
    print('If a file does not have an extension, that means it may either be a')
    print('python script or a jupyter notebook, so long as it has the specified')
    print('name.')
    print()
    print('---')
    print()
