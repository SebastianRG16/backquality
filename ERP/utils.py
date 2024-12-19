from django.db import connection

def get_accessible_data(user_id):
    """
    Llama al procedimiento almacenado para obtener datos accesibles al usuario.
    """
    with connection.cursor() as cursor:
        cursor.callproc('get_user_accessible_data', [user_id])
        results = cursor.fetchall()

    # Formatear los resultados como una lista de diccionarios
    data = [
        {
            'branch_office_id': row[0],
            'branch_office_name': row[1],
            'cost_center_id': row[2],
            'cost_center_name': row[3],
        }
        for row in results
    ]

    return data
