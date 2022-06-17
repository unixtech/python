def main():
    greet = "Hi"
    """
    Use f-strings for win! :)
    """

    # Adding spaces to Left
    print(f"{greet:>10}")
    print(f"{greet:<10}")
    print(f"{greet:_^10}")

    """
    Print numbers with various allign
    """
    print(f"{3.4:10}")
    print(f"{3820.45:2}")
    print(f"{10000:,.1f}")
    print(f"{10000:_.1f}")
    print(f"{0.34576:%}")
    print(f"{0.34576:.2%}")


if __name__ == "__main__":
    main()
