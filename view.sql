drop view if exists all_score_sum_VIEW;
CREATE VIEW all_score_sum_VIEW AS
SELECT max(member.id) id,
        max(member.name) name,
        max(member.post) post,
        max(member.mem_id) mem_id,
        count(actrecord.score) join_time,
        sum(actrecord.score) score

FROM  activityRecord_memberinfo member,
  activityRecord_actinfo actinfo,
  activityRecord_actrecord actrecord
where actinfo.id=actrecord.act_id and actrecord.member_id=member.id
group by member.id;
