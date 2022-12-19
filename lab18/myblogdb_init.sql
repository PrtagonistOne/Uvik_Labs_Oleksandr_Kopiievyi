CREATE TABLE IF NOT EXISTS Category (
   id BIGINT PRIMARY KEY,
   title VARCHAR(25) UNIQUE NOT NULL,
   description VARCHAR(250) NOT NULL,
   is_public BOOLEAN NOT NULL default '1',
   CONSTRAINT proper_title CHECK ( Category.title ~* '^[a-zA-Z]([\w -]*[a-zA-Z])?$' ),
   CONSTRAINT proper_description CHECK ( Category.description ~* '.*' )

);
CREATE INDEX IF NOT EXISTS category_id_index ON Category (id);


CREATE TABLE IF NOT EXISTS Blog (
   id BIGINT PRIMARY KEY,
   title VARCHAR(25) UNIQUE NOT NULL,
   content TEXT NOT NULL,
   description VARCHAR(250) NOT NULL,
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
   is_public BOOLEAN NOT NULL DEFAULT '1',
   CONSTRAINT proper_title CHECK ( Blog.title ~* '^[a-zA-Z]([\w -]*[a-zA-Z])?$' ),
   CONSTRAINT proper_description CHECK ( Blog.description ~* '.*' )

);
CREATE INDEX IF NOT EXISTS blog_id_index ON Blog (id);


CREATE TABLE IF NOT EXISTS Blog_Category (
   blog_id BIGINT NOT NULL,
   category_id BIGINT NOT NULL,
   PRIMARY KEY (blog_id, category_id),
   FOREIGN KEY (blog_id) REFERENCES Blog (id),
   FOREIGN KEY (category_id) REFERENCES Category (id)
);

CREATE TYPE _family_status AS ENUM ('single', 'married', 'divorced', 'widowed');
CREATE TABLE IF NOT EXISTS "user" (
    id BIGINT PRIMARY KEY,
    username varchar(25) UNIQUE NOT NULL,
    email varchar(50) UNIQUE NOT NULL,
    password_hash VARCHAR(60) NOT NULL,
    family_status _family_status NULL DEFAULT 'single',
    first_name varchar(25) NOT NULL,
    last_name varchar(25) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT '1',
    CONSTRAINT proper_username CHECK ( "user".username ~* '^[A-Za-z0-9]+$' ),
    CONSTRAINT proper_email CHECK ( "user".email ~* '^[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+[.][A-Za-z]+$' ),
    CONSTRAINT proper_first_name CHECK ( "user".first_name ~* '^[a-z]+$' ),
    CONSTRAINT proper_last_name CHECK ( "user".last_name ~* '^[a-z]+$' )

);
CREATE INDEX IF NOT EXISTS user_id_index ON "user" (id);

CREATE TABLE IF NOT EXISTS Post (
    id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL,
    blog_id BIGINT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user" (id),
    FOREIGN KEY (blog_id) REFERENCES Blog (id),
    title varchar(25) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at DATE NOT NULL,
    get_photo BYTEA NOT NULL,
    CONSTRAINT proper_title CHECK ( Post.title ~* '^[a-zA-Z]([\w -]*[a-zA-Z])?$' )

);
CREATE INDEX IF NOT EXISTS post_id_index ON Post (id);

CREATE TABLE IF NOT EXISTS Comment (
    id BIGINT PRIMARY KEY REFERENCES Post (id),
    username varchar(25) UNIQUE NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at DATE NOT NULL,
    is_deleted BOOLEAN NOT NULL DEFAULT '0',
    CONSTRAINT proper_username CHECK ( Comment.username ~* '^[A-Za-z0-9_]+$' )

);
CREATE INDEX IF NOT EXISTS comment_id_index ON Comment (id);