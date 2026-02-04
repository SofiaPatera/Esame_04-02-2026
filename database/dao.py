
from database.DB_connect import DBConnect
class DAO:
    @staticmethod
    def leggi_ruolo():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT DISTINCT role
                    FROM authorship au, 
                         artists ar
                    WHERE au.artist_id = ar.artist_id """
        cursor.execute(query)
        for row in cursor:
            result.append(row['role'])
        cursor.close()
        conn.close()
        return result




    @staticmethod
    def leggi_nodi(role):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT DISTINCT a.name 
                    FROM  artists a, authorship au
                    WHERE au.role = %s"""
        cursor.execute(query, (role,))
        for row in cursor:
            result.append(row['name'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def leggi_archi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT art1, art2, ABS(art1-art2) as peso 
                    FROM (SELECT distinct a.name, count(*) as indice
                            FROM artists a, authorship au, objects o
                            WHERE a.artist_id = au.artist_id and au.object_id = o.object_id 
                            and o.curator_approved = 1 
                            GROUP BY a.name) art1, 
                        (SELECT distinct a.name, count(*) as indice
                            FROM artists a, authorship au, objects o
                            WHERE a.artist_id = au.artist_id and au.object_id = o.object_id 
                            and o.curator_approved = 1 
                            GROUP BY a.name) art2 
                    WHERE art1.id != art2.id AND count(*) 
                    GROUP BY art1, art2
            
                                      """
        cursor.execute(query)
        for row in cursor:
            result.append((row['artist1'], row['artist2'], row['peso']))
        cursor.close()
        conn.close()
        return result