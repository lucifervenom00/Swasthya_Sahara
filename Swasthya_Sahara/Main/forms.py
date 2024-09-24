from django import forms
from .models import JournalEntry,Blog,Category
choice=Category.objects.all().values_list('name','name')
choice_list=[]
for item in choice:
    choice_list.append(item)
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['category']

        widget=forms.Select(choices=choice_list,attrs={'class':'form-control'})
    
class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['content']