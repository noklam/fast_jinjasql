{% sql 'users_select_cond', note='select users with condition' %}
    SELECT *
    FROM user
    {% if users_ids %}
        WHERE user_id IN ({{ users_ids|join(', ') }})
    {% endif %}
{% endsql %}