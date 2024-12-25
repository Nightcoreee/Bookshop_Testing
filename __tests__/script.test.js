const mysql = require('mysql');

// Tạo kết nối đến cơ sở dữ liệu
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Ngocha7890',
    database: 'bookshop_test'
});

// Kết nối đến cơ sở dữ liệu trước khi chạy các bài kiểm tra
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

// Đóng kết nối sau khi chạy xong các bài kiểm tra
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

// Bài kiểm tra kiểm tra xem email "alexson6060@gmail.com" có tồn tại hay không
test('Kiểm tra xem email "alexson6060@gmail.com" có tồn tại hay không', (done) => {
    // Truy vấn kiểm tra email
    connection.query('SELECT * FROM `user` WHERE email = "alexson6060@gmail.com"', (err, results) => {
        if (err) {
            console.error('Lỗi thực thi truy vấn:', err);
            done(err);
        } else {
            expect(results.length).toBeGreaterThan(0);
            done();
        }
    });
});