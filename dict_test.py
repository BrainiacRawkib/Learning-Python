first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = int(input('Enter your age: '))
job = input('What is your occupation: ')
post = input('What is your post in the org: ')

dict_zip = dict(zip(['Name', 'Age', 'Job'], [first_name, age, job]))

print(dict_zip)

job_profile = {'Name': {'First name': first_name, 'Last name': last_name},
               'Age': [age], 'jobs details': {'Job type': job, 'Position': post}}

print(job_profile)

print(job_profile['Name'])
print(job_profile['Name']['Last name'])


dict = {'a': 1, 'b': 2, 'h': 8, 'g': 7}

print(sorted(dict.items()))

