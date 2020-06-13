from flask_login import current_user


class UserService:
    @staticmethod
    def user_not_admin_nor_editing_own_content(author_id):
        return not (current_user.is_admin or current_user.id == author_id)
