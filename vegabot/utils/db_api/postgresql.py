from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result
    
    async def create_scheme(self):
        sql = """CREATE SCHEMA vegabot;"""
        await self.execute(sql, execute=True)
            

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS vegabot.Resume (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL UNIQUE,
        language varchar(255) NULL ,
        fullname VARCHAR(255) NULL,
        date VARCHAR(25) NULL,
        phone VARCHAR(255) NULL,
        addphone VARCHAR(255) NULL,
        malumot VARCHAR(255) NULL,
        manzil VARCHAR(255) NULL,
        oilaviy_holat VARCHAR(100) NULL,
        sud_holat VARCHAR(100) NULL,
        day timestamp default NULL,
        company VARCHAR(255) NULL,
        new_company VARCHAR(255) NULL,
        last_summa VARCHAR(250) NULL,
        new_summa VARCHAR(250) NULL,
        time_job VARCHAR (135) NULL,
        know_lang VARCHAR (135) NULL,
        know_lang_degree VARCHAR (135) NULL,
        abaut_as VARCHAR (255) NULL
        );
        """
        await self.execute(sql, execute=True)


    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())


    async def add_user(self, telegram_id, language, fullname, date, phone, addphone, malumot, manzil, oilaviy_holat, sud_holat,
                       day, company, new_company, last_summa,new_summa, time_job, know_lang,know_lang_degree,abaut_as):
        sql = "INSERT INTO vegabot.Resume (telegram_id, language, fullname, date, phone, addphone, malumot, manzil, oilaviy_holat, sud_holat," \
              "day, company, new_company, last_summa,new_summa, time_job, know_lang,know_lang_degree,abaut_as) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19) "\
                "ON CONFLICT (telegram_id) DO NOTHING RETURNING *"
        return await self.execute(sql, telegram_id, language, fullname, date, phone, addphone, malumot, manzil, oilaviy_holat, sud_holat,
                       day, company, new_company, last_summa,new_summa, time_job, know_lang,know_lang_degree,abaut_as, fetchrow=True)




    async def select_all_users(self):
        sql = "SELECT * FROM vegabot.Resume"
        return await self.execute(sql, fetch=True)

    async def select_all_users2(self,provency):
        sql = "SELECT * FROM vegabot.Resume WHERE provency=$1"
        return await self.execute(sql,provency, fetch=True)

    async def select_all_day(self):
        sql = "SELECT * FROM Admin WHERE holat=True"
        return await self.execute(sql, fetch=True)

    async def select_7den(self,dayy,now):
        sql = "SELECT * FROM vegabot.Resume WHERE day>=$1 AND day<=$2"
        return await self.execute(sql, dayy,now,fetch=True)


    async def select_user(self, **kwargs):
        sql = "SELECT * FROM vegabot.Resume WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)


    async def count_users(self):
        sql = "SELECT COUNT(*) FROM vegabot.Resume"
        return await self.execute(sql, fetchval=True)


    async def update_user_full(self, fullname, date, phone, addphone, malumot, manzil, oilaviy_holat, sud_holat,day, company, new_company, last_summa,new_summa, time_job, know_lang,know_lang_degree,abaut_as,telegram_id):
        sql = "UPDATE vegabot.Resume SET fullname=$1, date=$2, phone=$3, addphone=$4, malumot=$5, manzil=$6, oilaviy_holat=$7, sud_holat=$8, day=$9, company=$10, new_company=$11, last_summa=$12,new_summa=$13, time_job=$14, know_lang=$15,know_lang_degree=$16,abaut_as=$17 WHERE telegram_id=$18"
        return await self.execute(sql, fullname, date, phone, addphone, malumot, manzil, oilaviy_holat, sud_holat,day, company, new_company, last_summa,new_summa, time_job, know_lang,know_lang_degree,abaut_as,telegram_id, execute=True)


    async def update_user_name(self, name, telegram_id):
        sql = "UPDATE vegabot.Resume SET name=$1 WHERE telegram_id=$2"
        return await self.execute(sql, name, telegram_id, execute=True)


    async def update_user_phone(self, phone, telegram_id):
        sql = "UPDATE vegabot.Resume SET phone=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone, telegram_id, execute=True)

    async def update_user_provency(self, provency, telegram_id):
        sql = "UPDATE vegabot.Resume SET provency=$1 WHERE telegram_id=$2"
        return await self.execute(sql, provency, telegram_id, execute=True)

    async def update_user_language(self, language, telegram_id):
        sql = "UPDATE vegabot.Resume SET language=$1 WHERE telegram_id=$2"
        return await self.execute(sql, language, telegram_id, execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM vegabot.Resume WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE vegabot.Resume", execute=True)