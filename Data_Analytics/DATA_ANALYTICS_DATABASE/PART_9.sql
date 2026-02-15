select*from classicmodels.products;

select productLine, count(productCode) from classicmodels.products
group by productLine;

/* INNER - JOINS*/

-- select *from classicmodels.orderdetails;

select products.productName, orderdetails.quantityOrdered from products
inner join orderdetails
on products.productCode = orderdetails.productCode;

-- here use group by--  
select products.productName, sum(orderdetails.quantityOrdered) from products
inner join orderdetails
on products.productCode = orderdetails.productCode
group by products.productName;


-- LEFT JOIN-- 
select products.productName, orderdetails.quantityOrdered from products
LEFT join orderdetails
on products.productCode = orderdetails.productCode;


-- RIGHT JOIN--
select products.productName, orderdetails.quantityOrdered from products
RIGHT join orderdetails
on products.productCode = orderdetails.productCode;


-- CROSS JOIN--
select products.productName,products.quantityInStock, orderdetails.quantityOrdered from products
cross join orderdetails
on products.productCode = orderdetails.productCode;



