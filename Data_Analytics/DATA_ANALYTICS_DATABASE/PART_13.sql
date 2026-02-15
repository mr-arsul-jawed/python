USE classicmodels;

-- NORMAL FUNCTION-- 
Delimiter && 
create procedure get_data()
begin
    select*from classicmodels.customers;
end &&
Delimiter ;

call classicmodels.get_data()


-- NORMAL FUNCTION USING IN-- 
Delimiter && 
create procedure get_limit(in x int)
begin
    select*from classicmodels.customers limit x;
end &&
Delimiter ;

call classicmodels.get_limit(5)



-- NORMAL FUNCTION USING OUT-- 

DELIMITER &&

CREATE PROCEDURE get_credit(OUT var INT)
BEGIN
    SELECT MAX(creditLimit)
    INTO var
    FROM classicmodels.customers;
END &&

DELIMITER ;

CALL classicmodels.get_credit(@m);
SELECT @m;


-- NORMAL FUNCTION USING INOUT-- 

DELIMITER &&

CREATE PROCEDURE get_name(INOUT var INT)
BEGIN
   SELECT customerName FROM customers 
   where 
   customerNumber = var;
END &&

DELIMITER ;

set @m = 125 ;
call classicmodels.get_name(@m);
select @m;