# Common Issues & Solutions

## Database

### Postgresql

- If `brew services start postgresql` says it has started but it isn't accepting any connection, try `brew services list`. Services with green status are OK, if it's either yellow or red, something went wrong. Then check the log `tail /usr/local/var/log/postgres.log` and try to fix the problems.

## Dev Environment

### IDE

### Java

### Python