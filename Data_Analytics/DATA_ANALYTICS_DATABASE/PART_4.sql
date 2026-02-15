select*from demo.esd;

select concat(Job_Title," - ",Department) as Designation 
from demo.esd;

select concat_ws(" - ",Job_Title, Department, Gender) as Emp_Details 
from demo.esd;

select length(Annual_Salary) as digitCount from demo.esd;
select upper(Full_Name) as upper_names from demo.esd;
select lower(Full_Name) as lower_names from demo.esd;
select left(Full_Name, 4) as username from demo.esd;
select right(Full_Name, 4) as username from demo.esd;
select mid(Full_Name, 4) as mid_name from demo.esd;


 