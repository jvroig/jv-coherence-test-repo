# Django-api Template

This is a template to get started building on Coherence (withcoherence.com)

## To use

- Sign up for an account at app.withcoherence.com
- Import this template into a new repo
- Follow the onboarding steps on the Coherence site to set up your Cloud IDE, automatic preview environments, CI/CD pipelines, and managed cloud infrastructure

## To connect to the database from the toolbox

- Run the toolbox from the Coherence UI
- Run a terminal in the toolbox
- Use cocli to run commands in the running instance. Example:

To dump a database:

```console
cocli exec backend 'DB_SOCKET_NAME=$(compgen -A variable | grep _SOCKET) && PGPASSWORD="$DB_PASSWORD" pg_dump -h ${!DB_SOCKET_NAME} -U $DB_USER $DB_NAME'
```

To run the psql cli:

```console
cocli exec backend 'DB_SOCKET_NAME=$(compgen -A variable | grep _SOCKET) && PGPASSWORD="$DB_PASSWORD" psql -h ${!DB_SOCKET_NAME} -U $DB_USER $DB_NAME'
Going to run command (backend): [DB_SOCKET_NAME=$(compgen -A variable | grep _SOCKET) && PGPASSWORD="$DB_PASSWORD" psql -h ${!DB_SOCKET_NAME} -U $DB_USER $DB_NAME]
psql (13.7 (Debian 13.7-1.pgdg100+1))
Type "help" for help.

main=> \l
                                                List of databases
     Name      |       Owner       | Encoding |  Collate   |   Ctype    |            Access privileges            
---------------+-------------------+----------+------------+------------+-----------------------------------------
 cloudsqladmin | cloudsqladmin     | UTF8     | en_US.UTF8 | en_US.UTF8 | 
 main          | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | 
 postgres      | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | 
 template0     | cloudsqladmin     | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/cloudsqladmin                       +
               |                   |          |            |            | cloudsqladmin=CTc/cloudsqladmin
 template1     | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/cloudsqlsuperuser                   +
               |                   |          |            |            | cloudsqlsuperuser=CTc/cloudsqlsuperuser
(5 rows)

main=>
main=> select * from polls_question;
 id | question_text |           pub_date            
----+---------------+-------------------------------
  7 | Default poll  | 2022-07-27 18:45:36.004697+00
(1 row)

main=>
main=> select * from polls_choice;
 id | choice_text | votes | question_id 
----+-------------+-------+-------------
 12 | Option 2    |     0 |           7
 11 | Option 1    |     3 |           7
 13 | Option 3    |     1 |           7
(3 rows)

main=> 
```

## To connect to the database from the workspace

- Launch the workspace from the Coherence UI
- Run a terminal in the toolbox
- Use cocli to run commands in the running instance. Example:

To dump a database:

```console
cocli exec backend 'DB_PORT=$(compgen -A variable | grep _DB1_PORT) && PGPASSWORD="$DB_PASSWORD" pg_dump -h localhost -p ${!DB_PORT} -U $DB_USER $DB_NAME'
```

To run the psql cli:

```console
cocli exec backend 'DB_PORT=$(compgen -A variable | grep _DB1_PORT) && PGPASSWORD="$DB_PASSWORD" psql -h localhost -p ${!DB_PORT} -U $DB_USER $DB_NAME'
Going to run command (backend): [DB_SOCKET_NAME=$(compgen -A variable | grep _SOCKET) && PGPASSWORD="$DB_PASSWORD" psql -h ${!DB_SOCKET_NAME} -U $DB_USER $DB_NAME]
psql (13.7 (Debian 13.7-1.pgdg100+1))
Type "help" for help.

main=> \l
                                                List of databases
     Name      |       Owner       | Encoding |  Collate   |   Ctype    |            Access privileges            
---------------+-------------------+----------+------------+------------+-----------------------------------------
 cloudsqladmin | cloudsqladmin     | UTF8     | en_US.UTF8 | en_US.UTF8 | 
 main          | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | 
 postgres      | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | 
 template0     | cloudsqladmin     | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/cloudsqladmin                       +
               |                   |          |            |            | cloudsqladmin=CTc/cloudsqladmin
 template1     | cloudsqlsuperuser | UTF8     | en_US.UTF8 | en_US.UTF8 | =c/cloudsqlsuperuser                   +
               |                   |          |            |            | cloudsqlsuperuser=CTc/cloudsqlsuperuser
(5 rows)

main=>
main=> select * from polls_question;
 id | question_text |           pub_date            
----+---------------+-------------------------------
  7 | Default poll  | 2022-07-27 18:45:36.004697+00
(1 row)

main=>
main=> select * from polls_choice;
 id | choice_text | votes | question_id 
----+-------------+-------+-------------
 12 | Option 2    |     0 |           7
 11 | Option 1    |     3 |           7
 13 | Option 3    |     1 |           7
(3 rows)

main=> 
```
