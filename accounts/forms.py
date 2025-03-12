from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from allauth.account.forms import SignupForm
from craftsmen.models import Craftsman
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )

class CustomSignupForm(SignupForm):
    username = forms.CharField(
        max_length=30, 
        label="Username",
        widget=forms.TextInput(attrs={"placeholder": "Enter your username"})
    )
    phone = forms.CharField(
        max_length=15, 
        label="Phone Number",
        widget=forms.TextInput(attrs={"placeholder": "Enter your phone number"})
    )
    terms = forms.BooleanField(required=True, label="I Agree To Terms & Conditions.")
    is_craftsman = forms.BooleanField(
        required=False,
        label="Are you a craftsman?",
        help_text="Check this box if you are a craftsman."
    )

    def save(self, request):
        # Save the user using the parent class's save method
        user = super().save(request)
        
        # Update the user's username and phone
        user.username = self.cleaned_data["username"]
        user.phone = self.cleaned_data["phone"]
        user.is_craftsman = self.cleaned_data.get("is_craftsman", False)  # Ensure this line exists
        user.save()

        # Create a Craftsman profile if the user is a craftsman
        if self.cleaned_data.get("is_craftsman"):
            Craftsman.objects.create(user=user)

        return user