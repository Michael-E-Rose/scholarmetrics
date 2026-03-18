from scholarmetrics import AuthorMetrics

am_1 = AuthorMetrics(scopus_id="7004460308", refresh=30)
am_2 = AuthorMetrics(scopus_id="7402594891", start_year=2015, end_year=2025, refresh=30)

def test_len():
    assert len(am_1.h_index) == 2026 - 1995 + 1
    assert len(am_2.h_index) == 2025 - 2015 + 1

def test_g_index():
    assert am_1.g_index[1996] == 2
    assert am_2.g_index[2015] == 9

def test_h_index():
    assert am_1.h_index[2024] == 120
    assert am_2.h_index[2024] == 22

def test_euclidean_distance():
    assert am_1.euclidean_distance[2024] == 15074.703944024905
    assert am_2.euclidean_distance[2024] == 307.03094306600434