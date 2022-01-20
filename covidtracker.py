'''This bot informs users about the coronavirus pandemic. !help for commands''' # Last updated 12-24-20

# Last updated 12-23-20
import discord
from urllib.request import urlopen
import json

# Last updated 12-23-20
iso = {"Thailand": "THA", "Japan": "JPN", "Singapore": "SGP", "Nepal": "NPL", "Malaysia": "MYS", "Canada": "CAN", "Australia": "AUS", "Cambodia": "KHM", "Sri Lanka": "LKA", "Germany": "DEU", "Finland": "FIN", "United Arab Emirates": "ARE",
  "Philippines": "PHL", "India": "IND", "Italy": "ITA", "Sweden": "SWE", "Spain": "ESP", "Belgium": "BEL", "Egypt": "EGY", "Lebanon": "LBN", "Iraq": "IRQ",
  "Oman": "OMN", "Afghanistan": "AFG", "Bahrain": "BHR", "Kuwait": "KWT", "Algeria": "DZA", "Croatia": "HRV", "Switzerland": "CHE", "Austria": "AUT",
  "Israel": "ISR", "Pakistan": "PAK", "Brazil": "BRA", "Georgia": "GEO", "Greece": "GRC", "North Macedonia": "MKD", "Norway": "NOR",
  "Romania": "ROU", "Estonia": "EST", "San Marino": "SMR", "Belarus": "BLR", "Iceland": "ISL", "Lithuania": "LTU", "Mexico": "MEX",
  "New Zealand": "NZL", "Nigeria": "NGA", "Ireland": "IRL", "Luxembourg": "LUX", "Monaco": "MCO", "Qatar": "QAT", "Ecuador": "ECU",
  "Azerbaijan": "AZE", "Armenia": "ARM", "Dominican Republic": "DOM", "Indonesia": "IDN", "Portugal": "PRT", "Andorra": "AND", "Latvia": "LVA",
  "Morocco": "MAR", "Saudi Arabia": "SAU", "Senegal": "SEN", "Argentina": "ARG", "Chile": "CHL", "Jordan": "JOR", "Ukraine": "UKR",
  "Hungary": "HUN", "Liechtenstein": "LIE", "Poland": "POL", "Tunisia": "TUN", "Bosnia and Herzegovina": "BIH", "Slovenia": "SVN",
  "South Africa": "ZAF", "Bhutan": "BTN", "Cameroon": "CMR", "Colombia": "COL", "Costa Rica": "CRI", "Peru": "PER", "Serbia": "SRB",
  "Slovakia": "SVK", "Togo": "TGO", "Malta": "MLT", "Martinique": "MTQ", "Bulgaria": "BGR", "Maldives": "MDV", "Bangladesh": "BGD",
  "Paraguay": "PRY", "Albania": "ALB", "Cyprus": "CYP", "Brunei": "BRN", "US": "USA", "Burkina Faso": "BFA", "Holy See": "VAT", "Mongolia": "MNG",
  "Panama": "PAN", "China": "CHN", "Iran": "IRN", "Korea, South": "KOR", "France": "FRA", "Cruise Ship": "SHP", "Denmark": "DNK",
  "Czechia": "CZE", "Taiwan*": "TWN", "Vietnam": "VNM", "Russia": "RUS", "Moldova": "MDA", "Bolivia": "BOL", "Honduras": "HND", "United Kingdom": "GBR",
  "Congo (Kinshasa)": "COD", "Cote d'Ivoire": "CIV", "Jamaica": "JAM", "Turkey": "TUR", "Cuba": "CUB", "Guyana": "GUY", "Kazakhstan": "KAZ",
  "Ethiopia": "ETH", "Sudan": "SDN", "Guinea": "GIN", "Kenya": "KEN", "Antigua and Barbuda": "ATG", "Uruguay": "URY", "Ghana": "GHA",
  "Namibia": "NAM", "Seychelles": "SYC", "Trinidad and Tobago": "TTO", "Venezuela": "VEN", "Eswatini": "SWZ", "Gabon": "GAB", "Guatemala": "GTM",
  "Mauritania": "MRT", "Rwanda": "RWA", "Saint Lucia": "LCA", "Saint Vincent and the Grenadines": "VCT", "Suriname": "SUR", "Kosovo": "RKS",
  "Central African Republic": "CAF", "Congo (Brazzaville)": "COG", "Equatorial Guinea": "GNQ", "Uzbekistan": "UZB", "Netherlands": "NLD",
  "Benin": "BEN", "Liberia": "LBR", "Somalia": "SOM", "Tanzania": "TZA", "Barbados": "BRB", "Montenegro": "MNE", "Kyrgyzstan": "KGZ",
  "Mauritius": "MUS", "Zambia": "ZMB",
  "Djibouti": "DJI", "Gambia, The": "GMB", "Gambia": "GMB", "Bahamas, The": "BHS", "Bahamas": "BHS", "Chad": "TCD", "El Salvador": "SLV",
  "Fiji": "FJI", "Nicaragua": "NIC", "Haiti": "HTI", "Syria": "SYR", "Angola": "AGO", "Madagascar": "MDG", "Cabo Verde": "CPV", "Niger": "NER",
  "Papua New Guinea": "PNG", "Zimbabwe": "ZWE", "Cape Verde": "CBV", "East Timor": "ETL", "Uganda": "UGA", "Dominica": "DMA", "Grenada": "GRD",
  "Mozambique": "MOZ", "Timor-Leste": "TLS", "Eritrea": "ERI", "Belize": "BLZ", "Diamond Princess": "DPS", "Laos": "LAO", "Libya": "LBY",
  "The West Bank and Gaza": "WBG", "Guinea-Bissau": "GNB", "Mali": "MLI", "Saint Kitts and Nevis": "KNA", "West Bank and Gaza": "WBG", "Burma": "MMR",
  "Myanmar": "MMR", "MS Zaandam": "MSZ", "Botswana": "BWA", "Sierra Leone": "SLE", "Burundi": "BDI", "Malawi": "MWI", "Western Sahara": "ESH",
  "South Sudan": "SSD", "Sao Tome and Principe": "STP", "Yemen": "YEM", "Tajikistan": "TJK", "Comoros": "COM", "Lesotho": "LSO"
}

# Last updated 12-24-20
class MyClient(discord.Client):
    # Bot checking in
    # Last updated 12-23-20
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


    # Bot interactions
    # Last updated 12-24-20
    async def on_message(self, message):

        # Prevent bot from replying to itself
        # Last updated 12-23-20
        if message.author.id == self.user.id:
            return

        # Help section, shows different commands and their brief descriptions
        # Last updated 12-29-20
        if message.content.startswith('!help'):
            await message.channel.send('!maps: link to Johns Hopkins and Google coronavirus world maps. '
                                       '\n!report: follow up with a country, ISO, or global\n'
                                       ' \t\t\t for the respective COVID-19 overview.\n'
                                       '!mask: links to educational videos concerning masks.\n'
                                       '!vaccines: link to Wikipedia vaccine page.')

        # This command spawns a link to the Johns Hopkins and Google coronavirus world maps
        # Last updated 12-29-20
        if message.content.startswith('!maps'):
            await message.channel.send('Johns Hopkins: https://coronavirus.jhu.edu/map.html \n'
                                       'Google: https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen')

        # This command spawns a link to Wikipedia page concerning the coronavirus vaccines
        # Last updated 12-29-20
        if message.content.startswith('!vaccines'):
            await message.channel.send('DISCLAIMER: This is according to Wikipedia,\nwhich may not be accurate;'
                                       ' advised to take it with a grain of salt.\n\n'
                                       'Vaccines/candidates: https://en.wikipedia.org/wiki/COVID-19_vaccine#Vaccines \n'
                                       'Vaccine licensure: https://en.wikipedia.org/wiki/COVID-19_vaccine#Licensure')

        # This command spawns a link to educational videos regarding masks
        # Last updated 12-25-20
        if message.content.startswith('!mask'):
            await message.channel.send('Physics behind masks: https://www.youtube.com/watch?v=eAdanPfQdCA\n'
                                       'Why wear masks?: https://www.youtube.com/watch?v=Y47t9qLc9I4')

        # This command creates and outputs a COVID-19 report on a select location or the globe
        # Last updated 12-24-20
        if message.content.startswith('!report'):
            # Removing the command part from the input
            area = message.content.replace('!report ', '')

            # Converting input into ISO format
            # Last updated 12-24-20
            if len(area.title()) != 3 and area.lower() != 'global':
                # Input validation
                try:
                    area = iso[area]
                except KeyError:
                    await message.channel.send('!report command requires a country\'s name or global, try again.')
                    return

            # Retrieve latest date from the covidapi
            # Last updated 12-23-20
            url = 'https://covidapi.info/api/v1/latest-date'
            page = urlopen(url)
            html_bytes = page.read()
            latest_date = html_bytes.decode("utf-8")

            # Stripping the json from the api, both for country and global
            # Last updated 12-24-20
            if area != 'global':
                # Retrieve desired country-specific data
                country_url = 'https://covidapi.info/api/v1/country/' + area + '/' + latest_date
                country_page = urlopen(country_url)
                country_html_bytes = country_page.read()
                country_data = country_html_bytes.decode("utf-8")

                # Converting the extracted json into a dictionary
                data_dict = json.loads(country_data)

                # Formatting the output string
                formatted_data = 'COVID-19 report: ' + area + ', ' + latest_date + ':\n' + \
                                 'Confirmed  |  '.rjust(28) + str(data_dict['result'][latest_date]['confirmed']) + '\n' + \
                                 'Deaths  |  '.rjust(31) + str(data_dict['result'][latest_date]['deaths']) + '\n' + \
                                 'Recovered  |  '.rjust(28) + str(data_dict['result'][latest_date]['recovered'])

            else:
                # Retrieve data for the entire world
                world_url = 'https://covidapi.info/api/v1/global/' + latest_date
                world_page = urlopen(world_url)
                world_html_bytes = world_page.read()
                world_data = world_html_bytes.decode("utf-8")

                # Converting the extracted json into a dictionary
                data_dict = json.loads(world_data)

                # Formatting the output string
                formatted_data = 'COVID-19 report: ' + area + ', ' + latest_date + ':\n' + \
                                 'Confirmed  |  '.rjust(28) + str(data_dict['result']['confirmed']) + '\n' + \
                                 'Deaths  |  '.rjust(31) + str(data_dict['result']['deaths']) + '\n' + \
                                 'Recovered  |  '.rjust(28) + str(data_dict['result']['recovered'])

            # Sending the report
            # Last updated 12-23-20
            await message.channel.send(formatted_data)

# Main function
# Last updated 12-23-20
client = MyClient()
client.run(#token)
