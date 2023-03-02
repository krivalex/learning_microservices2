from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://testing:testing123@test.dsacademy.kz:5432/fortesting")
conn = engine.connect()

print("now connected to the database")
