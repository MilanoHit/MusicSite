from django import forms
from MusicApp.models import MyMusicAppUser, Album, Review
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


class MyMusicAppCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyMusicAppUser
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(
        strip = False,
        widget= forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': "Password"}))


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        exclude = ('profile', 'average_rating')
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'genre': forms.Select(attrs={'placeholder': 'Genre'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }
        labels = {
            'album_name': 'Album Name',
            'artist': 'Artist',
            'genre': 'Genre',
            'description': 'Description',
            'image': 'Image',
            'price': 'Price',
        }


class AlbumDeleteForm(AddAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for(_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ('profile', 'album')
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'rating': forms.Select(attrs={'placeholder': 'Rating'}),
        }
        labels = {
            'description': 'Description',
            'rating': 'Rating',
        }

class MyMusicAppUserEdit(forms.ModelForm):
    class Meta():
        model = MyMusicAppUser
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'gender')
        exclude = ('password',)
        labels= {'username': "Username",
                 'first_name': "First Name:",
                 'last_name': 'Last Name:',
                 'email': 'Email',
                 'profile_picture': 'Image',
                 'gender': "Gender"
                 }