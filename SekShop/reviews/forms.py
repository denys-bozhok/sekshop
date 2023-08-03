from django.forms import ModelForm

from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Enter your name :',
            'review_txt': 'Write your review :',
            'tags': 'Enter tags by coma :', 
            'rating':'Choose rating :',
            'isMember': 'isMember'
        }
        
        error_messages = {
            'uesr_name': {
                'reauired': 'Your name is empty',
                'max_length': 'So long name'
                }
        }