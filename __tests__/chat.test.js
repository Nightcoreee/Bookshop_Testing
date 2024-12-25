const mysql = require('mysql');
const addChat = require('../bookshop/app');

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

test('Kiểm tra chat có tồn tại trong database không', (done) => {
    const chat = {
        chat_id: 24,
        content: 'rất xin chào bạn 2',
        date_time: new Date(),
        status: 2,
        from: 'hai6060@gmail.com',
        to: 'sandeepaherath2001@gmail.com'
    };

    addChat(chat, (err, results) => {
        if (err) {
            console.error('Lỗi thực thi truy vấn:', err);
            done(err);
        } else {
            // Kiểm tra dữ liệu trong cơ sở dữ liệu
            connection.query('SELECT * FROM `chat` WHERE chat_id = ?', [chat.chat_id], (err, results) => {
                if (err) {
                    console.error('Lỗi thực thi truy vấn:', err);
                    done(err);
                } else {
                    expect(results.length).toBe(1);
                    expect(results[0].chat_id).toBe(chat.chat_id);
                    expect(results[0].content).toBe(chat.content);
                    expect(results[0].date_time.toISOString().split('T')[0]).toBe(chat.date_time.toISOString().split('T')[0]);
                    expect(results[0].status).toBe(chat.status);
                    expect(results[0].from).toBe(chat.from);
                    expect(results[0].to).toBe(chat.to);
                    done();
                }
            });
        }
    });
}, 15000); // Tăng timeout lên 15 giây