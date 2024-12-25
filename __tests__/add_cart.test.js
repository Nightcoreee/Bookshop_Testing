const mysql = require('mysql');
const { addToCart} = require('../bookshop/app');

// Thiết lập kết nối đến cơ sở dữ liệu thử nghiệm
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Ngocha7890',
    database: 'bookshop_test'
});

beforeAll((done) => {
    connection.connect((err) => {
        if (err) {
            console.error('Lỗi kết nối đến cơ sở dữ liệu:', err);
            done(err);
        } else {
            console.log('Đã kết nối đến cơ sở dữ liệu');
            done();
        }
    });
});

afterAll((done) => {
    connection.end((err) => {
        if (err) {
            console.error('Lỗi ngắt kết nối từ cơ sở dữ liệu:', err);
            done(err);
        } else {
            console.log('Đã ngắt kết nối từ cơ sở dữ liệu');
            done();
        }
    });
});

test('Kiểm tra sản phẩm vừa thêm vào giỏ hàng có tồn tại không', (done) => {
    const cart = {
        cart_id: 1,
        qty: 2,
        user_email: 'johndoe@gmail.com',
        product_id: 15
    };

    addToCart(cart, (err, results) => {
        if (err) {
            console.error('Lỗi thực thi truy vấn:', err);
            done(err);
        } else {
            // Kiểm tra dữ liệu trong cơ sở dữ liệu
            connection.query('SELECT * FROM `cart` WHERE cart_id = ?', [cart.cart_id], (err, results) => {
                if (err) {
                    console.error('Lỗi thực thi truy vấn:', err);
                    done(err);
                } else {
                    expect(results.length).toBe(1);
                    expect(results[0].cart_id).toBe(cart.cart_id);
                    expect(results[0].qty).toBe(cart.qty);
                    expect(results[0].user_email).toBe(cart.user_email);
                    expect(results[0].product_id).toBe(cart.product_id);
                    done();
                }
            });
        }
    });
});
