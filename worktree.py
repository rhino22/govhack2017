from flask import Flask, render_template, request
import gatherdata
import json
from worktreeforms import TreeForm

app = Flask(__name__)
app.secret_key = 'QEADSFXZCadgdsf'



# @app.route('/')
# def index():
#
#     form = TreeForm()
#
#     return render_template("one_page.html", form=form)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        form = TreeForm()

        return render_template("grayscale.html", form=form)

    form = TreeForm(request.form)

    if request.method == 'POST' and form.validate():
        pass
    else:
        return "Failed Validation"

    form_info = {'lowerlimit': form.lowerlimit.data, 'upperlimit': form.upperlimit.data}

    if form.state.data == ['QLD', 'NSW', 'VIC', 'TAS', 'SA', 'NT', 'ACT', 'WA']:
        pass
    else:
        form_info['state'] = form.state.data

    if form.year.data == ['12', '13', '14', '15', '16']:
        pass
    else:
        form_info['year'] = form.year.data

    if form.industry.data == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                              'R', 'S']:
        pass
    else:
        form_info['industry'] = form.industry.data

    if form.age.data == ['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60+']:
        pass
    else:
        form_info['age'] = form.age.data

    if form.absyear.data == ['2012', '2013', '2014', '2015']:
        pass
    else:
        form_info['absyear'] = form.absyear.data

    g = gatherdata.GatherData()
    this = g.build_data(form_info)

    g.finish()
    # print(json.dumps(this))

    return render_template("grayscale.html", form=form, data=json.dumps(this))


# @app.route('/data', methods=['GET', 'POST'])
# def data():
#
#     if request.method == 'GET':
#         form = TreeForm()
#
#         return render_template("one_page.html", form=form)
#
#     form = TreeForm(request.form)
#
#     if request.method == 'POST' and form.validate() :
#         pass
#     else:
#         return "Failed Validation"
#
#     form_info = {'lowerlimit': form.lowerlimit.data, 'upperlimit': form.upperlimit.data}
#
#     if form.state.data == ['QLD', 'NSW', 'VIC', 'TAS', 'SA', 'NT', 'ACT', 'WA']:
#         pass
#     else:
#         form_info['state'] = form.state.data
#
#     if form.year.data == ['12', '13', '14', '15', '16']:
#         pass
#     else:
#         form_info['year'] = form.year.data
#
#     if form.industry.data == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
#                               'R', 'S']:
#         pass
#     else:
#         form_info['industry'] = form.industry.data
#
#     if form.age.data == ['15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60+']:
#         pass
#     else:
#         form_info['age'] = form.age.data
#
#     if form.absyear.data == ['2012', '2013', '2014', '2015']:
#         pass
#     else:
#         form_info['absyear'] = form.absyear.data
#
#
#     g = gatherdata.GatherData()
#     this = g.build_data(form_info)
#
#     g.finish()
#     print(json.dumps(this))
#
#     return render_template("one_page.html", form=form, data=json.dumps(this))

    # return json.dumps(this)



if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=80)

    # app.run(debug=True, host='127.0.0.1', port=5000)