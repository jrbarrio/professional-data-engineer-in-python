
-- Update with SQL to return requested information
select 
   date_part('day', tpep_pickup_datetime) as day,
   count(*) as total_rides
from taxi_rides_raw
where Payment_type = 1
group by day