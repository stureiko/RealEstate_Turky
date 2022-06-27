-- auto-generated definition
create schema real_estate collate utf8_general_ci;

create table if not exists links
(
    id   int          not null
        primary key,
    link varchar(255) not null
);