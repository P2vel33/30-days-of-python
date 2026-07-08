# exexercise 5.1
list511 = list()
list512 = []
print(list511)
print(list512)

# exexercise 5.2
list52 = ['banana', 'orange', 'mango', 'lemon',"apple",'lime',"potato"]
print(list52)

# exexercise 5.3
print(len(list52))

# exexercise 5.4
print(list52[0],list52[-1],list52[len(list52) // 2])

# exexercise 5.5
mixed_data_types = list(["Pavel", 24, 178, {"married": False}])
print(mixed_data_types)

# exexercise 5.6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# exexercise 5.7
print(it_companies)

# exexercise 5.8
print(len(it_companies))

# exexercise 5.9
print(" ".join(it_companies[::len(it_companies)//2]))

# exexercise 5.10
it_companies[2] = "Figma"
print(it_companies)

# exexercise 5.11
it_companies.append("Microsoft")
print(it_companies)

# exexercise 5.12
it_companies.insert( len(it_companies) // 2,"Antrohic")
print(it_companies)

# exexercise 5.13
it_companies[1] = it_companies[1].upper()
print(it_companies)

# exexercise 5.14
print("#;".join(it_companies))

# exexercise 5.15
print("Antrohic" in it_companies)

# exexercise 5.16
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

# exexercise 5.17
it_companies.reverse()
print(it_companies)

# exexercise 5.18
print(it_companies[2:])

# exexercise 5.19
print(it_companies[:-3])

# exexercise 5.20
del it_companies[3:5]
print(it_companies)

# exexercise 5.21
it_companies.pop(0)
print(it_companies)

# exexercise 5.24
del it_companies[0: len(it_companies)]
print(it_companies)

# exexercise 5.25
del it_companies

# exexercise 5.26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# exexercise 5.25
full_stack = []
full_stack = front_end + back_end
full_stack.insert(full_stack.index("Redux"), "SQL")
full_stack.insert(full_stack.index("Redux"), "Python")
print(full_stack)

# exexercise 5 level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0], ages[-1])
print(min(ages), max(ages))
ages.append(17)
ages.append(30)
ages.sort()
print((ages[len(ages) // 2] + ages[len(ages) // 2 + 1])/2)
total = 0
for age in ages:
    total += age
print(total / len(ages))
print(max(ages) - min(ages))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];


print(countries[len(countries) // 2])
print(countries[::2])
print(countries[1::2])

last_countries = ['Китай', 'Россия', 'Финляндия', 'Швеция', 'Норвегия', 'Дания' ,'США']
china, russia,  *scandic, usa = last_countries
print(scandic)

