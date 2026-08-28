import argparse
import asyncio
import os
import sys

# Ensure backend root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import select
from app.core.config import settings
from app.core.security import get_password_hash
from app.db.session import AsyncSessionFactory
from app.models.user import User


async def list_users():
    """List all registered users and admins in the database."""
    async with AsyncSessionFactory() as db:
        stmt = select(User)
        result = await db.execute(stmt)
        users = result.scalars().all()

        print("\n================ Registered Accounts ================")
        if not users:
            print("No users found in database.")
        for u in users:
            print(f"ID: {u.id} | Email: {u.email} | Name: {u.full_name} | Role: {u.role} | Active: {u.is_active} | Verified: {u.is_verified}")
        print("====================================================\n")


async def reset_admin(email: str, password: str, name: str):
    """Reset or create admin user credentials."""
    email_clean = email.strip().lower()
    hashed_pwd = get_password_hash(password)

    async with AsyncSessionFactory() as db:
        stmt = select(User).where(User.email == email_clean)
        result = await db.execute(stmt)
        user = result.scalars().first()

        if user:
            user.password_hash = hashed_pwd
            user.role = "admin"
            user.is_active = True
            user.is_verified = True
            if name and name.strip():
                user.full_name = name.strip()
            db.add(user)
            await db.commit()
            await db.refresh(user)
            print("\n=======================================================")
            print("  SUCCESS: Admin Password Reset Successfully!")
            print("=======================================================")
            print(f"  User ID:       {user.id}")
            print(f"  Email:         {user.email}")
            print(f"  Role:          {user.role}")
            print(f"  Active:        {user.is_active}")
            print(f"  New Password:  {password}")
            print("=======================================================\n")
        else:
            new_admin = User(
                full_name=name.strip() if name else settings.FIRST_ADMIN_NAME,
                email=email_clean,
                password_hash=hashed_pwd,
                role="admin",
                is_active=True,
                is_verified=True
            )
            db.add(new_admin)
            await db.commit()
            await db.refresh(new_admin)
            print("\n=======================================================")
            print("  SUCCESS: New Admin Account Created Successfully!")
            print("=======================================================")
            print(f"  User ID:       {new_admin.id}")
            print(f"  Email:         {new_admin.email}")
            print(f"  Role:          {new_admin.role}")
            print(f"  Active:        {new_admin.is_active}")
            print(f"  Password:      {password}")
            print("=======================================================\n")


def main():
    parser = argparse.ArgumentParser(description="Reset or Create Admin User Password for Nearby Tourist Guide")
    parser.add_argument("--email", type=str, default=settings.FIRST_ADMIN_EMAIL, help=f"Admin email address (default: {settings.FIRST_ADMIN_EMAIL})")
    parser.add_argument("--password", type=str, default=settings.FIRST_ADMIN_PASSWORD, help=f"Admin password (default: {settings.FIRST_ADMIN_PASSWORD})")
    parser.add_argument("--name", type=str, default=settings.FIRST_ADMIN_NAME, help="Admin display name")
    parser.add_argument("--list", action="store_true", help="List all accounts in the database")

    args = parser.parse_args()

    if args.list:
        asyncio.run(list_users())
    else:
        asyncio.run(reset_admin(email=args.email, password=args.password, name=args.name))


if __name__ == "__main__":
    main()
