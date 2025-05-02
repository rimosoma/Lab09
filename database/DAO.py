from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_airports():
        from model.aereoporto import Aereoporto
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM airports"
        cursor.execute(query)
        for row in cursor:
            result[row['ID']] = Aereoporto(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesPesati():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT LEAST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS airport_1,"
                 " GREATEST(ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID) AS airport_2,"
                 " AVG(DISTANCE) AS avg_distance"
                 " FROM flights"
                 " GROUP BY airport_1, airport_2"
                 " ORDER BY avg_distance DESC;")
        cursor.execute(query)
        for row in cursor:
            tripla = (
                row["airport_1"],
                row["airport_2"],
                row["avg_distance"])
            result.append(tripla)
        cursor.close()
        conn.close()
        return result