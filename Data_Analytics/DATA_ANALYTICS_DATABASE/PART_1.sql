select*from demo.esd;

select E_ID, Department from demo.esd;

select E_ID,Full_Name, Department from demo.esd
WHERE Age > 30 And Annual_Salary > "40000";

select E_ID,Full_Name,Annual_Salary,Department from demo.esd
WHERE  Department = "IT" AND Annual_Salary > "40000";

select Full_Name,Department,Annual_Salary,Job_Title,Country from demo.esd
WHERE Department = "IT" OR Country="china";

select Full_Name,Department,Annual_Salary,Job_Title,Country from demo.esd
WHERE Not Department = "IT" AND Country="china";

select Full_Name,Gender,Annual_Salary,Job_Title,Country from demo.esd
WHERE Not Gender = "FEMALE" AND Country="china";

select * from demo.esd where Full_Name like 'mar%'; 

select * from demo.esd where Full_Name like '%mar';

select * from demo.esd where Full_Name like '%mar%';

select Full_Name, Age from demo.esd  where Age < 30 
order by Age;

select Full_Name, Age from demo.esd  where Age < 30 
order by Age desc;

select Full_Name, Age,Department from demo.esd  
order by Department Asc, Age desc;

select Full_Name, Age,Department from demo.esd  
order by Department ,Age ASC;

select*from demo.esd order by Department, Age asc limit 3;

