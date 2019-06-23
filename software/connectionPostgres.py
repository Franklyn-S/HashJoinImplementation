import psycopg2

def create_txt_from_table(table_name):
  try:
      connection = psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "iswc")
      cursor = connection.cursor()
      query = "SELECT * FROM tpch1g." + table_name
      cursor.execute(query)
      file = open(table_name + ".txt", "w")
      columns_names = ""

      #getting columns names
      columns = [col[0] for col in cursor.description]
      qtd_columns = 0
      for c in columns:
        if qtd_columns == len(columns)-1:
          columns_names += c + "\n"
        else:
          columns_names += c + ";"
        qtd_columns += 1
      file.write(columns_names)

      #getting data
      data = ""
      tupleCounter = 0
      row = cursor.fetchone()
      while row != None:
        #print(row)
        for col_index in range(qtd_columns):
          if col_index == qtd_columns-1:
            data += str(row[col_index]) + "\n"
          else:
            data += str(row[col_index]) + ";"
        if tupleCounter > 100000:
          file.write(data)
          data = ''
        row = cursor.fetchone()
        tupleCounter += 1
      file.write(data)
      file.close()



  except (Exception, psycopg2.Error) as error :
      print ("Error while connecting to PostgreSQL", error)
  finally:
      
      #closing database connection.
      if(connection):
          cursor.close()
          connection.close()
          #print("PostgreSQL connection is closed")


if __name__ == "__main__":
  try:
    connection = psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "127.0.0.1",
                                    port = "5432",
                                    database = "iswc")
    cursor = connection.cursor()
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema='tpch1g'AND table_type= 'BASE TABLE'"
    cursor.execute(query)
    table_names = cursor.fetchall()
    for table_name in table_names:
      create_txt_from_table(table_name[0])
    
  except (Exception, psycopg2.Error) as error :
      print ("Error while connecting to PostgreSQL", error)
  finally:
      #closing database connection.
      if(connection):
          cursor.close()
          connection.close()
          print("PostgreSQL connection is closed")         