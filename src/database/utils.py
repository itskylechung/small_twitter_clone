from fastapi import Depends, HTTPException, Security, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.database.database import get_db_session
from src.models.users import User


async def get_user_by_api_key(
    api_key: str, session: AsyncSession = Depends(get_db_session)
):
    query = (
        select(User)
        .where(User.api_key == api_key)
        .options(
            selectinload(User.following),
        )
    )
    user = await session.execute(query)

    return user.scalar_one_or_none()
