SELECT p1.title, p2.content
FROM post p1, post p2
WHERE p1.user_id = p2.blog_id;

SELECT B.title, C.title
FROM blog b, category c, blog_category bc
WHERE bc.blog_id = b.id AND c.id = bc.category_id
ORDER BY c.title;

SELECT *
FROM category
WHERE title NOT LIKE '%a%'
LIMIT 2;

SELECT u.username, u.family_status, c.content
FROM "user" u INNER JOIN comment c
ON u.username = c.username;

SELECT active_users.username, count(*) as amounts_of_comments
From (SELECT ALL u.username
      FROM "user" u, comment c
      WHERE u.username = c.username) as active_users
      GROUP BY username
      HAVING count(*) > 1;

SELECT u.username, COALESCE(p.title, 'No post written yet')
FROM "user" u LEFT JOIN post p
on u.id = p.user_id;

SELECT c.username, c.content, p.title
FROM comment c FULL OUTER JOIN post p
ON c.id = p.blog_id;

SELECT u.username, u.family_status, c.content
FROM "user" u INNER JOIN comment c
USING (username);

SELECT *
FROM "user" NATURAL JOIN comment;

SELECT count(*) possible_combinations, category.title
FROM blog CROSS JOIN category
GROUP BY category.title
HAVING count(*) > 0;

SELECT u.username FROM "user" u
UNION ALL
SELECT c.username FROM comment c LIMIT 5;

SELECT DISTINCT u.username FROM "user" u
EXCEPT
SELECT u.username
FROM "user" u RIGHT JOIN post p
on u.id = p.user_id;

WITH passive_users AS (
    SELECT DISTINCT u.username FROM "user" u
    EXCEPT
    SELECT u.username
    FROM "user" u RIGHT JOIN post p
    on u.id = p.user_id)
SELECT family_status, username
FROM "user" u
WHERE u.username IN (SELECT * FROM passive_users);

BEGIN;
INSERT INTO comment(id, username, content, updated_at)
VALUES(1,'kariana','Looks nice, but i can do better', '2022-12-19');
COMMIT;

BEGIN;
UPDATE "user"
SET family_status = 'married'
where family_status = 'single';

UPDATE "user"
SET family_status = 'married'
where username = 'kolyan';
COMMIT;

SELECT *
FROM "user"
WHERE CAST(id as varchar) = '1';

SELECT first_name, family_status,
   CASE WHEN first_name LIKE '%n%' THEN 'Have letter "n" in the name'
   WHEN family_status = 'married' THEN 'This person is Married'
   WHEN family_status = 'single' THEN 'This person is singe'
   WHEN family_status = 'widowed' THEN 'This person is widowed'
   ELSE 'divorced'
   END AS some_description
FROM "user";

SELECT ABS(DATE_PART('day', (SELECT c.updated_at
                          FROM comment c
                          WHERE c.id = 1
                          LIMIT 1)::date) - DATE_PART('day', CURRENT_DATE::date)) as DATEDIFF;