def wash(input_dict: dict) -> None: 
    if input_dict is not None:
        print('get a dict')

    if isinstance(input_dict, dict):
        try:
            if input_dict['dirty'] != True:
                pass
            else:
                print('wash your dict')
        finally:
            print("wash your dict")

    else:
        print("can't wash your dict")
    