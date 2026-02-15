select*from classicmodels.customers;

select customerName,creditLimit from classicmodels.customers;

select avg(creditLimit) from classicmodels.customers;

select*from classicmodels.customers where creditLimit > 67659;

-- SUB-QUERY --
 select*from classicmodels.customers where 
 creditLimit > (select avg(creditLimit) from classicmodels.customers);
 
 
 
 