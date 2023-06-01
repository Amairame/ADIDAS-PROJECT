SELECT *
FROM [Adidas US Sales Datasets4]


--- Use Distinct to see the different Retailers, Regions, States, Products, Sales methods, 
 
SELECT DISTINCT(Region)
FROM [Adidas US Sales Datasets4]

SELECT DISTINCT(Product)
FROM [Adidas US Sales Datasets4]

SELECT DISTINCT(Sales_Method)
FROM [Adidas US Sales Datasets4]

SELECT DISTINCT(Retailer)
FROM [Adidas US Sales Datasets4]

-- Count
-- To get the total number of rows in the data
SELECT COUNT(*)
FROM [Adidas US Sales Datasets4]

--- Count of product being sold  
SELECT Product, Count(Product) as Product_count
FROM [Adidas US Sales Datasets4]
group by Product




---Max Min Avg
 
SELECT MAX(Operating_Profit) as Max_Operating_Profit
from [Adidas US Sales Datasets4]
 
SELECT MAX(Price_per_Unit) as MAX_Price
from [Adidas US Sales Datasets4]
 
SELECT Retailer , MAX(Units_Sold) as MAX_Unitsold
from [Adidas US Sales Datasets4]
group by Retailer
order by MAX_Unitsold desc
 
SELECT Sales_Method , MAX(Price_per_Unit) as MAX_UnitPrice
from [Adidas US Sales Datasets4] 
group by Sales_Method
order by MAX_UnitPrice desc

SELECT Sales_Method , MAX(Units_Sold) as MAX_Unitsold
from [Adidas US Sales Datasets4] 
group by Sales_Method
order by MAX_Unitsold desc
 
SELECT MIN(Price_per_Unit) as MIN_Price
from [Adidas US Sales Datasets4] 
 
SELECT AVG(Price_per_Unit) as Avg_Price
from[Adidas US Sales Datasets4] 
 
SELECT AVG(Units_Sold) as Avg_Unit_Sold
from [Adidas US Sales Datasets4] 
 
SELECT AVG(Total_Sales) as Avg_Total_Sales
from [Adidas US Sales Datasets4] 



 -----WHERE STATEMENT, LIKE, NULL and not null, IN

SELECT *
FROM [Adidas US Sales Datasets4] 
where Retailer = 'West Gear' and Price_per_Unit >10



----GROUP BY
 
SELECT Product, Price_per_Unit, COUNT(Price_per_Unit) as Price_per_unit_count
FROM [Adidas US Sales Datasets4]
where Price_per_Unit >= 70
GROUP BY Product,Price_per_Unit 
ORDER BY Price_per_unit_count desc



 --- CASE STATEMENT
 
SELECT Retailer, Product, Price_per_Unit, 
case
when Price_per_Unit > 100 then 'Expensive'
else 'Fair price'
end
from [Adidas US Sales Datasets4]
order by Price_per_Unit
 
SELECT Retailer, Product, Price_per_Unit, Units_Sold,
case
when Price_per_Unit > 100 then 'Expensive'
else 'Fair price'
end
from [Adidas US Sales Datasets4]
where Units_Sold > 1000
order by Price_per_Unit desc
 
SELECT Retailer, Product, Price_per_Unit, Units_Sold,
case
when Price_per_Unit > 100 then 'Expensive'
else 'Average'
end
from [Adidas US Sales Datasets4]
where Units_Sold > 1000
order by Units_Sold desc, Price_per_Unit desc
 
SELECT Retailer, Product, Price_per_Unit, Sales_Method, Units_Sold, sum(Units_Sold) as Total_Unit_Sold,
case
when Price_per_Unit > 100 then 'Expensive'
else 'Average'
end
from [Adidas US Sales Datasets4]
where Units_Sold > 1000
group by Retailer, Product, Price_per_Unit,Units_Sold, Sales_Method
order by Price_per_Unit desc, Total_Unit_Sold desc
 
SELECT Retailer, Product, Price_per_Unit, Units_Sold, count(Units_Sold) as Total_Unit_Sold,
case
when Price_per_Unit > 100 then 'Expensive'
else 'Average'
end
from [Adidas US Sales Datasets4]
where Units_Sold > 1000
group by Retailer, Product, Price_per_Unit,Units_Sold
order by Price_per_Unit desc
 
--- Having clause
 
SELECT Retailer,  Sales_Method, sum(Units_Sold) as Sum
FROM [Adidas US Sales Datasets4]
GROUP BY Retailer,Sales_Method
HAVING sum(Units_Sold) >10 


---Partition by 
SELECT Region, Sales_Method, Product, sum(Units_Sold) OVER (PARTITION BY Product) as TotalSales
FROM [Adidas US Sales Datasets4]
 

---- CTEs

---generate a report with the highest daily revenue by branch for Year 2021

WITH Simple_CTE
AS (
    SELECT Retailer, Sales_Method, Total_Sales, [Year]
    FROM [Adidas US Sales Datasets4]
    WHERE [Year] = 2021
    GROUP BY Retailer, Sales_Method, Total_Sales, [Year]

)
SELECT Retailer, Sales_Method, MAX(Total_Sales) as max_daily_sales
FROM Simple_CTE
GROUP BY Retailer, Sales_Method
ORDER BY MAX(Total_Sales) DESC


---- Subqueries
 
Select Retailer, Price_per_Unit, (select AVG(Total_Sales) from [Adidas US Sales Datasets4]) as average
from [Adidas US Sales Datasets4]

--- product with the Max sales
 
SELECT Product, MAX(Total_Sales) AS Max_sales
FROM [Adidas US Sales Datasets4]
GROUP BY Product
ORDER BY Max_sales DESC


--- Which Product has the highest total sales?
 
SELECT Product, SUM(Total_Sales) AS highest_sales
FROM [Adidas US Sales Datasets4]
GROUP BY Product
ORDER BY highest_sales DESC

-- Which Product is the most sold?
 
SELECT Product, SUM(Units_Sold) AS Top_Productsold
FROM [Adidas US Sales Datasets4]
GROUP BY Product
ORDER BY Top_Productsold DESC

---- Average sales per year
 
Select Year, Avg(Total_Sales) as AVG_Sales
From [Adidas US Sales Datasets4]
GROUP BY Year
ORDER BY AVG_Sales DESC

-- Which stores have the highest sales?
 
SELECT Retailer, SUM(Total_Sales) AS Retailer_HighestTotalsale
FROM [Adidas US Sales Datasets4]
GROUP BY Retailer
ORDER BY Retailer_HighestTotalsale DESC
 
SELECT Retailer, SUM(Units_Sold) AS Retailer_Unitsold
FROM [Adidas US Sales Datasets4]
GROUP BY Retailer
ORDER BY Retailer_Unitsold DESC
 