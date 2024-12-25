const mysql = require('mysql');
const updateUser = require('../bookshop/app');

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

test('Kiểm tra cập nhật thông tin người dùng', (done) => {
    const updatedUser = {
        fname: 'John',
        lname: 'Doe',
        email: 'johndoe@gmail.com',
        password: 'newpassword123',
        mobile: '0741164259',
        joined_date: new Date(),
        verification_code: '654321',
        gender_gender_id: 1,
        status_status_id: 1
    };

    updateUser(updatedUser, (err, results) => {
        if (err) {
            console.error('Lỗi thực thi truy vấn:', err);
            done(err);
        } else {
            // Kiểm tra dữ liệu trong cơ sở dữ liệu
            connection.query('SELECT * FROM `user` WHERE email = ?', [updatedUser.email], (err, results) => {
                if (err) {
                    console.error('Lỗi thực thi truy vấn:', err);
                    done(err);
                } else {
                    expect(results.length).toBe(1);
                    expect(results[0].fname).toBe(updatedUser.fname);
                    expect(results[0].lname).toBe(updatedUser.lname);
                    expect(results[0].password).toBe(updatedUser.password);
                    expect(results[0].mobile).toBe(updatedUser.mobile);
                    expect(new Date(results[0].joined_date).toISOString().split('T')[0]).toBe(updatedUser.joined_date.toISOString().split('T')[0]);
                    expect(results[0].verification_code).toBe(updatedUser.verification_code);
                    expect(results[0].gender_gender_id).toBe(updatedUser.gender_gender_id);
                    expect(results[0].status_status_id).toBe(updatedUser.status_status_id);
                    done();
                }
            });
        }
    });
});