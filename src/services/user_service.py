from src.database.models import User


class UserService:
    @staticmethod
    def get_all_users(ses):
        return ses.query(User)

    @classmethod
    def get_user_by_name(cls, ses, username):
        return cls.get_all_users(ses).filter(User.user_name == username).first()

    @classmethod
    def get_user_by_uuid(cls, ses, uuid):
        return cls.get_all_users(ses).filter(uuid == uuid).first()
