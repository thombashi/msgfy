import msgfy

def main():
    try:
        raise ValueError("example message")
    except ValueError as e:
        print(msgfy.to_error_message(e, "{func_name}: {error_msg}"))

main()

