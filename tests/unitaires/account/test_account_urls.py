from django.urls import reverse, resolve


def test_register():
    path = reverse("add_user")
    assert path == "/register/"
    assert resolve(path).view_name == "add_user"


def test_login():
    path = reverse("login")
    assert path == "/login/"
    assert resolve(path).view_name == "login"


def test_logout():
    path = reverse("logout")
    assert path == "/logout/"
    assert resolve(path).view_name == "logout"


def test_account():
    path = reverse("account_page")
    assert path == "/account/"
    assert resolve(path).view_name == "account_page"


def test_activate_mail():
    path = reverse("activate", kwargs={"token": 1})
    assert path == "/activate-email/1"
    assert resolve(path).view_name == "activate"


def test_success_page():
    path = reverse("success")
    assert path == "/success"
    assert resolve(path).view_name == "success"


def test_activate_message_page():
    path = reverse("activate_your_mail")
    assert path == "/activate-message"
    assert resolve(path).view_name == "activate_your_mail"


def test_reset_password():
    path = reverse("reset_password")
    assert path == "/reset_password/"
    assert resolve(path).view_name == "reset_password"


def test_reset_password_sent():
    path = reverse("password_reset_done")
    assert path == "/reset_password_sent/"
    assert resolve(path).view_name == "password_reset_done"


def test_reset_password_confirm():
    path = reverse("password_reset_confirm", kwargs={"uidb64": "toto", "token": 1})
    assert path == "/reset/toto/1"
    assert resolve(path).view_name == "password_reset_confirm"


def test_reset_password_complete():
    path = reverse("password_reset_complete")
    assert path == "/reset_password_complete/"
    assert resolve(path).view_name == "password_reset_complete"


def test_password_change():
    path = reverse("password_change")
    assert path == "/password_change/"
    assert resolve(path).view_name == "password_change"


def test_password_change_done():
    path = reverse("password_change_done")
    assert path == "/password_change/done/"
    assert resolve(path).view_name == "password_change_done"
