select *from demo.esd;
# Group by function
select Gender, count(E_ID) FROM demo.esd Group by Gender;

# Having by
select Department, count(E_ID) FROM demo.esd Group by Department Having 
count(E_ID) > 200;

select*from demo.product;
select Category, sum(price) as total_price FROM demo.product 
group by Category;

select Category, sum(price) as total_price FROM demo.product 
group by Category Having sum(price) > 15000;