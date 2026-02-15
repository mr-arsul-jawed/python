Select*from sakila.payment;

Select sum(amount) as Total_amount from sakila.payment;
Select count(customer_id) as Total_customer from sakila.payment;
Select avg(amount) as Total_avg from sakila.payment;
Select max(amount) as max_values from sakila.payment;
Select min(amount) as min_values  from sakila.payment;
Select truncate(amount, 1) as amount from sakila.payment;
Select ceil(amount) as high_values  from sakila.payment;
Select floor(amount) as lower_values  from sakila.payment;
