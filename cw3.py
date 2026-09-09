has_account=True
email_verified=False
can_login=has_account and email_verified
email="varshini@gmail.com"
is_email_valid= "@" in email
user_age=17
is_age_valid=user_age>=18
can_login_final=has_account and email_verified and is_email_valid and is_age_valid
print("can login",can_login,"Is email verfied",is_email_valid,"Is age valid",is_age_valid,"can login",can_login_final)
print(has_account is True)



    