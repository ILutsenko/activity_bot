from app import db_executor

# db_executor.create_task(2, 'test_task_2')
result = db_executor.show_all_tasks(user_id=1)
for task in result:
    print(task.task_name)