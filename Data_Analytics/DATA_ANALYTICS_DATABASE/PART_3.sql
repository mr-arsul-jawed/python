select*from demo.esd;

select*from demo.esd 
where Age between 40 and 50;

select*from demo.esd 
where Annual_Salary between '40000' and '100000';

select*from demo.esd 
where Department in ("IT","Sales","Director");

select*from demo.esd 
where Country in ("China","Brazil") 
and Department in ("IT","Accounting");


select*from demo.esd 
where Country Not in ("China","Brazil");


select*from demo.esd 
where Country Not in ("China","Brazil") 
and Department in ("IT","Accounting");
