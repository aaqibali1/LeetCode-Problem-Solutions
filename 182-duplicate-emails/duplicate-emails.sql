# Write your MySQL query statement below
select distinct p1.email as Email from person as p1 join person as p2 
where p1.email=p2.email and p1.id!=p2.id;