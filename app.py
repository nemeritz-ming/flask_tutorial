from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = "secret key"
# 定义路由器通过装饰器实现
# 路由默认只支持get，如果需要更多，以list形式增加
@app.route('/', methods=['GET', 'POST'])
# def index():
    # 动态传入网址 html双括号{{}}来传入
    # url_str = 'www.baidu.com'
    # my_list = [1, 2, 3, 4, 5]
    # my_dictionary = {'A': 888, 'B': 'CHINA', 'C': 345}
    # return render_template('index.html', url_str=url_str, my_list=my_list, my_dictionary=my_dictionary)


def index():
    """
    1.判断请求方式
    2.获取账号密码参数
    flash 需要对消息加密
    """
    # 判断请求方式
    if request.method == 'POST':
        # 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(username, password, password2)
        if not all([username, password, password2]):
            flash(u'参数不完整')
        elif password != password2:
            flash(u'密码不一致')
        return 'success'
    return render_template('table.html')


# 使用同一个试图函数来显示不同订单信息
# 在<>内定义路由的参数
# 定义order_id为int类型
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):
    # 参数类型 默认为unicode编码的字符串
    print(type(order_id))
    # 需要在试图函数内()添加参数名，才可以使用
    return 'order_id%s' % order_id


if __name__ == '__main__':
    app.run()
