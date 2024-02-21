USE ada_students;

SELECT sga.student_id, sga.module_id, sga.group_id, s.first_name AS s1, sgb.s2 FROM student_groups sga
	LEFT JOIN students s USING(student_id)
    LEFT JOIN (SELECT sg.student_id, sg.module_id, sg.group_id, s.first_name AS s2 FROM student_groups sg
				JOIN students s USING(student_id)) sgb ON sga.group_id = sgb.group_id AND sga.module_id = sgb.module_id
	WHERE s.first_name <> sgb.s2;


INSERT INTO ada_students.student_groups 
(student_module_id, student_id, module_id, group_id)
VALUES
("663_6",663,6,1),
("675_6",675,6,2),
("678_6",678,6,3),
("683_6",683,6,4),
("673_6",673,6,5),
("679_6",679,6,4),
("664_6",664,6,6),
("669_6",669,6,5),
("667_6",667,6,6),
("674_6",674,6,7),
("665_6",665,6,2),
("677_6",677,6,3),
("670_6",670,6,8),
("671_6",671,6,1),
("680_6",680,6,7),
("661_6",661,6,2),
("668_6",668,6,8);