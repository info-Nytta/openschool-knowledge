import pytest
from utils import osszead, kivon, szoroz, osztas, atlag, egyedi, leggyakoribb, szavak_szama


# 13.1 – Alap műveletek

class TestOsszead:
    def test_pozitiv(self):
        assert osszead(2, 3) == 5

    def test_negativ(self):
        assert osszead(-1, -2) == -3

    def test_nulla(self):
        assert osszead(0, 0) == 0


class TestKivon:
    def test_pozitiv(self):
        assert kivon(10, 3) == 7

    def test_negativ_eredmeny(self):
        assert kivon(3, 10) == -7


class TestSzoroz:
    def test_pozitiv(self):
        assert szoroz(4, 5) == 20

    def test_nullaval(self):
        assert szoroz(100, 0) == 0


# 13.2 – Osztás és kivétel

class TestOsztas:
    def test_egesz(self):
        assert osztas(10, 2) == 5.0

    def test_tort(self):
        assert osztas(7, 2) == 3.5

    def test_nullaval(self):
        with pytest.raises(ValueError, match="Nullával"):
            osztas(10, 0)


# 13.3 – Lista műveletek

class TestAtlag:
    def test_egeszek(self):
        assert atlag([1, 2, 3, 4, 5]) == 3.0

    def test_egy_elem(self):
        assert atlag([42]) == 42.0

    def test_ures(self):
        with pytest.raises(ValueError):
            atlag([])


class TestEgyedi:
    def test_duplikatumok(self):
        eredmeny = egyedi([1, 2, 2, 3, 3, 3])
        assert sorted(eredmeny) == [1, 2, 3]

    def test_ures(self):
        assert egyedi([]) == []


# 13.4 – Szótár műveletek

class TestLeggyakoribb:
    def test_alap(self):
        assert leggyakoribb([1, 2, 2, 3, 3, 3]) == 3

    def test_szoveg(self):
        assert leggyakoribb(["a", "b", "a"]) == "a"


class TestSzavakSzama:
    def test_alap(self):
        eredmeny = szavak_szama("alma korte alma")
        assert eredmeny["alma"] == 2
        assert eredmeny["korte"] == 1

    def test_ures(self):
        assert szavak_szama("") == {}
