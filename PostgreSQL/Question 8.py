#8. Create Courses table (cid, cname) where cid is a primary key and Student table
#(rollno, name, cid) where rollno is a primary key and cid is a foreign key.

"""
create table courses (cid int, cname text,primary key(cid));
create table student (rollno int, name text, cid int, primary key(rollno), constraint fk_cid foreign key(cid) references courses(cid))
"""