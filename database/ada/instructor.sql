CREATE TABLE instructor.grades (
  student_id INT NOT NULL,
  module_id INT NULL,
  grade_type VARCHAR(45) NULL,
  grade_desc VARCHAR(45) NULL,
  grade VARCHAR(45) NULL,
  due_date DATETIME NULL,
  PRIMARY KEY (student_id));
  
CREATE TABLE instructor.students (
  student_id INT NOT NULL,
  first_name VARCHAR(45) NULL,
  last_name VARCHAR(45) NULL,
  cohort VARCHAR(45) NULL,
  PRIMARY KEY (student_id));

INSERT INTO instructor.students
(SELECT * FROM ada_students.students);
  
CREATE TABLE instructor.modules (
  module_id INT NOT NULL,
  module_name VARCHAR(45) NULL,
  PRIMARY KEY (module_id));
  
INSERT INTO instructor.modules
(SELECT module_id, module_name FROM ada_students.modules);

ALTER TABLE instructor.grades
ADD  FOREIGN KEY fk_student(student_id)
	REFERENCES instructor.students (student_id)
	ON DELETE NO ACTION
	ON UPDATE CASCADE,
ADD FOREIGN KEY fk_module(module_id)
  REFERENCES instructor.modules(module_id)
  ON DELETE NO ACTION
  ON UPDATE CASCADE;

