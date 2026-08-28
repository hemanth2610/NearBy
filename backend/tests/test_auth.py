import pytest
from app.core.security import create_access_token, decode_jwt_token, get_password_hash, verify_password


def test_password_hashing():
    """Test bcrypt password hashing and verification."""
    password = "SuperSecretPassword123!"
    hashed = get_password_hash(password)
    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password("WrongPassword", hashed) is False


def test_jwt_token_encoding():
    """Test JWT token encoding and decoding."""
    user_uuid = "550e8400-e29b-41d4-a716-446655440000"
    token = create_access_token(user_uuid=user_uuid)
    assert isinstance(token, str)

    payload = decode_jwt_token(token)
    assert payload is not None
    assert payload["sub"] == user_uuid
    assert payload["type"] == "access"


@pytest.mark.asyncio
async def test_register_endpoint(client, monkeypatch):
    """Test user registration endpoint."""
    from app.crud.crud_user import crud_user
    from app.models.user import User

    fake_user = User(
        id=1,
        uuid="550e8400-e29b-41d4-a716-446655440000",
        full_name="Jane Doe",
        email="janedoe@example.com",
        password_hash="hashed_pw",
        role="user",
        is_active=True,
        is_verified=False
    )

    async def mock_get_by_email(db, email):
        return None

    async def mock_create_user(db, obj_in):
        return fake_user

    monkeypatch.setattr(crud_user, "get_by_email", mock_get_by_email)
    monkeypatch.setattr(crud_user, "create_user", mock_create_user)

    payload = {
        "full_name": "Jane Doe",
        "email": "janedoe@example.com",
        "password": "Password123!"
    }
    response = await client.post("/api/v1/auth/register", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["success"] is True
    assert data["data"]["email"] == "janedoe@example.com"
    assert data["data"]["full_name"] == "Jane Doe"

