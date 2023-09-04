def wash(input_dict: dict) -> None:
    """
    >>> wash({})
    wash your dict
    >>> wash({'dirty': True})
    wash your dirty dict
    >>> wash(None)
    get a dict
    can't wash your dict
    """

    if input_dict is None:
        print('get a dict')

    if isinstance(input_dict, dict):
        try:
            if 'dirty' in input_dict:
                if input_dict['dirty'] != True:
                    pass
                else:
                    print('wash your dirty dict')
            else:
                print('wash your dict')
        except TypeError:
            print('skill issue')

    else:
        print("can't wash your dict")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
