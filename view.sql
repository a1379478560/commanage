drop view if exists score_sum_VIEW;
CREATE VIEW score_sum_VIEW AS
SELECT 0 id,
        max(member.name) name,
        max(member.post) post,
        max(member.mem_id) mem_id,
        max(actinfo.name) actname,
        count(actrecord.score) join_time,
        sum(actrecord.score) score

FROM  activityRecord_memberinfo member,
  activityRecord_actinfo actinfo,
  activityRecord_actrecord actrecord
where actinfo.id=actrecord.act_id and actrecord.member_id=member.id
group by member.id,actinfo.id;