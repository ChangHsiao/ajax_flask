from flask_restful import Resource

class Users(Resource):
    def get(self):
        # 讀取所有資料
        return {"users": "所有使用者"}, 200

    def post(self):
        return {"users": "新增使用者"}, 200

# GET http://127.0.0.1/api.users/8
class User(Resource):
    def get(self, user_id):
        # 根據 user id 讀取資料
        return {"user": user_id}, 200

    def post(self, user_id):
        return {"修改 user": user_id}, 200

    def delete(self, user_id):
        return {"刪除 user": user_id}, 200
