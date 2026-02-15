select*from demo.esd;

-- UNION--
SELECT First_Name,Department from demo.esd
union
select Full_Name,Department from demo.esd;


-- UNION ALL--
SELECT First_Name,Department from demo.esd
union all
select Full_Name,Department from demo.esd;

-- intersect--
SELECT Job_Title, Department
FROM demo.esd
WHERE Job_Title IN (
    SELECT Full_Name FROM demo.esd
);


