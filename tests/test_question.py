import pytest
import requests
import sys
import numpy as np
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tasks.task_manager import *

def test_define_scalar_energy():
    assert isinstance(define_scalar_energy(), (int, float))

def test_define_crime_vector():
    vec = define_crime_vector()
    assert isinstance(vec, np.ndarray)
    assert vec.ndim == 1

def test_define_energy_matrix():
    mat = define_energy_matrix()
    assert isinstance(mat, np.ndarray)
    assert mat.ndim == 2

def test_add_crime_vectors():
    v1 = np.array([1,2])
    v2 = np.array([3,4])
    result = add_crime_vectors(v1, v2)
    assert np.array_equal(result, np.array([4,6]))

def test_subtract_energy_matrices():
    m1 = np.array([[5,5],[5,5]])
    m2 = np.array([[1,2],[3,4]])
    assert np.array_equal(subtract_energy_matrices(m1, m2), np.array([[4,3],[2,1]]))

def test_transpose_sensor_matrix():
    mat = np.array([[1,2],[3,4]])
    trans = transpose_sensor_matrix(mat)
    assert np.array_equal(trans, np.array([[1,3],[2,4]]))

def test_dot_energy_source():
    mat = np.array([[1,2],[3,4]])
    vec = np.array([1,1])
    result = dot_energy_source(mat, vec)
    assert np.array_equal(result, np.array([3,7]))

def test_why_linear_algebra_is_important():
    answer = why_linear_algebra_is_important()
    assert isinstance(answer, str)
    assert len(answer) > 10

def test_average_crime_rate():
    vec = np.array([5, 15, 25])
    assert average_crime_rate(vec) == 15.0

def test_max_energy_usage():
    mat = np.array([[1,2,3], [10,10,10], [5,5,5]])
    assert max_energy_usage(mat) == 1  # index of max row

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://edugen-backend-487d2168bc6c.herokuapp.com/projectLog/"
    payload = {
        "user_id": 34,
        "project_id": 200,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()