def business_card
name_input = input('what is your name ?')
email_input = input('what is your email ? ')
phone_num_input = int(input('what is your phone number ? '))
job_title = input('what is yor job ? ')

business = {'name': name_input,
            'email': email_input,
            'phone': phone_num_input,
            'job_title': job_title
            }

print('--- business card-----')
print(f'Name: {business['name']}')
print(f'Email: {business['email']}')
print(f'Phone: {business['phone']}')
print(f'Job title: {business['job_title']}')
