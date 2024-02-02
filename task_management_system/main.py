from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorise_task import categorize_task
#create a task
task1=create_task('Complete Your Assignment','Finish TASK MANAGEMENT SYSTEM')
#Display the task
print('Task1:',task1)
#edit the task
edit_task(task1,new_title='Updated Assignment',new_description='Review and submit to Rashmi Mam')
#display the updated task
print('Updated Task1:',task1)
#categorize the task
categorize_task(task1,'Zappkode Academy')
#display the categorized task
print('Categorized Task1:',task1)
