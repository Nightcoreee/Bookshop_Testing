const fs = require('fs');
const path = require('path');
const mysql = require('mysql');
const register = require('../bookshop/app');


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

test('Kiểm tra người dùng vừa đăng ký có tồn tại trong database không', (done) => {
    const user = {
        fname: 'John',
        lname: 'Doe',
        email: 'johndoe@gmail.com',
        password: 'password123',
        mobile: '0741164258',
        joined_date: new Date(),
        verification_code: '123456',
        gender_gender_id: 1,
        status_status_id: 1
    };

    register(user, (err, results) => {
        if (err) {
            console.error('Lỗi thực thi truy vấn:', err);
            done(err);
        } else {
            // Kiểm tra dữ liệu trong cơ sở dữ liệu
            connection.query('SELECT * FROM `user` WHERE email = ?', [user.email], (err, results) => {
                if (err) {
                    console.error('Lỗi thực thi truy vấn:', err);
                    done(err);
                } else {
                    expect(results.length).toBe(1);
                    expect(results[0].fname).toBe('John');
                    expect(results[0].lname).toBe('Doe');
                    done();
                }
            });
        }
    });
});