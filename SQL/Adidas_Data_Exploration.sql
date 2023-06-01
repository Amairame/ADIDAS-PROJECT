--- Temp Table, do it at the top 

CREATE TABLE #temp_Sales (
    Retailer varchar(50),
    Retailer_ID INT,
    Year  INT,
    Region varchar(100),
    State varchar(50),
    City varchar(50),
    Product varchar(50),
    Price_per_Unit money,
    Units_Sold money,
    Total_Sales money,
    Operating_Profit money,
    Sales_Method varchar(100)
)

insert into #temp_Sales 
SELECT *
FROM [Adidas US Sales Datasets4]

---- Select TOP10
 
SELECT TOP 10 *
FROM [Adidas US Sales Datasets4]

SELECT Product, Count(distinct(Product))
FROM [Adidas US Sales Datasets4]
group by Product

SELECT *
FROM [Adidas US Sales Datasets4] 
where Year = 2021
 
SELECT *
FROM ADIDAS.salesdata
where Retailer = 'West Gear'

SELECT Product, Price_per_Unit, COUNT(Price_per_Unit) as Price_per_unit_count
FROM [Adidas US Sales Datasets4]
GROUP BY Product,Price_per_Unit 
ORDER BY Price_per_unit_count desc

SELECT Region, Retailer, COUNT(Retailer) OVER (PARTITION BY Retailer) as TotalRetailer
FROM [Adidas US Sales Datasets4]
 
SELECT Region, Retailer, count(Retailer)
from [Adidas US Sales Datasets4]
group by Region, Retailer

---- Count distinct and partition by
 
select Region, count(distinct Retailer) as Total_retailer
from [Adidas US Sales Datasets4]
Group by Region
 

ELECT Retailer, AVG(Total_Sales) AS Retailer_avgTotalsale
FROM [Adidas US Sales Datasets4]
GROUP BY Retailer
ORDER BY Retailer_avgTotalsale DESC