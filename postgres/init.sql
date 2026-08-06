-- ======================================
-- ShopSmart Workshop Database
-- ======================================

CREATE TABLE customers (

    id SERIAL PRIMARY KEY,

    customer_code VARCHAR(30) UNIQUE NOT NULL,

    first_name VARCHAR(50) NOT NULL,

    city VARCHAR(100),

    status VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100) UNIQUE NOT NULL,

    status VARCHAR(20) NOT NULL
);

CREATE TABLE products (

    id SERIAL PRIMARY KEY,

    sku VARCHAR(30) UNIQUE NOT NULL,

    category_id INT NOT NULL REFERENCES categories(id),

    name VARCHAR(200) NOT NULL,

    price NUMERIC(10,2) NOT NULL,

    status VARCHAR(20) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE inventory (

    id SERIAL PRIMARY KEY,

    product_id INT REFERENCES products(id),

    quantity INT,

    status VARCHAR(30),

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (

    id SERIAL PRIMARY KEY,

    customer_id INT REFERENCES customers(id),

    amount NUMERIC(10,2),

    status VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (

    id SERIAL PRIMARY KEY,

    order_id INT REFERENCES orders(id),

    product_id INT REFERENCES products(id),

    quantity INT,

    amount NUMERIC(10,2)
);

CREATE TABLE payments (

    id SERIAL PRIMARY KEY,

    order_id INT REFERENCES orders(id),

    amount NUMERIC(10,2),

    type VARCHAR(50),

    status VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE returns (

    id SERIAL PRIMARY KEY,

    order_id INT REFERENCES orders(id),

    amount NUMERIC(10,2),

    type VARCHAR(50),

    status VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE marketing_campaigns (

    id SERIAL PRIMARY KEY,

    name VARCHAR(200),

    type VARCHAR(30),

    status VARCHAR(30),

    start_date DATE,

    end_date DATE
);

CREATE TABLE customer_campaigns (

    id SERIAL PRIMARY KEY,

    customer_id INT REFERENCES customers(id),

    campaign_id INT REFERENCES marketing_campaigns(id),

    clicked_at TIMESTAMP,

    converted BOOLEAN
);