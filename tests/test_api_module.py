from unittest.mock import MagicMock, patch

from src.api_class_module import ApiHH


@patch("requests.get")
def test_get_vacancies(mock_get, get_vac_object_list):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [{"id": 1, "name": "Python"}]}
    mock_get.return_value = mock_response
    vacancies = ApiHH().get_vacancies("Python")
    assert len(vacancies) == 20
    assert vacancies[0]["name"] == "Python"
