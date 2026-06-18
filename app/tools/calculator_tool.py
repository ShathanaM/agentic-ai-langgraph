def calculator_tool(expression):

    try:
        result = eval(expression)

        return str(result)

    except Exception as e:

        return str(e)