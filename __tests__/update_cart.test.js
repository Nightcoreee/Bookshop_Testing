const mysql = require('mysql');
const { updateCart} = require('../bookshop/app');

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

test('Kiểm tra cập nhật mục trong giỏ hàng', (done) => {
    const user = {
        email: 'johndoe_updated@gmail.com',
        fname: 'John',
        lname: 'Doe',
        password: 'password123',
        mobile: '0741164259',
        joined_date: new Date(),
        verification_code: '123456',
        gender_gender_id: 1,
        status_status_id: 1
    };

    const updatedCart = {
        cart_id: 1,
        qty: 3,
        user_email: 'johndoe_updated@gmail.com',
        product_id: 15
    };

    // Thêm người dùng vào bảng user
    connection.query('INSERT INTO `user` SET ?', user, (err, results) => {
        if (err) {
            console.error('Lỗi thêm người dùng:', err);
            done(err);
        } else {
            // Cập nhật giỏ hàng
            updateCart(updatedCart, (err, results) => {
                if (err) {
                    console.error('Lỗi thực thi truy vấn:', err);
                    done(err);
                } else {
                    // Kiểm tra dữ liệu trong cơ sở dữ liệu
                    connection.query('SELECT * FROM `cart` WHERE cart_id = ?', [updatedCart.cart_id], (err, results) => {
                        if (err) {
                            console.error('Lỗi thực thi truy vấn:', err);
                            done(err);
                        } else {
                            expect(results.length).toBe(1);
                            expect(results[0].qty).toBe(updatedCart.qty);
                            expect(results[0].user_email).toBe(updatedCart.user_email);
                            expect(results[0].product_id).toBe(updatedCart.product_id);
                            done();
                        }
                    });
                }
            });
        }
    });
});