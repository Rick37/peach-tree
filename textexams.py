import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix','Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver','Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee','Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for textnum in range(3):
    textfile = open('quiz%s.txt'%(textnum + 1),'w')
    answerfile = open('answer%s.txt'%(textnum + 1),'w')

    textfile.write('Name:\nDate:\n\n')
    answerfile.write('Answer%s'%(textnum + 1))
    answerfile.write('\n')

    timu = list(capitals.keys())
    for i in range(len(timu)):
        random.shuffle(timu)
        coan = capitals[timu[i]]
        wrongans = list(capitals.values())
        wrongans.remove(coan)
        wrongan = random.sample(wrongans,3)
        wrongan.append(coan)
        random.shuffle(wrongan)

        textfile.write('%s.What is the capital of %s\n' %(i+1,timu[i]))
        for j in range(4):
            textfile.write('%s.%s\n'%('ABCD'[j],wrongan[j]))
        textfile.write('\n')
        answerfile.write('%s.%s\n'%(i+1,'ABCD'[wrongan.index(coan)]))
textfile.close()
answerfile.close()