import psycopg2

#Database manager
conn = psycopg2.connect('dbname=peoplecounterdb')
cur = conn.cursor()

def add_field(date,hour,counter_in,counter_out):
    query = """
    INSERT INTO
      tablepi
    VALUES
      (%s, %s, %s, %s)
    """
    values = (date, hour, counter_in, counter_out)
    cur.execute(query, values)
    conn.commit()
