from db.run_sql import run_sql
from models.manager import Manager

def save(manager):
    sql = "INSERT INTO managers (name, picture, start_date, end_date, active) VALUES (%s, %s, %s, NULL, 't') RETURNING id"
    values = [manager.name, manager.picture, manager.start_date]
    results = run_sql(sql, values)
    id = results[0]['id']
    manager.id = id

def select_all():
    managers = []
    sql = "SELECT * FROM managers"
    results = run_sql(sql)
    for row in results:
        manager = Manager(row['name'], row['picture'], row['start_date'], row['id'])
        managers.append(manager)
    return managers

def select(id):
    manager = None
    sql = "	SELECT * FROM managers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        manager = Manager(result['name'], result['picture'], result['start_date'], result['id'])
    return manager

def update(manager):
    sql = "UPDATE managers SET (name, picture, start_date, end_date) = (%s, %s, %s, %s) where id = %s" 
    values = [manager.name, manager.picture, manager.start_date, manager.end_date, manager.id]
    run_sql(sql, values)