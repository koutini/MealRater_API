from allauth.account.adapter import DefaultAccountAdapter
from MealApp.models import Profile


class RegisterAdapter(DefaultAccountAdapter):

    def save_profile(self, user, data):
        """
        method to save profile.
        """
        profile_data = {}
        phone_number = data.get("phone_number", False)
        description = data.get("description", False) 
        cin = data.get("cin", False)
        date_of_birth = data.get("date_of_birth", False)
        if phone_number: 
            profile_data.update(phone_number=phone_number)
        if description: 
            profile_data.update(description=description) 
        if cin: 
            profile_data.update(cin=cin)
        if date_of_birth:
            profile_data.update(date_of_birth=date_of_birth)     
        profile_obj = Profile.objects.update_or_create(user=user,  defaults=profile_data)
        return profile_obj

    def save_user(self, request, user, form, commit=True):
        """
        overriding this method to update the corresponding profile of a specific user.
        """
        user = super(RegisterAdapter, self).save_user(request, user, form, commit=True)
        data = form.cleaned_data
        try:
            self.save_profile(user, data)
        except Exception:
            user.delete()
            return None
        return user

