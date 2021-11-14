from class_funct import *
from flask import request, jsonify, json


@app.route('/users/', methods=['GET', 'POST'])
def all_users():
    """GET-запросы получения всех пользователей.
    Создание пользователя посредством метода POST"""

    if request.method == 'GET':
        all_user = db.session.query(Users).all()
        result = []
        for u in all_user:
            result.append(u.user_dict())
        return jsonify(result)

    elif request.method == 'POST':
        data_user = request.get_json()
        new_user = Users(
            first_name=data_user['first_name'],
            last_name=data_user['last_name'],
            age=data_user['age'],
            email=data_user['email'],
            role=data_user['role'],
            phone=data_user['phone']
        )
        db.session.add(new_user)
        db.session.commit()
        return "", 201


@app.route('/users/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def one_users(uid: int):
    """Обрабатывает GET-запросы получения пользователя по идентификатору
    Обновление пользователя посредством метода PUT.
    Удаление пользователя посредством метода DELETE"""

    if request.method == 'GET':
        all_user = db.session.query(Users).all()
        for u in all_user:
            if u.id == uid:
                return jsonify(u.user_dict())

    elif request.method == 'DELETE':
        delete_user = Users.query.get(uid)
        db.session.delete(delete_user)
        db.session.commit()
        return jsonify(""), 204

    elif request.method == 'PUT':
        data_user = request.get_json()
        change_user = Users.query.get(uid)
        change_user.first_name = data_user['first_name']
        change_user.last_name = data_user['last_name']
        change_user.age = data_user['age']
        change_user.email = data_user['email']
        change_user.role = data_user['role']
        change_user.phone = data_user['phone']
        db.session.add(change_user)
        db.session.commit()
        return jsonify(""), 204


@app.route('/orders/', methods=['GET', 'POST'])
def all_orders():
    """GET-запросы получения всех заказов.
    Создание заказа order посредством метода POST на URL /orders"""

    if request.method == 'GET':
        all_orders = db.session.query(Order).all()
        result = []
        for order in all_orders:
            result.append(order.order_dict())
        return jsonify(result)

    elif request.method == 'POST':
        data_order = request.get_json()
        new_order = Order(
            name=data_order['name'],
            description=data_order['description'],
            start_date=data_order['start_date'],
            end_date=data_order['end_date'],
            address=data_order['address'],
            price=data_order['price'],
            customer_id=data_order['customer_id'],
            executor_id=data_order['executor_id']
        )
        db.session.add(new_order)
        db.session.commit()
        return "", 201


@app.route('/orders/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def one_order(uid: int):
    """Обрабатывает GET-запросы получения заказа по идентификатору.
    Обновление заказа посредством метода PUT на URL /orders/<id>.
    Удаление заказа order посредством метода DELETE на URL /orders/<id>"""

    if request.method == 'GET':
        all_orders = db.session.query(Order).all()
        for order in all_orders:
            if order.id == uid:
                return jsonify(order.order_dict())

    elif request.method == 'DELETE':
        delete_order = Users.query.get(uid)
        db.session.delete(delete_order)
        db.session.commit()
        return jsonify(""), 204

    elif request.method == 'PUT':
        data_order = request.get_json()
        change_order = Order.query.get(uid)
        change_order.name = data_order['name']
        change_order.description = data_order['description']
        change_order.end_date = data_order['end_date']
        change_order.address = data_order['address']
        change_order.price = data_order['price']
        change_order.customer_id = data_order['customer_id']
        change_order.executor_id = data_order['executor_id']
        db.session.add(change_order)
        db.session.commit()
        return jsonify(""), 204


@app.route('/offers/', methods=['GET', 'POST'])
def all_offers():
    """GET-запросы получения всех предложений.
     Создание предложения посредством метода POST"""

    if request.method == 'GET':
        all_offers = db.session.query(Offers).all()
        result = []
        for offer in all_offers:
            result.append(offer.offer_dict())
        return jsonify(result)

    elif request.method == 'POST':
        data_offer = request.get_json()
        new_offer = Offers(
            order_id=data_offer['order_id'],
            executor_id=data_offer['executor_id']
        )
        db.session.add(new_offer)
        db.session.commit()
        return "", 201


@app.route('/offers/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def one_offer(uid: int):
    """Обрабатывает GET-запросы получения заказа по идентификатору.
    Обновление предложения посредством метода PUT.
    Удаление предложения посредством метода DELETE"""

    if request.method == 'GET':
        all_offers = db.session.query(Offers).all()
        for offer in all_offers:
            if offer.id == uid:
                return jsonify(offer.offer_dict())

    elif request.method == 'DELETE':
        delete_offer = Users.query.get(uid)
        db.session.delete(delete_offer)
        db.session.commit()
        return jsonify(""), 204

    elif request.method == 'PUT':
        data_offer = request.get_json()
        change_offer = Offers.query.get(uid)
        change_offer.order_id = data_offer['order_id']
        change_offer.executor_id = data_offer['executor_id']
        db.session.add(change_offer)
        db.session.commit()
        return jsonify(""), 204


if __name__ == '__main__':
    app.run(debug=True)