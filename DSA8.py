def outer_function():
    outer_variable = "Hello"

    def inner_function():
        nonlocal outer_variable
        print(outer_variable)  # Accessing the outer variable

    inner_function()

print(outer_function().outer_variable)