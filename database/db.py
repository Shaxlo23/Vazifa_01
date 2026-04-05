import asyncpg
from config import config

class Database:
    def __init__(self):
        self.pool=None

    
    async def connection(self):
        self.pool=await asyncpg.create_pool(
            host=config.DB_HOST,
            port=config.DB_PORT,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )

    async def add_user(self,telegram_id,name,surename,age,phone_number):
        query="""
        insert into users(telegram_id,name,surename,age,phone_number) values($1,$2,$3,$4,$5);
        """
        await self.pool.execute(query,telegram_id,name,surename,age,phone_number)
    


    async def is_user_exists(self,telegram_id: int)-> bool:
        query="""
        SELECT EXISTS (
        SELECT 1 FROM users WHERE telegram_id=$1
        );
        """
        return await self.pool.fetchval(query,telegram_id)
    


    async def profile(self,tg_id):
        query="""
        select name,surename,age,phone_number,role from users where telegram_id=$1;
        """
        return await self.pool.fetchrow(query,tg_id)
    


    async def get_user_role(self,telegram_id):
        query="""
        SELECT role FROM users WHERE telegram_id=$1
        """
        return await self.pool.fetchval(query,telegram_id)
    
    async def get_users(self):
        query="""
        select name,surename,role,id from users order by id;
        """
        return await self.pool.fetch(query)
    

    async def update_role(self,user_id,role):
        query="""
        update users set role=$1 where id=$2;
        """

        await self.pool.execute(query,role,user_id)