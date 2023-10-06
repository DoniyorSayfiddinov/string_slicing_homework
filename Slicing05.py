def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    y=s[-1:-n:-1]
    return y[::-1]
print(main("codeschooluz",4))
