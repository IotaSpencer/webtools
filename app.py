import flask
from flask import Flask, render_template
import yaml

app = Flask(__name__)


@app.before_request
def before_request():
    flask.g.site = yaml.load(open('./data/site.yml', 'r').read(), Loader=yaml.Loader)


@app.route('/')
def root_index():  # put application's code here
    flask.g.page = yaml.load(open('./data/index.yml', 'r').read(), Loader=yaml.Loader)
    return render_template('index.html')


@app.route('/tools/')
def tools_index():
    flask.g.page = yaml.load(open('./data/tools.yml', 'r').read(), Loader=yaml.Loader)
    return render_template('tools/index.html')


@app.route('/tools/<tool_name>')
def tools(tool_name):
    flask.g.page = yaml.load(open('./data/tools.yml', 'r').read(), Loader=yaml.Loader)

    tools_obj = yaml.load(open('./data/tools.yml', 'r').read(), Loader=yaml.Loader)['tools']
    tool_slugs = [tool['slug'] for tool in tools_obj]
    if tool_name in tool_slugs:
        return render_template('tools/tool.html')
    else:
        return render_template('tools/index.html', tool_name=tool_name, error_404=True)


if __name__ == '__main__':
    app.run(debug=True)
