const mysql = require('mysql');

function addToCart(cart, callback) {
    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'Ngocha7890',
        database: 'bookshop_test'
    });

    connection.connect((err) => {
        if (err) {
            return callback(err);
        }

        const query = `INSERT INTO cart (cart_id, qty, user_email, product_id) VALUES (?, ?, ?, ?)`;
        const values = [
            cart.cart_id,
            cart.qty,
            cart.user_email,
            cart.product_id
        ];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    });
}

function deleteFromCart(product_id, callback) {
    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'Ngocha7890',
        database: 'bookshop_test'
    });

    connection.connect((err) => {
        if (err) {
            return callback(err);
        }

        const query = `DELETE FROM cart WHERE product_id = ?`;
        const values = [product_id];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    });
}

function updateCart(cart, callback) {
    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: 'Ngocha7890',
        database: 'bookshop_test'
    });

    connection.connect((err) => {
        if (err) {
            return callback(err);
        }

        const query = `UPDATE cart SET qty = ?, user_email = ?, product_id = ? WHERE cart_id = ?`;
        const values = [
            cart.qty,
            cart.user_email,
            cart.product_id,
            cart.cart_id
        ];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    });
}

module.exports = { addToCart, deleteFromCart, updateCart };

const mysql = require('mysql');

function addChat(chat, callback) {
    const connection = mysql.createConnection({
       });

    connection.connect((err) => {
        if (err) {
            return callback(err);
        }

        const query = `INSERT INTO chat (chat_id, content, date_time, status, \`from\`, \`to\`) VALUES (?, ?, ?, ?, ?, ?)`;
        const values = [
            chat.chat_id,
            chat.content,
            chat.date_time,
            chat.status,
            chat.from,
            chat.to
        ];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    });
}

module.exports = addChat;

const mysql = require('mysql');

function register(user, callback) {

        const query = `INSERT INTO user (fname, lname, email, password, mobile, joined_date, verification_code, gender_gender_id, status_status_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)`;
        const values = [
            user.fname,
            user.lname,
            user.email,
            user.password,
            user.mobile,
            user.joined_date,
            user.verification_code,
            user.gender_gender_id,
            user.status_status_id
        ];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    };


module.exports = register;


const mysql = require('mysql');

function updateUser(user, callback) {


    

        const query = `UPDATE user SET fname = ?, lname = ?, password = ?, mobile = ?, joined_date = ?, verification_code = ?, gender_gender_id = ?, status_status_id = ? WHERE email = ?`;
        const values = [
            user.fname,
            user.lname,
            user.password,
            user.mobile,
            user.joined_date,
            user.verification_code,
            user.gender_gender_id,
            user.status_status_id,
            user.email
        ];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    };


module.exports = updateUser;


const mysql = require('mysql');

function addWishlist(wishlist, callback) {

        const query = `INSERT INTO watchlist (w_id, user_email, product_id) VALUES (?, ?, ?)`;
        const values = [
            wishlist.w_id,
            wishlist.user_email,
            wishlist.product_id
        ];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    };


function deleteWishlist(user_email, callback) {


        const query = `DELETE FROM watchlist WHERE user_email = ?`;
        const values = [user_email];

        connection.query(query, values, (err, results) => {
            connection.end();
            callback(err, results);
        });
    };


module.exports = { addWishlist, deleteWishlist };