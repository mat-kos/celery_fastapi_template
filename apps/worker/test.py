from src.app import create_app


app = create_app()


result = app.send_task('multiply', args=(3, 4))
assert result.get() == 12

result = app.send_task('add', args=(3, 4))
assert result.get() == 7

result = app.send_task('divide', args=(4, 2))
assert result.get() == 2

