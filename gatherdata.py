import sqlite3
import string




class GatherData():

    def __init__(self):
        # connection
        self.conn = sqlite3.connect('worktree.db')

        # cursor
        self.cur = self.conn.cursor()

        #alphabet
        self.alphabet = string.ascii_lowercase

        self.anzsic = {
            "A" : {
                "name" : "Agriculture, Forestry and Fishing",
                "min" : 100,
                "max" : 599,
                "list": [
                {
                  "max": 190,
                  "min": 1,
                  "name": "Agriculture"
                },
                {
                  "max": 290,
                  "min": 200,
                  "name": "Aquaculture"
                },
                {
                  "max": 390,
                  "min": 300,
                  "name": "Forestry and Logging"
                },
                {
                  "max": 490,
                  "min": 400,
                  "name": "Fishing, Hunting and Trapping"
                },
                {
                  "max": 590,
                  "min": 500,
                  "name": "Agriculture, Forestry and Fishing Support Services"
                }
                ]
            },
            "B" : {
                "name" : "Mining",
                "min" : 600,
                "max" : 1099,
                "list": [
                {
                  "max": 690,
                  "min": 600,
                  "name": "Coal Mining"
                },
                {
                  "max": 790,
                  "min": 700,
                  "name": "Oil and Gas Extraction"
                },
                {
                  "max": 890,
                  "min": 800,
                  "name": "Metal Ore Mining"
                },
                {
                  "max": 990,
                  "min": 900,
                  "name": "Non-Metallic Mineral Mining and Quarrying"
                },
                {
                  "max": 1090,
                  "min": 1000,
                  "name": "Exploration and Other Mining Support Services"
                }
                ]
            },
            "C" : {
                "name" : "Manufacturing",
                "min" : 1100,
                "max" : 2599,
                "list": [
                    {
                        "max": 1199,
                        "min": 1100,
                        "name": "Food Product Manufacturing"
                    },
                    {
                        "max": 1299,
                        "min": 1200,
                        "name": "Beverage and Tobacco Product Manufacturing"
                    },
                    {
                        "max": 1399,
                        "min": 1300,
                        "name": "Textile, Leather, Clothing and Footwear Manufacturing"
                    },
                    {
                        "max": 1499,
                        "min": 1400,
                        "name": "Wood Product Manufacturing"
                    },
                    {
                        "max": 1599,
                        "min": 1500,
                        "name": "Pulp, Paper and Converted Paper Product Manufacturing"
                    },
                    {
                        "max": 1699,
                        "min": 1600,
                        "name": "Printing (including the Reproduction of Recorded Media)"
                    },
                    {
                        "max": 1799,
                        "min": 1700,
                        "name": "Petroleum and Coal Product Manufacturing"
                    },
                    {
                        "max": 1899,
                        "min": 1800,
                        "name": "Basic Chemical and Chemical Product Manufacturing"
                    },
                    {
                        "max": 1999,
                        "min": 1900,
                        "name": "Polymer Product and Rubber Product Manufacturing"
                    },
                    {
                        "max": 2099,
                        "min": 2000,
                        "name": "Non-Metallic Mineral Product Manufacturing"
                    },
                    {
                        "max": 2199,
                        "min": 2100,
                        "name": "Primary Metal and Metal Product Manufacturing"
                    },
                    {
                        "max": 2299,
                        "min": 2200,
                        "name": "Fabricated Metal Product Manufacturing"
                    },
                    {
                        "max": 2399,
                        "min": 2300,
                        "name": "Transport Equipment Manufacturing"
                    },
                    {
                        "max": 2499,
                        "min": 2400,
                        "name": "Machinery and Equipment Manufacturing"
                    },
                    {
                        "max": 2599,
                        "min": 2500,
                        "name": "Furniture and Other Manufacturing"
                    }
                ]

            },
            "D" : {
                "name" : "Electricity, Gas, Water and Waste Services",
                "min" : 2600,
                "max" : 2922,
                "list": [
                    {
                      "max": 2699,
                      "min": 2600,
                      "name": "Electricity Supply"
                    },
                    {
                      "max": 2799,
                      "min": 2700,
                      "name": "Gas Supply"
                    },
                    {
                      "max": 2899,
                      "min": 2800,
                      "name": "Water Supply, Sewerage and Drainage Services"
                    },
                    {
                      "max": 2999,
                      "min": 2900,
                      "name": "Waste Collection, Treatment and Disposal Services"
                    }
                ]
            },
            "E" : {
                "name" : "Construction",
                "min" : 3000,
                "max" : 3299,
                "list": [
                {
                  "max": 3099,
                  "min": 3000,
                  "name": "Building Construction"
                },
                {
                  "max": 3199,
                  "min": 3100,
                  "name": "Heavy and Civil Engineering Construction"
                },
                {
                  "max": 3299,
                  "min": 3200,
                  "name": "Construction Services"
                }
                ]
            },
            "F" : {
                "name" : "Wholesale Trade",
                "min" : 3300,
                "max" : 3899,
                "list": [
                    {
                        "max": 3399,
                        "min": 3300,
                        "name": "Basic Material Wholesaling"
                    },
                    {
                        "max": 3499,
                        "min": 3400,
                        "name": "Machinery and Equipment Wholesaling"
                    },
                    {
                        "max": 3599,
                        "min": 3500,
                        "name": "Motor Vehicle and Motor Vehicle Parts Wholesaling"
                    },
                    {
                        "max": 3699,
                        "min": 3600,
                        "name": "Grocery, Liquor and Tobacco Product Wholesaling"
                    },
                    {
                        "max": 3799,
                        "min": 3700,
                        "name": "Other Goods Wholesaling"
                    },
                    {
                        "max": 3899,
                        "min": 3800,
                        "name": "Commission-Based Wholesaling"
                    }
                ]
            },
            "G" : {
                "name" : "Retail Trade",
                "min" : 3900,
                "max" : 4320,
                "list": [
                {
                  "max": 3999,
                  "min": 3900,
                  "name": "Motor Vehicle and Motor Vehicle Parts Retailing"
                },
                {
                  "max": 4099,
                  "min": 4000,
                  "name": "Fuel Retailing"
                },
                {
                  "max": 4199,
                  "min": 4100,
                  "name": "Food Retailing"
                },
                {
                  "max": 4299,
                  "min": 4200,
                  "name": "Other Store-Based Retailing"
                },
                {
                  "max": 4399,
                  "min": 4300,
                  "name": "Non-Store Retailing and Retail Commission-Based Buying and\/or Selling"
                }
                ]
            },
            "H" : {
                "name" : "Accommodation and Food Services",
                "min" : 4400,
                "max" : 4599,
                "list": [
                    {
                      "max": 4499,
                      "min": 4400,
                      "name": "Accommodation"
                    },
                    {
                      "max": 4599,
                      "min": 4500,
                      "name": "Food and Beverage Services"
                    }
                  ]
            },
            "I" : {
                "name" : "Transport, Postal and Warehousing",
                "min" : 4600,
                "max" : 5399,
                "list": [
                {
                  "min": 4600,
                  "name": "Road Transport",
                  "max": 4699
                },
                {
                  "min": 4700,
                  "name": "Rail Transport",
                  "max": 4799
                },
                {
                  "min": 4800,
                  "name": "Water Transport",
                  "max": 4899
                },
                {
                  "min": 4900,
                  "name": "Air and Space Transport",
                  "max": 4999
                },
                {
                  "min": 5000,
                  "name": "Other Transport",
                  "max": 5099
                },
                {
                  "min": 5100,
                  "name": "Postal and Courier Pick-up and Delivery Services",
                  "max": 5199
                },
                {
                  "min": 5200,
                  "name": "Transport Support Services",
                  "max": 5299
                },
                {
                  "min": 5300,
                  "name": "Warehousing and Storage Services",
                  "max": 5399
                }
                ]
            },
            "J" : {
                "name" : "Information Media and Telecommunications",
                "min" : 5400,
                "max" : 6199,
                "list": [
                {
                  "min": 5400,
                  "max": 5499,
                  "name": "Publishing (except Internet and Music Publishing)"
                },
                {
                  "min": 5500,
                  "max": 5599,
                  "name": "Motion Picture and Sound Recording Activities"
                },
                {
                  "min": 5600,
                  "max": 5699,
                  "name": "Broadcasting (except Internet)"
                },
                {
                  "min": 5700,
                  "max": 5799,
                  "name": "Internet Publishing and Broadcasting"
                },
                {
                  "min": 5800,
                  "max": 5899,
                  "name": "Telecommunications Services"
                },
                {
                  "min": 5900,
                  "max": 5999,
                  "name": "Internet Service Providers, Web Search Portals and Data Processing Services"
                },
                {
                  "min": 6000,
                  "max": 6099,
                  "name": "Library and Other Information Services"
                }
                ]
            },
            "K" : {
                "name" : "Financial and Insurance Services",
                "min" : 6200,
                "max" : 6599,
                "list": [
                {
                  "min": 6200,
                  "name": "Finance",
                  "max": 6299
                },
                {
                  "min": 6300,
                  "name": "Insurance and Superannuation Funds",
                  "max": 6399
                },
                {
                  "min": 6400,
                  "name": "Auxiliary Finance and Insurance Services",
                  "max": 6599
                }
                ]
            },
            "L" : {
                "name" : "Rental, Hiring and Real Estate Services",
                "min" : 6600,
                "max" : 6899,
                "list": [
                {
                  "name": "Rental and Hiring Services (except Real Estate)",
                  "max": 6699,
                  "min": 6600
                },
                {
                  "name": "Property Operators and Real Estate Services",
                  "max": 6899,
                  "min": 6700
                }
                ]

            },
            "M" : {
                "name" : "Professional, Scientific and Technical Services",
                "min" : 6900,
                "max" : 7199,
                "list": [
                {
                  "min": 6900,
                  "name": "Professional, Scientific and Technical Services (Except Computer System Design and Related Services)",
                  "max": 6999
                },
                {
                  "min": 7000,
                  "name": "Computer System Design and Related Services",
                  "max": 7099
                }
              ]
            },
            "N" : {
                "name" : "Administrative and Support Services",
                "min" : 7200,
                "max" : 7499,
                "list": [
                    {
                      "name": "Administrative Services",
                      "max": 7299,
                      "min": 7200
                    },
                    {
                      "name": "Building Cleaning, Pest Control and Other Support Services",
                      "max": 7499,
                      "min": 7300
                    }
                  ]
            },
            "O" : {
                "name" : "Public Administration and Safety",
                "min" : 7500,
                "max" : 7999,
                "list": [
                {
                  "min": 7500,
                  "name": "Public Administration",
                  "max": 7599
                },
                {
                  "min": 7600,
                  "name": "Defence",
                  "max": 7699
                },
                {
                  "min": 7700,
                  "name": "Public Order, Safety and Regulatory Services",
                  "max": 7799
                }
                ]
            },
            "P" : {
                "name" : "Education and Training",
                "min" : 8000,
                "max" : 8399,
                "list": [
                {
                  "max": 8099,
                  "min": 8000,
                  "name": "Preschool and School Education"
                },
                {
                  "max": 8199,
                  "min": 8100,
                  "name": "Tertiary Education"
                },
                {
                  "max": 8299,
                  "min": 8200,
                  "name": "Adult, Community and Other Education"
                }
                ]
            },
            "Q" : {
                "name" : "Health Care and Social Assistance",
                "min" : 8400,
                "max" : 8899,
                "list": [
                {
                  "name": "Hospitals",
                  "max": 8499,
                  "min": 8400
                },
                {
                  "name": "Medical and Other Health Care Services",
                  "max": 8599,
                  "min": 8500
                },
                {
                  "name": "Residential Care Services",
                  "max": 8699,
                  "min": 8600
                },
                {
                  "name": "Social Assistance Services",
                  "max": 8799,
                  "min": 8700
                }
                ]
            },
            "R" : {
                "name" : "Arts and Recreation Services",
                "min" : 8900,
                "max" : 9399,
                "list": [
                {
                  "max": 8999,
                  "min": 8900,
                  "name": "Heritage Activities"
                },
                {
                  "max": 9099,
                  "min": 9000,
                  "name": "Creative and Performing Arts Activities"
                },
                {
                  "max": 9199,
                  "min": 9100,
                  "name": "Sports and Recreation Activities"
                },
                {
                  "max": 9299,
                  "min": 9200,
                  "name": "Gambling Activities"
                }
                ]
            },
            "S" : {
                "name" : "Other Services",
                "min" : 9400,
                "max" : 9699,
                "list": [
                {
                  "min": 9400,
                  "max": 9499,
                  "name": "Repair and Maintenance"
                },
                {
                  "min": 9500,
                  "max": 9599,
                  "name": "Personal and Other Services"
                },
                {
                  "min": 9600,
                  "max": 9699,
                  "name": "Private Households Employing Staff and Undifferentiated Goods and Service-Producing Activities of Households forOwn Use"
                }
                ]
            }

        }

        self.abs_stats = {"2012":
            {
"A":	0.6382052473,
"B":	0.7031835206,
"C":	0.6431190199,
"D":	0.7884160757,
"E":	0.7297781761,
"F":	0.6614699332,
"G":	0.6653875329,
"H":	0.8696409899,
"I":	0.7325406455,
"J":	0.8213058419,
"K":	1.0603305343,
"L":	0.869955988,
"M":	0.7927675833,
"N":	0.7118688015,
"O":	0.745363766,
"P":	0.7469645459,
"Q":	1.2264896302,
"R":	0.7016235191,
"S":	0.7731092437
},
"2013":
{
"A":	0.8154279856,
"B":	1.0234113712,
"C":	0.916207506,
"D":	1.2762430939,
"E":	1.0814311255,
"F":	1.0423970202,
"G":	0.9646639349,
"H":	1.3042980879,
"I":	1.0625399965,
"J":	1.2364100693,
"K":	1.3928874863,
"L":	1.2526195069,
"M":	1.1328168578,
"N":	1.0595247684,
"O":	1.0034100597,
"P":	1.2323109626,
"Q":	1.7104913679,
"R":	1.0427302997,
"S":	1.0932127507
},
"2014":
{
"A":	0.7259642699,
"B":	0.7794970986,
"C":	0.9377505803,
"D":	1.1548117155,
"E":	1.1335645958,
"F":	1.005926388,
"G":	0.8804785094,
"H":	1.1597284393,
"I":	1.0196255358,
"J":	1.1059063136,
"K":	1.5363005986,
"L":	1.1962280245,
"M":	1.1099129608,
"N":	1.0519563312,
"O":	0.9467741935,
"P":	1.2089215133,
"Q":	1.4871574422,
"R":	0.9829775736,
"S":	1.1142857143
},
"2015":
{
"A":	0.8206774553,
"B":	0.7927756654,
"C":	0.9859080314,
"D":	1.2449238579,
"E":	1.2495360427,
"F":	1.1088016967,
"G":	0.9276755172,
"H":	1.1936469585,
"I":	1.3033763112,
"J":	1.1293188549,
"K":	1.5061635074,
"L":	1.2201929549,
"M":	1.1692964868,
"N":	1.2048192771,
"O":	1.0041493776,
"P":	1.25976458,
"Q":	1.5191191191,
"R":	1.0765445599,
"S":	1.1815642458
}
}

    def finish(self):
        self.conn.close()

    def get_count_by_anzsic_code_range(self, a, b):
        get = "SELECT COUNT(*) FROM neisdatagovhack WHERE anzsic_code > {0} and anzsic_code < {1}".format(a, b)

        quantity = self.cur.execute(get).fetchone()
        # (778,)

        return quantity[0]

    def get_count_by_anzsic_code_range_and_year(self, a, b, yr):
        get = "SELECT COUNT(*) FROM neisdatagovhack WHERE anzsic_code > {0} and anzsic_code < {1} AND " \
              "start_date like '%{2}%'".format(a, b,  self.clean_year(yr))

        quantity = self.cur.execute(get).fetchone()
        # (778,)

        return quantity[0]

    def compare(self, a, b, yr, success):
        '''anzsic range, year start, success'''


        get = "SELECT COUNT(*) FROM neisdatagovhack WHERE anzsic_code > {0} AND anzsic_code < {1}" \
              " AND start_date like '%{2}%' AND successful = '{3}'".format(a, b, self.clean_year(yr), success)



        quantity = self.cur.execute(get).fetchone()
        # (778,)

        return quantity[0]


    def query(self, request):
        ''' a dictionary of requests'''

        if request.get("min") == None or request.get("max") == None:
            return

        the_request = "SELECT COUNT(*) FROM neisdatagovhack WHERE "

        the_request += "anzsic_code >= {0} AND anzsic_code <= {1}".format(request.get("min"), request.get("max"))

        if request.get("year"):
            for i in request.get("year"):

                the_request += " OR start_date like '%-{0}%'".format(self.clean_year(i))

        if request.get("state"):
            for i in request.get("state"):
                the_request += " OR state = '{0}'".format(i)

        # if request.get("industry"):
        #     for i in request.get("industry"):
        #         the_request += " OR industry = '{0}'".format(i)

        if request.get("age"):
            for i in request.get("age"):
                the_request += " OR age_group = '{0}'".format(i)

        if request.get("success"):
            the_request += " AND successful = '{0}'".format(request.get("success"))



        answer = self.cur.execute(the_request).fetchone()
        # print(the_request)
        # print(answer)

        return answer[0]


    def clean_year(self, yrstart):
        '''2 digit year'''
        if yrstart == 12:
            yrstart = '-12'
        elif yrstart == 13:
            yrstart = '-13'
        elif yrstart == 14:
            yrstart = '-14'
        elif yrstart == 15:
            yrstart = '-15'
        elif yrstart == 16:
            yrstart = '-16'

        return(yrstart)



    def build_data(self, form_info):
        '''{'year': ['13'], 'industry': ['B'], 'age': ['20-24'], 'state': ['VIC']}'''

        data = []
        data.append(['Industry', 'Parent', 'Market Size', 'Market success'])
        data.append(['Global', '', 0, 0])

        infoblock = self.anzsic.copy()
        absblock = self.abs_stats.copy()
        alphabet = self.alphabet


        if form_info.get("industry"):
            alphabet = ''
            for k in form_info.get("industry"):

                alphabet += k

        # build request query info from form here
        request = {}
        if form_info.get("year"):
            request["year"] = form_info.get("year")  # should be arrays
        if form_info.get("state"):
            request['state'] = form_info.get("state")
        if form_info.get('age'):
            request['age'] = form_info.get("age")

        for i in alphabet:

            if i == 't':
                break

            info = infoblock.get(i.upper())
            if info == None:
                continue
            # build query dict

            request["min"] = info.get('min')
            request["max"] = info.get('max')

            value = self.query(request)

            if value < form_info.get("lowerlimit") or value > form_info.get("upperlimit"):
                infoblock.pop(i.upper())
                continue

            request['success'] = 'Y'
            success1 = self.query(request)
            request['success'] = 'N'
            success2 = self.query(request)

            absave = 0
            if form_info.get("absyear"):
                for l in form_info.get("absyear"):
                    a = []
                    a.append(absblock.get(l).get(i.upper()))
                    absave = sum(a)/len(a)

            else:
                for l in absblock:
                    a = []
                    a.append(absblock.get(l).get(i.upper()))
                    absave = sum(a) / len(a)

            try:
                dsuccess = success1 / success2 - absave
            except:
                continue

            data.append([info.get('name'), 'Global', value, dsuccess])

        # sub areas:
        for i in alphabet:

            if i == 't':
                break

            info = infoblock.get(i.upper())
            if info == None:
                continue


            for j in info.get('list'):

                request["min"] = j.get('min')
                request["max"] = j.get('max')

                value = self.query(request)

                request['success'] = 'Y'
                success1 = self.query(request)
                request['success'] = 'N'
                success2 = self.query(request)

                absave = 0
                if form_info.get("absyear"):
                    for l in form_info.get("absyear"):
                        a = []
                        a.append(absblock.get(l).get(i.upper()))
                        absave = sum(a) / len(a)

                else:
                    for l in absblock:
                        a = []
                        a.append(absblock.get(l).get(i.upper()))
                        absave = sum(a) / len(a)

                try:
                    dsuccess = success1 / success2 - absave
                except:
                    continue

                data.append([j.get('name'), info.get('name'), value, dsuccess])


        return data
