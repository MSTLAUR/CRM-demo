from django import forms
from .models import Item, newProductModels



class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ['item_name','item_desc', 'item_price']
        
        
        
class userProductForm(forms.ModelForm):
    class Meta:
        model = newProductModels
        fields = ['name', 'city', 'price', 'category', 'currency',
               'description', 'video_link']  # Fields you want users to edit
       
        '''  
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mb-5  bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'Enter your name'
            }),
            'city': forms.TextInput(attrs={
                'class': ' mb-5 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
                'placeholder': 'city'
            }),
            'price': forms.TextInput(attrs={
                'class': ' m-5 form-control rounded-lg p-2 border-gray-300',
                'placeholder': 'price'
            }),
        }
        '''