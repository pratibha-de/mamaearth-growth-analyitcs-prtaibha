create database mamaearth_growth_analytics;
use mamaearth_growth_analytics;

create table customers(
customer_id varchar(10) primary key,
name varchar(50) not null,
city varchar (50) not null,
city_tier int not null,
signup_date date not null,
acquisition_source varchar (20) not null
);

create table products(
product_id varchar(10) primary key,
product_name varchar(100) not null,
category varchar (30) not null,
price decimal(10,2) not null
);

create table orders(
order_id varchar (10) primary key,
customer_id varchar(10) not null,
product_id varchar(10) not null,
order_date date not null,
quantity int not null,
discount_pct int,
payment_method varchar (10) not null,
rating int,
returned int not null default 0,
foreign key (customer_id) references customers(customer_id),
foreign key(product_id ) references products(product_id)
);
