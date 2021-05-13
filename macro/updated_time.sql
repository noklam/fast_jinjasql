{% macro updated_time() %}
		to_utc_timestamp(
			now(),
			'HKT'
		) AS updated_time
{% endmacro %}
