import os

import pytest as pytest

if __name__ == '__main__':
    pytest.main()


os.system('allure generate ./temps -o ./res --clean')