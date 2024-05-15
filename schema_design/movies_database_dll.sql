
CREATE SCHEMA "content" AUTHORIZATION habrpguser;

CREATE TABLE "content".film_work (
	id uuid NOT NULL,
	title text NOT NULL,
	description text NULL,
	creation_date date NULL,
	rating float4 NULL,
	"type" text NOT NULL,
	created timestamptz NULL,
	modified timestamptz NULL,
	CONSTRAINT film_work_pkey PRIMARY KEY (id)
);
CREATE INDEX film_work_creation_date_type_rating_idx ON content.film_work USING btree (creation_date, type, rating);

CREATE TABLE "content".genre (
	id uuid NOT NULL,
	"name" text NOT NULL,
	description text NULL,
	created timestamptz NULL,
	modified timestamptz NULL,
	CONSTRAINT genre_pkey PRIMARY KEY (id)
);

CREATE TABLE "content".person (
	id uuid NOT NULL,
	full_name text NOT NULL,
	created timestamptz NULL,
	modified timestamptz NULL,
	CONSTRAINT person_pkey PRIMARY KEY (id)
);

CREATE TABLE "content".genre_film_work (
	id uuid NOT NULL,
	genre_id uuid NOT NULL,
	film_work_id uuid NOT NULL,
	created timestamptz NULL,
	CONSTRAINT genre_film_work_pkey PRIMARY KEY (id),
	CONSTRAINT genre_film_work_film_work_id_fkey FOREIGN KEY (film_work_id) REFERENCES "content".film_work(id),
	CONSTRAINT genre_film_work_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES "content".genre(id)
);


CREATE TABLE "content".person_film_work (
	id uuid NOT NULL,
	film_work_id uuid NOT NULL,
	person_id uuid NOT NULL,
	"role" text NOT NULL,
	created timestamptz NULL,
	CONSTRAINT person_film_work_pkey PRIMARY KEY (id),
	CONSTRAINT person_film_work_film_work_id_fkey FOREIGN KEY (film_work_id) REFERENCES "content".film_work(id) ON DELETE CASCADE,
	CONSTRAINT person_film_work_person_id_fkey FOREIGN KEY (person_id) REFERENCES "content".person(id) ON DELETE CASCADE
);
CREATE UNIQUE INDEX film_work_person_role_idx ON content.person_film_work USING btree (film_work_id, person_id, role);


