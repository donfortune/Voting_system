Candidate1 = 'John'
Candidate2 = 'David'

results = {'John': 0, 'David': 0}

while True:
    print('Welcome to Today\'s Election')
    intro = f'On the ballot today, we have Mr {Candidate1} and Mr {Candidate2}'
    print(intro)
    Decision = input('Enter your preffered candidate: ')
    if Decision == Candidate1:
        print('Decision Noted')
        results['John'] += 1
    elif Decision == Candidate2:
        print('Decision Noted')
        results['David'] += 1
    else:
        print('You entered an invalid value')
    continue_voting = input('Do you want to continue voting? (yes/no): ')
    if continue_voting.lower() != 'yes':
        break




for candidate, votes in results.items():
    print(f'{candidate}: {votes} votes')
#print(results)