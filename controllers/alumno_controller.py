from models.alumno_model import AlumnoModel


class AlumnoController():

    def get(self):
        alumnos = AlumnoModel.query.all()
        resultado = []

        try:
            for alumnos in alumnos:
                resultado.append(alumnos.json())
            if resultado:
                return self.__json__response(True, "Lista de alumnos", resultado, 200)
            return self.__json__response(True, "Lista de alumnos vacio", resultado, 404)
        except Exception as e:
            return self.__json_response(False, "Hubo un error el servidor", 500)

    def post(self, data):
        try:
            resultado = AlumnoModel(
                data['alumnoNombre'], data['alumnoDni'], data['alumnoEdad']).guardar_db()
            return self.__json__response(True, "Alumno creado", resultado, 201)
        except Exception as e:
            return self.__json_response(False, e, None, 500)

    def update(self, alumno_id, data):
        try:
            alumno = AlumnoModel.query.filter_by(alumnoId=alumno_id).first()
            resultado = alumno.actualizar_db(
                data['alumnoNombre'], data['alumnoDni'], data['alumnoEdad'])
            return self.__json__response(True, "Alumno actualizado", resultado, 201)
        except Exception as e:
            return self.__json__response(False, e, None, 500)

    def delete(self, alumno_id):
        try:
            alumno = AlumnoModel.query.filter_by(alumnoId=alumno_id).first()
            resultado = alumno.eliminar_db()
            return self.__json__response(True, "Alumno eliminado", resultado, 201)
        except Exception as e:
            return self.__json__response(False, e, None, 500)

    def __json__response(self, estatus, message, content, status_code):
        return {
            "success": estatus,
            "message": message,
            "content": content
        }, status_code
