from _decorators import input_error

@input_error
def add_contact(args, contacts):
    if len(args)!=2:
        raise ValueError 
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args)!=2:
        raise ValueError 
    name, new_phone = args
    if name in contacts:
        contacts[name]=new_phone
        return f"Contact {name} updated"
    else:
        raise KeyError(f"{name} not found") 
    
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        raise KeyError(f"{name} not found") 

       
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

@input_error    
def delete_contact(args,contacts):
    name, phone = args
    if name in contacts and contacts[name] == phone:
        del contacts[name]
        return "Contact delete."     
    else:
        raise KeyError(f"{name} not found")
