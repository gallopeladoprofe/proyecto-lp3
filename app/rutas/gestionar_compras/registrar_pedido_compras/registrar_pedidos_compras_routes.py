from flask import Blueprint, render_template

pdcmod = Blueprint('pdcmod', __name__, template_folder='templates')

@pdcmod.route('/pedidos-index')
def pedidos_index():
    return render_template('pedidos-index.html')