def assert_equals(var1, var2, var3):
    if var1 == var2:
        return print("Succeeded : "+str(var3)+", "+str(var1)+", "+str(var2))
    else:
        return print("failed : "+str(var3)+", "+str(var1)+", "+str(var2))
