create view count_of_customers as
select country, count(customerNumber) from classicmodels.customers
group by country;

create view france_data as
select*from customers where country = "France";