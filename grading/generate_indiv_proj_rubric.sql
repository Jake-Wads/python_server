(select null as skill_id, null as skill, null as 'Seven', null as 'Six', null as 'Five', null as 'Four', 
        null as 'Three', null as 'Two', null as 'One', null as 'Zero'  
    FROM skills
)
union
(select null as skill_id, 'v1.0-s' as skill, null as 'Seven', null as 'Six', null as 'Five', null as 'Four', 
        null as 'Three', null as 'Two', null as 'One', null as 'Zero'  
    FROM skills
)
union
(select s.skill_id, concat(p.pipeline_name, "(", s.skill_artifact, ") - ", s.skill_name) AS skill, 
        null as 'Seven', null as 'Six', null as 'Five', null as 'Four', 
        null as 'Three', null as 'Two', null as 'One', null as 'Zero'  
    FROM skills s
    JOIN pipeline p using (pipeline_id)
    JOIN project_skill_requirement_pts pt using (skill_id)
        where pt.proj_id = 6
)
union
(select s.skill_id, s.skill_desc AS skill, 
        null as 'Seven', null as 'Six', null as 'Five', null as 'Four', 
        null as 'Three', null as 'Two', null as 'One', null as 'Zero'
    FROM skills s
    JOIN project_skill_requirement_pts pt using (skill_id)
        where pt.proj_id = 6
)
union
(
select s.skill_id, null as skill, max(s.Seven) AS 'Seven', max(s.Six) AS 'Six', 
		  max(s.Five) AS 'Five', max(s.Four) AS 'Four', max(s.Three) AS 'Three',
			max(s.Two) aS 'Two', max(s.One) AS 'One', max(s.Zero) AS 'Zero'
    From 
        (select s.skill_id,
            case when p.req_pts = 7 then p.req_pts else null
                    end as 'Seven',
            case when p.req_pts = 6 then p.req_pts else null 
                    end as 'Six',
            case when p.req_pts = 5 then p.req_pts else null 
                    end as 'Five',
            case when p.req_pts = 4 then p.req_pts else null 
                    end as 'Four',
            case when p.req_pts = 3 then p.req_pts else null 
                    end as 'Three',
            case when p.req_pts = 2 then p.req_pts else null 
                    end as 'Two',
            case when p.req_pts = 1 then p.req_pts else null 
                    end as 'One',
            case when p.req_pts = 0 then p.req_pts else null 
                    end as 'Zero'
        from skills s
        join skill_requirements r using (skill_id)
        join project_skill_requirement_pts p using (skill_id, req_id)
        where p.proj_id = 6
        ) AS s
    group by s.skill_id
)
union
(
select s.skill_id, null as skill, max(s.Seven) AS 'Seven', max(s.Six) AS 'Six', 
		  max(s.Five) AS 'Five', max(s.Four) AS 'Four', max(s.Three) AS 'Three',
			max(s.Two) aS 'Two', max(s.One) AS 'One', max(s.Zero) AS 'Zero'
    From 
        (select s.skill_id,
            case when p.req_pts = 7 then r.req_name else null
                    end as 'Seven',
            case when p.req_pts = 6 then r.req_name else null 
                    end as 'Six',
            case when p.req_pts = 5 then r.req_name else null 
                    end as 'Five',
            case when p.req_pts = 4 then r.req_name else null 
                    end as 'Four',
            case when p.req_pts = 3 then r.req_name else null 
                    end as 'Three',
            case when p.req_pts = 2 then r.req_name else null 
                    end as 'Two',
            case when p.req_pts = 1 then r.req_name else null 
                    end as 'One',
            case when p.req_pts = 0 then r.req_name else null 
                    end as 'Zero'
        from skills s
        join skill_requirements r using (skill_id)
        join project_skill_requirement_pts p using (skill_id, req_id)
        where p.proj_id = 6
        ) AS s
    group by s.skill_id
)
union
(
select s.skill_id, null as skill, max(s.Seven) AS 'Seven', max(s.Six) AS 'Six', 
		  max(s.Five) AS 'Five', max(s.Four) AS 'Four', max(s.Three) AS 'Three',
			max(s.Two) aS 'Two', max(s.One) AS 'One', max(s.Zero) AS 'Zero'
    From 
        (select s.skill_id,
            case when p.req_pts = 7 then r.req_desc else null
                    end as 'Seven',
            case when p.req_pts = 6 then r.req_desc else null 
                    end as 'Six',
            case when p.req_pts = 5 then r.req_desc else null 
                    end as 'Five',
            case when p.req_pts = 4 then r.req_desc else null 
                    end as 'Four',
            case when p.req_pts = 3 then r.req_desc else null 
                    end as 'Three',
            case when p.req_pts = 2 then r.req_desc else null 
                    end as 'Two',
            case when p.req_pts = 1 then r.req_desc else null 
                    end as 'One',
            case when p.req_pts = 0 then r.req_desc else null 
                    end as 'Zero'
        from skills s
        join skill_requirements r using (skill_id)
        join project_skill_requirement_pts p using (skill_id, req_id)
        where p.proj_id = 6
        ) AS s
    group by s.skill_id
)
order by skill_id;