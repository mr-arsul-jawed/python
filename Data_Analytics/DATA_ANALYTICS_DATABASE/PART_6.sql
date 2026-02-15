select*from sakila.payment;

select date(payment_date) as dates from sakila.payment;
select time(payment_date) as dates from sakila.payment;
select day(payment_date) as dates from sakila.payment;
select dayname(payment_date) as dates from sakila.payment;
select dayofweek(payment_date) as dates from sakila.payment;
select monthname(payment_date) as dates from sakila.payment;
select year(payment_date) as dates from sakila.payment;
select datediff(shippedDate, orderDate) as dates from sakila.payment;
select hour(payment_date) as hour from sakila.payment;