# almanac
Project Created to Demonstrate the issue faced in Django==3.2.4


Python: 3.8.7
MySQL: 8.0.19
Django: 3.2.4
OS: Centos 7


```python
  Applying nucleus.0003_nucleusdata_new_txt...Traceback (most recent call last):
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/mysql/base.py", line 73, in execute
    return self.cursor.execute(query, args)
  File "/root/almanac/venv/lib/python3.8/site-packages/MySQLdb/cursors.py", line 206, in execute
    res = self._query(query)
  File "/root/almanac/venv/lib/python3.8/site-packages/MySQLdb/cursors.py", line 319, in _query
    db.query(q)
  File "/root/almanac/venv/lib/python3.8/site-packages/MySQLdb/connections.py", line 259, in query
    _mysql.connection.query(self, query)
MySQLdb._exceptions.OperationalError: (1101, "BLOB, TEXT, GEOMETRY or JSON column 'new_txt' can't have a default value")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 21, in <module>
    main()
  File "manage.py", line 17, in main
    execute_from_command_line(sys.argv)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/root/almanac/venv/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/core/management/base.py", line 89, in wrapped
    res = handle_func(*args, **kwargs)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 244, in handle
    post_migrate_state = executor.migrate(
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 117, in migrate
    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 147, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/migrations/executor.py", line 227, in apply_migration
    state = migration.apply(state, schema_editor)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/migrations/migration.py", line 126, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/migrations/operations/fields.py", line 104, in database_forwards
    schema_editor.add_field(
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/mysql/schema.py", line 91, in add_field
    super().add_field(model, field)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 517, in add_field
    self.execute(sql, params)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 145, in execute
    cursor.execute(sql, params)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 98, in execute
    return super().execute(sql, params)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 66, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 75, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/root/almanac/venv/lib/python3.8/site-packages/django/db/backends/mysql/base.py", line 73, in execute
    return self.cursor.execute(query, args)
  File "/root/almanac/venv/lib/python3.8/site-packages/MySQLdb/cursors.py", line 206, in execute
    res = self._query(query)
  File "/root/almanac/venv/lib/python3.8/site-packages/MySQLdb/cursors.py", line 319, in _query
    db.query(q)
  File "/root/almanac/venv/lib/python3.8/site-packages/MySQLdb/connections.py", line 259, in query
    _mysql.connection.query(self, query)
django.db.utils.OperationalError: (1101, "BLOB, TEXT, GEOMETRY or JSON column 'new_txt' can't have a default value")
```
