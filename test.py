# %%
from __future__ import unicode_literals
import unittest
from jinja2 import DictLoader
from jinja2 import Environment
from jinjasql import JinjaSql
from jinjasql.core import MissingInClauseException, InvalidBindParameterException
from datetime import date
from yaml import safe_load_all
from os.path import dirname, abspath, join
# %%
utils = """
        {% macro print_where(value) -%}
        WHERE dummy_col = {{value}}
        {%- endmacro %}
        """
source = """
        {% import 'utils.sql' as utils %}
        select * from dual {{ utils.print_where(100) }}
        """
loader = DictLoader({"utils.sql" : utils})
env = Environment(loader=loader)
j = JinjaSql(env)
# %%
utils
# %%
query, bind_params = j.prepare_query(source, _DATA)
expected_query = "select * from dual WHERE dummy_col = %s"


# %%
bind_params

# %%
