from app import get_status


def test_status():
    assert get_status() == "API configured"
