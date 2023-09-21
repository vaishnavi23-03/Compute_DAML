def fun(s):
    if s=="":
        return False
    
    if s.count('.')!=1 or s.count('@')!=1:
        return False
    if s[0]=='@' or s[0]=='-'or s[0]=='_':
        return False
    extension=""
    username,s1=s.split('@')
    websitename,extension=s1.split('.')
    
    if len(websitename)==0 or len(username)==0 or len(extension)==0:
        return False
    
       
    for u in username:
        if ((97<=ord(u)<=122) or (65<=ord(u)<=90) or (u=='-') or (u=='_') or (48<=ord(u)<=57)):
            username_check=True
        else:
            return False
    
    for u in websitename:
        if ((97<=ord(u)<=122) or (65<=ord(u)<=90) or (48<=ord(u)<=57)):
            websitename_check=True
        else:
            return False
   
    if len(extension)>3:
        return False
    else:
        for u in extension:
            if ((97<=ord(u)<=122) or (65<=ord(u)<=90)):
                extension_check=True
            else:
                return False
    
    return True
        
            

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)