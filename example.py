from pathlib import Path
from datetime import date
import logfire

logfire.configure(
    send_to_logfire=True,
    token="pylf_v1_us_4X7CrfGRqNLwFLQCGjVBNZHF041vvKTZYP7FH4hkBQHw",
    service_name="starter-project"
)

with logfire.span('Asking the user for their {question}', question='birthday'):
    user_input = input('When were you born [YYYY-mm-dd]?')
    dob = date.fromisoformat(user_input)
    logfire.debug('{dob=}{age=!r}', dob=dob, age=date.today() - dob)
