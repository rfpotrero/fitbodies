from django.shortcuts import render, redirect

from .forms import ContactForm


def add_contact(request):
    """
    View to process contacts 
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('contact_success')
    else:

        form = ContactForm()
        template = 'contact/add_contact.html'
        context = {
            'form': form
        }

        return render(request, template, context)


def contact_success(request):
    """
    View to generate a sucess page
    """

    template = 'contact/contact_success.html'
    return render(request, template)

