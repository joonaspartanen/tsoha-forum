from application import app, db

from flask_login import current_user
from application.auth.models import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


class UserService:
    @staticmethod
    def user_not_admin_nor_editing_own_content(author_id):
        return not (current_user.is_admin or current_user.id == author_id)

    @staticmethod
    def create_testadmin_if_absent(password):
        testadmin = User.query.filter_by(username="tsohaadmin").first()
        if testadmin:
            return

        pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        testadmin = User("tsohaadmin", pw_hash, True)

        db.session().add(testadmin)
        db.session().commit()
