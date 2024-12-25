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

// Bài kiểm tra kiểm tra xem kết nối có thành công hay không
test('Kiểm tra kết nối đến cơ sở dữ liệu', (done) => {
    connection.ping((err) => {
        if (err) {
            console.error('Lỗi kết nối đến cơ sở dữ liệu:', err);
            done(err);
        } else {
            console.log('Kết nối đến cơ sở dữ liệu thành công');
            done();
        }
    });
});