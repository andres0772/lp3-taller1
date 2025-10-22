"""
Recursos y rutas para la API de videos
"""
from ast import Param
from typing_extensions import ReadOnly
from flask_restx import Namespace, Resource, reqparse, abort, fields, marshal_with #se cambia a restx y se agrega Namespace
from models.video import VideoModel
from models import db

#se crea un Namespace para que se documente el swagger
api = Namespace ('videos', description='Operaciones para los videos')

#definir el modelo de los videos
video_model = api.model('Video', {
    'id': fields.Integer(readonly=True, description='ID del video'),
    'name': fields.String(required=True, description='Nombre del video'),
    'views': fields.Integer(required=True, description='Número de vistas'),
    'likes': fields.Integer(required=True, description='Número de likes')
})

# Campos para serializar respuestas
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# Parser para los argumentos en solicitudes PUT (crear video)
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Nombre del video es requerido", required=True)
video_put_args.add_argument("views", type=int, help="Número de vistas del video", required=True)
video_put_args.add_argument("likes", type=int, help="Número de likes del video", required=True)

# Parser para los argumentos en solicitudes PATCH (actualizar video)
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Nombre del video")
video_update_args.add_argument("views", type=int, help="Número de vistas del video")
video_update_args.add_argument("likes", type=int, help="Número de likes del video")

def abort_if_video_doesnt_exist(video_id):
    """
    Verifica si un video existe, y si no, aborta la solicitud
    
    Args:
        video_id (int): ID del video a verificar
    """
    video = VideoModel.query.filter_by(id=video_id).first()
    if not video:
        abort(404, message=f"No se encontró un video con este ID: {video_id}")
    return video

class Video(Resource):
    """
    Recurso para gestionar videos individuales
    
    Métodos:
        get: Obtener un video por ID
        put: Crear un nuevo video
        patch: Actualizar un video existente
        delete: Eliminar un video
    """
    @api.doc(params={'video_id': 'ID del video'}, responses={200: 'video encontrado', 404: 'video no encontrado'}) #se crea una api de documento que tendra el siguiente parametro, tendria el id del video y la respuesta es si esta dara un 200 si no dara un 404.
    @marshal_with(resource_fields)
    def get(self, video_id):
        """
        Obtiene un video por su ID
        
        Args:
            video_id (int): ID del video a obtener
            
        Returns:
            VideoModel: El video solicitado
        """
        video = abort_if_video_doesnt_exist(video_id)
        return video

    @api.doc(responses={200: 'Video creado', 400: 'Datos inválidos'}, body=video_model) #se crea otra api doc donde va a responder lo siguiente, si el video se creo dara una respuesta 200, si en caso no dara una respuesta 400.
    @marshal_with(resource_fields)
    def put(self, video_id):
        """
        Crea un nuevo video con un ID específico
        
        Args:
            video_id (int): ID para el nuevo video
            
        Returns:
            VideoModel: El video creado
        """
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video
    
    @api.doc(responses={200: 'Video actualizado', 404: 'Video no encontrado'}, body=video_model)#se crea otro decorador que respondera lo siguiente, si el video se creo dara una respuesta 200 si no dara 404.
    @marshal_with(resource_fields)
    def patch(self, video_id):
        """
        Actualiza un video existente
        
        Args:
            video_id (int): ID del video a actualizar
            
        Returns:
            VideoModel: El video actualizado
        """
        args = video_update_args.parse_args()
        video = abort_if_video_doesnt_exist(video_id)
        if args['name'] is not None:
            video.name = args['name']
        if args['views'] is not None:
            video.views = args['views']
        if args['likes'] is not None:
            video.likes = args['likes']
        db.session.commit()
        return video
        

    @api.doc(responses={204: 'Video eliminado', 404: 'Video no encontrado'})#se crea otro decorador que respondera lo siguiente, si el video se creo dara una respuesta 204 si no dara 404.
    def delete(self, video_id):
        """
        Elimina un video existente
        
        Args:
            video_id (int): ID del video a eliminar
            
        Returns:
            str: Mensaje vacío con código 204
        """
        video = abort_if_video_doesnt_exist(video_id)
        db.session.delete(video)
        db.session.commit()
        return '', 204

api.add_resource(Video, '/<int:video_id>')