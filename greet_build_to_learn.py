from random import randint
def greetings():
    greet=['hi hello','hello guy ','hey man','yo bro','vanankkam thozhA']
    n=randint(0,len(greet)-1 )
    return(greet[n])
a=greetings()
print(a,"thanks for using me")

