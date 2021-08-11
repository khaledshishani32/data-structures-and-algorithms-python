def validate_brackets(str):
    string=list(str)
    brackets=['{','[','(']
    dummy=[]
    for item in string:
        if item in brackets:
            dummy+=[item]
        else:
            delete_item= dummy.pop()
            if  delete_item== '(':
                if item != ")":
                    return False
            if delete_item == '{':
                if item != "}":
                    return False
            if delete_item == '[':
                if item != "]":
                    return False
            if dummy:
                return False
            else:
                return True


print(validate_brackets("[({}]"))