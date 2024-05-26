from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import ContactForm

contact_bp = Blueprint('contact_bp', __name__, template_folder='templates')


@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Here you can process the form data, such as sending an email
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact_bp.contact'))
    return render_template('contact.html', form=form)
