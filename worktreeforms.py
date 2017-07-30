from flask_wtf import Form
from wtforms import SelectMultipleField, IntegerField

from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange, Optional, regexp
# https://wtforms.readthedocs.io/en/latest/validators.html

class TreeForm(Form):

    year = SelectMultipleField( label="Year", choices=[('12', '2012'), ('13', '2013'),
                                                       ('14', '2014'), ('15', '2015'), ('16','2016')],
                                default=['12'])
                                # default=['12', '13','14', '15', '16'])
    state = SelectMultipleField( label="State", choices=[('QLD', 'QLD'), ('NSW', 'NSW'), ('VIC', 'VIC'), ('TAS', 'TAS'),
                                          ('SA', 'SA'), ('NT', 'NT'), ('ACT', 'ACT'), ('WA', 'WA')],
                                    default=['QLD', 'NSW', 'VIC', 'TAS', 'SA', 'NT', 'ACT', 'WA'])
    industry = SelectMultipleField( label="Industry", choices = [
("A", "Agriculture, Forestry and Fishing"),
("B", "Mining"),
("C", "Manufacturing"),
("D", "Electricity, Gas, Water and Waste Services"),
("E", "Construction"),
("F", "Wholesale Trade"),
("G", "Retail Trade"),
("H", "Accommodation and Food Services"),
("I", "Transport, Postal and Warehousing"),
("J", "Information Media and Telecommunications"),
("K", "Financial and Insurance Services"),
("L", "Rental, Hiring and Real Estate Services"),
("M", "Professional, Scientific and Technical Services"),
("N", "Administrative and Support Services"),
("O", "Public Administration and Safety"),
("P", "Education and Training"),
("Q", "Health Care and Social Assistance"),
("R", "Arts and Recreation Services"),
("S", "Other Services")],
                                    default=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R",
                                             "S"])
    age = SelectMultipleField( label="Age Group", choices = [("15-19", "15_19"),
                                        ("20-24", "20_24"),
                                        ("25-29", "25_29"),
                                        ("30-34", "30_34"),
                                        ("35-39", "35_39"),
                                        ("40-44", "40_44"),
                                        ("45-49", "45_49"),
                                        ("50-54", "50_54"),
                                        ("55-59","55_59"),
                                        ("60+", "60+")]
                               ,
                               default=["15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59", "60+"])

    lowerlimit = IntegerField(label="Lower Sample limit (0-5000)", validators=[NumberRange(min=0, max=5000,
                                                                                          message="no")])
    upperlimit = IntegerField(label="Upper Sample limit (10-80000)", validators=[NumberRange(min=10, max=80000,
                                                                                       message="no")])


    absyear = SelectMultipleField(label="Years, ABS data", choices=[('2012', '2012'), ('2013', '2013'),
                                                      ('2014', '2014'), ('2015', '2015')],
                                  default=['2012'])
                               # default=['2012','2013','2014','2015'])
