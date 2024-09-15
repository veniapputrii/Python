#4. raise => used to raise an error. These errors are visible in the traceback and they cancel
#the execution of the program if not handled properly

enter = 2
if not type(enter) is int:
    raise TypeError("Only integers are allowed")

#✨ more ✨ 
#int => integer
#"" => string
#directly input amount of number without symbol "" then operator will read it as int
