class User():
    def __init__(self, id_user, email, company, region):
        self.id_user = self.validate_user(id_user)
        self.email = self.validate_email(email)
        self.company = company
        self.region = region
    
    def validate_user(self, id_user):
        try:
            if is_integer(id_user):
                return True
            else:
                raise(ValueError)
                return False
        except Exception as e:
            print(e)

    #TODO Implement some regex email validation, if there isn't some built-in email validation widget in streamlit
    def validate_email(self, email):
        return None
    
    def show_user(self):
        print(f"Dados do usuário: {1}, {2}, {3}".format(self.id_user, self.company, self.region))



    #todo def show_observations(self)

