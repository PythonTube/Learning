email = input("What is your email adress?: ").strip() # Get user email adress

user = email[:email.index("@")]  # Slice out user name

domain = email[email.index("@")+1:] # Slice domain name

output = "Your username is {} and your domain name is {}".format(user, domain) # Format message

print(output)
