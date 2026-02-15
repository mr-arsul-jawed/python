select*from demo.product;

select Name,Stock ,
CASE 
    WHEN Stock < 400 then "urgent need of more stock"
    else "no requirement as of now"
end as production_details
from demo.product;


select Name, Price,
CASE 
   WHEN Price <= 500 then "Low Price"
   when Price >= 500 then "High Price"
   else "avg_price"
end as price_details
from demo.product;


