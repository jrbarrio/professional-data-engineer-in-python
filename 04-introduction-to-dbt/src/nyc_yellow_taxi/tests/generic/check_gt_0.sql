{% test check_gt_0(model, column_name) %}
select fare_amount, total_amount 
from {{ model }}
where {{ column_name }} <= 0
{% endtest %}