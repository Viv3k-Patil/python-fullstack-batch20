try:
    from colorama import Fore, init
    init(autoreset=True)
    _HAS_COLOR = True
except ImportError:
    # Falls back to plain text if colorama isn't installed
    _HAS_COLOR = False

    class _NoColor:
        def __getattr__(self, name):
            return ""

    Fore = _NoColor()


def print_success(message):
    print(Fore.GREEN + "✅ " + message)


def print_error(message):
    print(Fore.RED + "❌ " + message)


def print_info(message):
    print(Fore.CYAN + "ℹ️  " + message)


def print_menu(title, options):
    print(Fore.YELLOW + f"\n===== {title} =====")
    for key, label in options.items():
        print(f"{key}. {label}")
    print(Fore.YELLOW + "=" * (len(title) + 12))
