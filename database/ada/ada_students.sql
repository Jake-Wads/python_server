INSERT INTO ada_students.modules
	(module_id, module_name, module_days)
VALUES
	(1,"Fundamentals",4.5),
	(2,"Excel_Stats" ,5.5),
	(3,"SQL_CLI_Git" ,7),
	(4,"Python" ,10),
    (5,"Regression" ,7),
    (6,"Classification" ,7),
    (7,"Clustering" ,7),
    (8,"TimeSeries" ,6),
    (9,"AnomalyDetection" ,4),
    (10,"NLP" ,6),
    (11,"DistributedML" ,5),
    (12,"Advanced_Topics" ,5),
    (13,"Storytelling" ,3),
    (14,"DomainExpertise" ,1),
    (15,"Capstone" ,11)
;
    
INSERT INTO ada_students.student_groups
	(student_module_id, student_id, module_id, group_id)
VALUES
    ("683_4", 683, 4, 1),
    ("684_4", 684, 4, 1),
    ("674_4", 674, 4, 2),
    ("677_4", 677, 4, 2),
    ("675_4", 675, 4, 3),
    ("679_4", 670, 4, 3),
    ("664_4", 664, 4, 4),
    ("668_4", 668, 4, 4),
    ("670_4", 670, 4, 5),
    ("671_4", 671, 4, 5),
    ("663_4", 663, 4, 6),
    ("680_4", 680, 4, 6),
    ("673_4", 673, 4, 7),
    ("665_4", 665, 4, 7),
    ("678_4", 678, 4, 8),
    ("667_4", 667, 4, 8),
    ("669_4", 669, 4, 9),
    ("661_4", 661, 4, 9)
    ;
    
INSERT INTO ada_students.students
	(student_id, first_name, last_name, cohort)
VALUES
	("661", "Sandy", "Graham" , "ada"),
    ("663", "Chad", "Hackney", "ada"),
    ("664", "Jessica", "Ruiz", "ada"),
    ("665", "Matthew", "Zapata", "ada"),
    ("667", "Kathryn", "Salts", "ada"),
    ("668", "Steven", "Garis", "ada"),
    ("669", "Joseph", "Burton", "ada"),
    ("670", "Nicole", "Garza", "ada"),
    ("671", "Norrick", "McGee", "ada"),
    ("673", "Gary", "Gonzenbach", "ada"),
    ("674", "Matthew", "Capper", "ada"),
    ("675", "Cody", "Watson", "ada"),
    ("677", "Michael", "Moran", "ada"),
    ("678", "Ednalyn", "De Dios", "ada"),
    ("679", "Jason", "Dunn", "ada"),
    ("680", "Orion", "Wills", "ada"),
    ("683", "Eric", "Escalante", "ada"),
    ("684", "Stacy", "Johnson", "ada")
    ;

ALTER TABLE ada_students.student_groups
ADD  FOREIGN KEY fk_student(student_id)
	REFERENCES ada_students.students (student_id)
	ON DELETE NO ACTION
	ON UPDATE CASCADE,
ADD FOREIGN KEY fk_module(module_id)
  REFERENCES ada_students.modules(module_id)
  ON DELETE NO ACTION
  ON UPDATE CASCADE;


SELECT sg.group_id AS team_id
			, sg.module_id
            , m.module_name
            , s.student_id AS my_id
            , s.first_name AS my_firstname
            , s.last_name AS my_lastname
            , sg2.student_id AS teammate_id
            , s2.first_name AS teammate_firstname
            , s2.last_name AS teammate_lastname
FROM ada_students.students s
JOIN ada_students.student_groups sg ON s.student_id = sg.student_id
JOIN ada_students.modules m ON sg.module_id = m.module_id
JOIN ada_students.student_groups sg2 ON sg.group_id = sg2.group_id AND s.student_id != sg2.student_id
JOIN ada_students.students s2 ON sg2.student_id = s2.student_id
WHERE s.first_name = "Eric"
;



INSERT INTO ada_students.student_groups
	(student_module_id, student_id, module_id, group_id)
VALUES
	("663_5",663,5,1),
	("675_5",675,5,2),
	("678_5",678,5,3),
	("683_5",683,5,1),
	("673_5",673,5,4),
	("679_5",679,5,5),
	("664_5",664,5,4),
	("669_5",669,5,6),
	("667_5",667,5,7),
	("674_5",674,5,7),
	("665_5",665,5,8),
	("677_5",677,5,8),
	("670_5",670,5,4),
	("671_5",671,5,2),
	("680_5",680,5,5),
	("661_5",661,5,3),
	("668_5",668,5,6)
    ;
    

CREATE TABLE `ada_students`.`seating` (
  `student_id` INT NOT NULL,
  `row_number` INT NULL,
  `column_number` INT NULL,
  `seat_id` VARCHAR(45) NULL,
  `start_date` DATETIME NULL,
  `end_date` DATETIME NULL,
  PRIMARY KEY (`student_id`));


INSERT INTO ada_students.seating
	(student_id, row_number, column_number, seat_id, start_date, end_date)
VALUES
	(661, 1, 6, "1_6", "2019-03-11","2019-03-26"),
    (663, 1, 2, "1_2", "2019-03-11","2019-03-26"),
    (664, 3, 6, "3_6", "2019-03-11","2019-03-26"),
    (665, 2, 8, "2_8", "2019-03-11","2019-03-26"),
    (667, 2, 6, "2_6", "2019-03-11","2019-03-26"),
    (668, 2, 4, "2_4", "2019-03-11","2019-03-26"),
    (669, 2, 3, "2_3", "2019-03-11","2019-03-26"),
    (670, 3, 7, "3_7", "2019-03-11","2019-03-26"),
    (671, 1, 4, "1_4", "2019-03-11","2019-03-26"),
    (673, 3, 8, "3_8", "2019-03-11","2019-03-26"),
    (674, 2, 5, "2_5", "2019-03-11","2019-03-26"),
    (675, 1, 3, "1_3", "2019-03-11","2019-03-26"),
    (677, 2, 7, "2_5", "2019-03-11","2019-03-26"),
    (678, 1, 5, "1_5", "2019-03-11","2019-03-26"),
    (679, 1, 7, "1_7", "2019-03-11","2019-03-26"),
    (680, 1, 8, "1_8", "2019-03-11","2019-03-26"),
    (683, 1, 1, "1_1", "2019-03-11","2019-03-26")
    ;
    

