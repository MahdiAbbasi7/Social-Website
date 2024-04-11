from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'descriptions']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        """
        check that the filename ends with a jpg, jpeg, png extension to allow sharing JPEG and PNG files only.
        url = "https://example.com/image.jpg"
        ['https://example.com/image', 'jpg']
        url.rsplit('.', 1)[1]: 'jpg'
        and lower()
        """
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'png', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not '
                                        'match valid image extensions.')
        return url
