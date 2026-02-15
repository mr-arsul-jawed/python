SELECT*FROM classicmodels.customers; 

select contactFirstName,contactLastName,city, sum(salesRepEmployeeNumber) 
from classicmodels.customers
group by contactFirstName,contactLastName,city;

select contactFirstName,contactLastName,city,salesRepEmployeeNumber,
sum(salesRepEmployeeNumber) 
over (partition by contactFirstName order by city ) 
from classicmodels.customers;

select*from classicmodels.products;

select*,row_number()
over(partition by products.productName) from classicmodels.products;


