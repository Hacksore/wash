import os
import gettext

LOCALE_DIR = 'locales'
LANGUAGES = ['en_US', 'es_ES']

lang = os.environ.get('LANG', 'en_US')
lang = lang.split('.')[0]

translation = gettext.translation('base', LOCALE_DIR, languages=[lang], fallback=True)
_ = translation.gettext


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
                    print(_('wash your dirty dict'))
            else:
                print(_('wash your dict'))
        except TypeError:
            print(_('skill issue'))

    else:
        print(_("can't wash your dict"))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
