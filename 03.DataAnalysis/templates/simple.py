from flask import Blueprint, render_template

#simple_bp = blueprint('simple_bp', __name__, template_)
simple_bp = Blueprint('simple_bp', __name__)

@simple_bp.route('/')
def simple():
    return render_template('simple.html')