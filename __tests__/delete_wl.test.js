const mysql = require('mysql');
const { addWishlist, deleteWishlist } = require('../bookshop/app');

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

test('Kiểm tra xóa sản phẩm khỏi watchlist', (done) => {
    const user_email = 'johndoe@gmail.com';

    deleteWishlist(user_email, (err, results) => {
        if (err) {
            console.error('Lỗi thực thi truy vấn:', err);
            done(err);
        } else {
            // Kiểm tra dữ liệu trong cơ sở dữ liệu
            connection.query('SELECT * FROM `watchlist` WHERE user_email = ?', [user_email], (err, results) => {
                if (err) {
                    console.error('Lỗi thực thi truy vấn:', err);
                    done(err);
                } else {
                    expect(results.length).toBe(0);
                    done();
                }
            });
        }
    });
});