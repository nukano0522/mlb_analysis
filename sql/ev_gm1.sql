select 
	cast(gm.game_dt as varchar) game_dt,
	ev.game_id ,
	gm.home_team_id,
	gm.away_team_id,
	ev.inn_ct ,
	ev.bat_home_id ,
	ev.outs_ct ,
	ev.balls_ct ,
	ev.strikes_ct ,
	ev.bat_lineup_id ,
	ev.event_tx ,
	ev.away_score_ct ,
	ev.home_score_ct ,
	ev.bat_id ,
	ev.resp_bat_hand_cd ,
	ev.pit_id ,
	ev.start_bases_cd ,
	ev.event_cd ,
	ev.bat_event_fl ,
	ev.ab_fl ,
	ev.sf_fl ,
	ev.bunt_fl ,
	ev.h_cd ,
	ev.bat_dest_id ,
	ev.base1_run_id ,
	ev.base2_run_id ,
	ev.base3_run_id ,
	ev.run1_dest_id ,
	ev.run2_dest_id ,
	ev.run3_dest_id ,
	ev.event_outs_ct ,
	ev.battedball_cd ,
	ev.battedball_loc_tx ,
	ev.fld_cd,
	ev.rbi_ct,
	ev.pitch_seq_tx 
--	ev.pa_ball_ct ,
--	ev.pa_called_ball_ct ,
--	ev.pa_intent_ball_ct ,
--	ev.pa_pitchout_ball_ct ,
--	ev.pa_hitbatter_ball_ct ,
--	ev.pa_other_ball_ct ,
--	ev.pa_strike_ct ,
--	ev.pa_called_strike_ct ,
--	ev.pa_swingmiss_strike_ct ,
--	ev.pa_foul_strike_ct ,
--	ev.pa_inplay_strike_ct ,
--	ev.pa_other_strike_ct 
from
	events ev
inner join
	games gm
on
	ev.game_id  = gm .game_id 
where 
	left(cast(gm.game_dt as varchar), 4) = '2011'
order by
	gm.game_dt ,
	gm.game_id ,
	inn_ct ,
	bat_home_id ,
	outs_ct ,
	inn_pa_ct 
limit 1000
;