import pyodbc

# server = input('server: ')
server = ''
if not server:
    server = 'DESKTOP-OVI4VGA'
conn = pyodbc.connect('driver={SQL Server}; server='+server+';' + """
                       database=railway_new_db;
                       trusted_connection=yes;""".format(server), 
                       autocommit=True)
