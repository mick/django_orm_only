==Just using the Django ORM

I really like the django orm, but I dont always want to use all of django. Here is a quick setup that imports just the needed parts of Django to use the ORM.

It still includes manage.py so you can do handy commands like syncdb, sql, etc. (Plus you could add south for migrations)

Settings for this are in settings.py as normal. Configure that as needed. Otherwise assuming you have django running:

    python manage.py sql orm_only

Should result in:

    BEGIN;
    CREATE TABLE "orm_only_newtable" (
        "id" serial NOT NULL PRIMARY KEY,
        "text" varchar(255) NOT NULL
    )
    ;
    COMMIT;


-Mick Thompson [@dthompson](http://twitter.com/dthompson)
