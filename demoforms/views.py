from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import FormView
from demoforms.forms import CommentForm

import openai

class CommentFormView(FormView):
    template_name = "comment.html"
    form_class = CommentForm
    success_url = "comment"

    def form_valid(self, form):
        form.log_data()
        messages.success(self.request, 'Form submitted successfully')

        # Get the user's question from the form
        user_question = form.cleaned_data['comment']

        # Use OpenAI to generate a response
        client = openai.OpenAI()
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot that is an expert in the online Python coding and hosting platform, PythonAnywhere."},
                {"role": "user", "content": user_question}
            ]
        )

        # Extract the AI's reply from the OpenAI response
        ai_reply = completion.choices[0].message.content

                # Add the AI's reply to the context
        context = self.get_context_data()
        context['ai_reply'] = ai_reply

        return self.render_to_response(context)
    


"""         # Get the form values and add them to the context
        context = self.get_context_data()
        context['form_values'] = {
            'name': form.cleaned_data['name'],
        }

        return self.render_to_response(context)
 """