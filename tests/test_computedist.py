from toolbox.distance import haversine

def test_length_of_hello_world():
    assert int(haversine(48.865, 2.380, 48.235, 2.393)) == 70
