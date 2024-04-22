from database import db  
class User(db.Model):
    __tablename__ ='users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    
    # agregamos email, contrasena, fecha de nacimiento
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.String(50), nullable=False)
    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, email, password, fecha_nacimiento):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.fecha_nacimiento = fecha_nacimiento

    # Guarda un usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos
    @staticmethod
    def get_all():
        return User.query.all()