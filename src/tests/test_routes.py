import pytest

from src.calculations.vogel_ipr import calc_ipr
from src.models.models import IprCalcResponse


@pytest.fixture
def generate_data_for_tests():
    return {
        "p_res": 250,
        "wct": 50,
        "pi": 1,
        "pb": 150
    }


def test_calc_model_success(api_client, generate_data_for_tests):
    expected_result = IprCalcResponse.parse_obj(
        calc_ipr(**generate_data_for_tests)
    ).dict()

    actual_result = api_client.post(
        "http://localhost:8002/ipr/calc",
        json=generate_data_for_tests
    ).text

    assert eval(actual_result) == expected_result
