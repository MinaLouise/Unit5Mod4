from django.test import SimpleTestCase

# Create your tests here.

# Warmup 1
class TestWarmup2(SimpleTestCase):
    def test_front_times_ChoCho(self):
        response = self.client.get("/warmup-2/font-times/?csrfmiddlewaretoken=B0W78GWn6IqQJSAM5Uhorn2TAKCimkJKTpj1jdNnTtetifwpnYQ3N30BYoLiJDFv&word=Chocolate&n=2")
        self.assertContains(response, "ChoCho")

    def test_front_times_AbcAbcAbc(self):
        response = self.client.get("/warmup-2/font-times/?csrfmiddlewaretoken=ORDzFgmrHeajzxVpmwlJMHVfIrM4OoxZ6g0tQNdruZYW8UR2EAUo8nTX65V4bHtK&word=Abc&n=3")
        self.assertContains(response, "AbcAbcAbc")

    def test_front_times_AAAA(self):
        response = self.client.get("/warmup-2/font-times/?csrfmiddlewaretoken=tGtTxjw0Gy52lUxM56dE4WiUs3Fzlc2YL5QNIQn0tjTFUhtpnaMjqCgCQHOzIvYJ&word=A&n=4")
        self.assertContains(response, "AAAA")


# Warmup 2
class TestStringPosition(SimpleTestCase):
    def test_teen_4(self):
        response = self.client.get("/logic-2/no-teen-sum/?csrfmiddlewaretoken=OQZBPJxogDHes6xGLbHCfzONWEXds8ck6fmv0goo3ovR1ttj3fghBfMvki6dPr85&a=1&b=2&c=3")
        self.assertContains(response, "6")

    def test_teen_0(self):
        response = self.client.get("/logic-2/no-teen-sum/?csrfmiddlewaretoken=lJnWGjFitSsVWINq6K7lr1F1cntc9eCZD8KQRQwigDgyv5J3oOG0NHDJA1CcwxyK&a=2&b=13&c=1")
        self.assertContains(response, "3")

    def test_teen_3(self):
        response = self.client.get("/logic-2/no-teen-sum/?csrfmiddlewaretoken=2bnb5NfQ3Y4ynH4vgoGgcXOpOuthnWOKkAK5gk6QQJSbW408ysfVyDM7c8ChKfKv&a=2&b=1&c=14")
        self.assertContains(response, "3")


# # Warmpu 3
class TestCatDog(SimpleTestCase):
    def test_abcxyz(self):
        response = self.client.get("/string-2/xyz-there/?csrfmiddlewaretoken=8DTSHtgSzEkI4yW53c7ZIsXSBvW1oOWJq2gMS07Smp8lDVSIlgGE48VAZ951L7Su&s=abcxyz")
        self.assertContains(response, True)

    def test_abc_xyz(self):
        response = self.client.get("/string-2/xyz-there/?csrfmiddlewaretoken=5Dt4hMUQrLtIL0CKoED1Hh1lp0rONFXyn2QYsjLQewhlknynGIcG3XZ3NEAOaYTj&s=abc.xyz")
        self.assertContains(response, False)

    def test_xyz_abc(self):
        response = self.client.get("/string-2/xyz-there/?csrfmiddlewaretoken=CFlM5Pbh7RxW49um8kvfoIYCvFPNjjFAU4IGgm2hUClzDwqZqo4UKoWkTjYNGCBl&s=xyz.abc")
        self.assertContains(response, True)


# Warmup 4
class TestLoneSum(SimpleTestCase):
    def test_centered_7(self):
        response = self.client.get("/list-2/centered-average/?csrfmiddlewaretoken=jVWPbsGlcH5zeRdlwzi0Iz8r17y1XY7YBkjJmZxlZsTcNe9YODRF4f69pLH1kh3J&a=-10&b=-4&c=-2&d=-4&e=-2&f=0&g=")
        self.assertContains(response, "-4")

    def test_centered_8(self):
        response = self.client.get("/list-2/centered-average/?csrfmiddlewaretoken=TYc1C9o60Rg1zpazR7hRyBKCmik00cBBbnzVNGf6NC4E8M6c9bQwUhIkKWt0nvxm&a=1&b=2&c=3&d=4&e=100&f=&g=")
        self.assertContains(response, "22")

    def test_centered_9(self):
        response = self.client.get("/list-2/centered-average/?csrfmiddlewaretoken=Cork8bx4WVndfocXysd5che7wmNCdH63UNOejIo4JGbQOL8AQwMKyXcPU0WCA02O&a=4&b=4&c=4&d=4&e=5&f=&g=")
        self.assertContains(response, "4")