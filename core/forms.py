from django.conf import settings
from django.core.mail import EmailMessage
from django.forms import (
    CharField, MultiValueField, EmailField, Form, Textarea)
from django.http import JsonResponse
from django.template import Context
from django.template.loader import get_template


class ContactForm(Form):
    contact_name = CharField(required=True)
    contact_email = EmailField(required=True)
    contact_phone = CharField(required=True)
    contact_content = CharField(required=True, widget=Textarea)

    def send(self):
        print('#'*50)
        print(settings.EMAIL_DL_FROM)
        print(settings.EMAIL_DL_TO)
        form = super(ContactForm, self)
        response = {'errors': '', 'response': ''}
        
        if self.is_valid():
            contact_name = self.cleaned_data['contact_name']
            contact_email = self.cleaned_data['contact_email']
            contact_phone = self.cleaned_data['contact_phone']
            form_content = self.cleaned_data['contact_content']

            # Email the profile with the 
            # contact information
            template = get_template('core/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_phone': contact_phone,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                settings.EMAIL_DL_FROM,  # from
                [settings.EMAIL_DL_TO], # to
                headers = {'Reply-To': contact_email }
            )
            email.send()
            response['response'] = {'status': 'success'}
            return JsonResponse(response)

        else:
            response['errors'] = self.errors
            return JsonResponse(response) 