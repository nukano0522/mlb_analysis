import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')


#def get_batting_results(df, bat_id):
#    #�i�ۃC�x���g������
#    df_res = df[(df['bat_id']==bat_id) & (df['bat_event_fl']=='T')]
#    
#    #�ŐȐ�
#    
#    #�Ő�
#    df_res['ab_cum'] = df_res['ab_fl'].replace({'T': 1, 'F': 0})
#    df_res['ab_cum'] = df_res['ab_cum'].cumsum()
#    
#    #single
#    df_res['single_cum'] = 0
#    df_res.loc[df_res['h_cd']==1, 'single_cum'] = 1
#    df_res['single_cum'] = df_res['single_cum'].cumsum()
#     
#    #double
#    df_res['double_cum'] = 0
#    df_res.loc[df_res['h_cd']==2, 'double_cum'] = 1
#    df_res['double_cum'] = df_res['double_cum'].cumsum()
#    
#    #triple
#    df_res['triple_cum'] = 0
#    df_res.loc[df_res['h_cd']==3, 'triple_cum'] = 1
#    df_res['triple_cum'] = df_res['triple_cum'].cumsum()
#    
#    #homerun
#    df_res['homerun_cum'] = 0
#    df_res.loc[df_res['h_cd']==4, 'homerun_cum'] = 1
#    df_res['homerun_cum'] = df_res['homerun_cum'].cumsum()
#    
#    #���Ő�
#    df_res['hit_cum'] = df_res['single_cum'] + df_res['double_cum'] + df_res['triple_cum'] + df_res['homerun_cum']
#     
#    #�ۑ�
#    df_res['base_hit_cum'] = df_res['single_cum']*1 + df_res['double_cum']*2 + df_res['triple_cum']*3 + df_res['homerun_cum']*4
#    
#    #�œ_
#    df_res['rbi_cum'] = df_res['rbi_ct'].cumsum()
#    
#    #�l��
#    df_res['walk_cum'] = 0
#    df_res.loc[df_res['event_cd'].isin([14, 15]), 'walk_cum'] = 1
#    df_res['walk_cum'] = df_res['walk_cum'].cumsum()
#    
#    #����
#    df_res['dead_cum'] = 0
#    df_res.loc[df_res['event_cd'].isin([16]), 'dead_cum'] = 1
#    df_res['dead_cum'] = df_res['dead_cum'].cumsum()
#    
#    #�]��
#    df_res['sf_cum'] = df_res['sf_fl'].replace({'T': 1, 'F': 0})
#    df_res['sf_cum'] = df_res['sf_cum'].cumsum()
#    
#    #�O�U
#    df_res['stout_cum'] = 0
#    df_res.loc[df_res['event_cd']==3, 'stout_cum'] = 1
#    df_res['stout_cum'] = df_res['stout_cum'].cumsum()
#    
#    #�ŗ�
#    df_res['bat_ave_cum'] = round(df_res['hit_cum'] / df_res['ab_cum'], 3)
#    
#    #�o�ۗ�
#    df_res['on_base_cum'] = round(
#        (df_res['hit_cum'] + df_res['walk_cum'] + df_res['dead_cum']) / \
#        (df_res['ab_cum'] + df_res['walk_cum'] + df_res['dead_cum'] + df_res['sf_cum'])
#        , 3)
#    
#    #���ŗ�
#    df_res['slug_cum'] = round(df_res['base_hit_cum'] / df_res['ab_cum'], 3)
#    
#    #OPS
#    df_res['ops'] = df_res['on_base_cum'] + df_res['slug_cum']
#    
#    return df_res
#

def get_batting_results(df):
    #�i�ۃC�x���g������
    df_res = df[(df['bat_event_fl']=='T')]
    
    #�ŐȐ�
    
    #�Ő�
    df_res['ab_cum'] = df_res['ab_fl'].replace({'T': 1, 'F': 0})
    df_res['ab_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['ab_cum'].cumsum()
    
    #single
    df_res['single_cum'] = 0
    df_res.loc[df_res['h_cd']==1, 'single_cum'] = 1
    df_res['single_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['single_cum'].cumsum()
     
    #double
    df_res['double_cum'] = 0
    df_res.loc[df_res['h_cd']==2, 'double_cum'] = 1
    df_res['double_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['double_cum'].cumsum()
    
    #triple
    df_res['triple_cum'] = 0
    df_res.loc[df_res['h_cd']==3, 'triple_cum'] = 1
    df_res['triple_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['triple_cum'].cumsum()
    
    #homerun
    df_res['homerun_cum'] = 0
    df_res.loc[df_res['h_cd']==4, 'homerun_cum'] = 1
    df_res['homerun_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['homerun_cum'].cumsum()
    
    #���Ő�
    df_res['hit_cum'] = df_res['single_cum'] + df_res['double_cum'] + df_res['triple_cum'] + df_res['homerun_cum']
     
    #�ۑ�
    df_res['base_hit_cum'] = df_res['single_cum']*1 + df_res['double_cum']*2 + df_res['triple_cum']*3 + df_res['homerun_cum']*4
    
    #�œ_
    df_res['rbi_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['rbi_ct'].cumsum()
    
    #�l��
    df_res['walk_cum'] = 0
    df_res.loc[df_res['event_cd'].isin([14, 15]), 'walk_cum'] = 1
    df_res['walk_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['walk_cum'].cumsum()
    
    #����
    df_res['dead_cum'] = 0
    df_res.loc[df_res['event_cd'].isin([16]), 'dead_cum'] = 1
    df_res['dead_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['dead_cum'].cumsum()
    
    #�]��
    df_res['sf_cum'] = df_res['sf_fl'].replace({'T': 1, 'F': 0})
    df_res['sf_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['sf_cum'].cumsum()
    
    #�O�U
    df_res['stout_cum'] = 0
    df_res.loc[df_res['event_cd']==3, 'stout_cum'] = 1
    df_res['stout_cum'] = df_res.groupby(['bat_id', 'game_year'], as_index=False)['stout_cum'].cumsum()
    
    #�ŗ�
    df_res['bat_ave_cum'] = round(df_res['hit_cum'] / df_res['ab_cum'], 3)
    
    #�o�ۗ�
    df_res['on_base_cum'] = round(
        (df_res['hit_cum'] + df_res['walk_cum'] + df_res['dead_cum']) / \
        (df_res['ab_cum'] + df_res['walk_cum'] + df_res['dead_cum'] + df_res['sf_cum'])
        , 3)
    
    #���ŗ�
    df_res['slug_cum'] = round(df_res['base_hit_cum'] / df_res['ab_cum'], 3)
    
    #OPS
    df_res['ops'] = df_res['on_base_cum'] + df_res['slug_cum']
    
    return df_res


#���_���l�s��
def score_value_matrix(df):
    #�ŐȎ��_�ł̗��`�[���̓��_�̍��v
    df['runs'] = df['home_score_ct'] + df['away_score_ct']
    #�Q�[���~�C�j���O�~�\���ň�ӂ�ID
    df['half.inning'] = df['game_id'] + df['inn_ct'].astype(str) + df['bat_home_id'].astype(str)
    
    #���̑ŐȂœ��������_
    func = lambda x: 1 if x>3 else 0
    df['runs.scored'] = df['bat_dest_id'].apply(func) + df['run1_dest_id'].apply(func) + df['run2_dest_id'].apply(func) + df['run3_dest_id'].apply(func)
    
    #���̃C�j���O�œ��������_�A���̃C�j���O���_�̓��_
    half_innings = df.groupby('half.inning', as_index=False).agg({'event_outs_ct': 'sum', 'runs.scored': 'sum', 'runs': 'min'})
    half_innings.columns = ['half.inning', 'outs.inning', 'runs.inning', 'runs.start']
    half_innings['max.runs'] = half_innings['runs.inning'] + half_innings['runs.start']
    
    
    df = pd.merge(df, half_innings, on='half.inning')
    
    #���̃C�j���O�œ���c��̓��_
    df['runs.roi'] = df['max.runs'] - df['runs']
    
    #���̑ŐȎ��_�ł̃����i�[�~�A�E�g�J�E���g�̏�
    df['base1_run_id'] = df['base1_run_id'].astype(str)
    df['base2_run_id'] = df['base2_run_id'].astype(str)
    df['base3_run_id'] = df['base3_run_id'].astype(str)

    func = lambda x: '1' if x != 'nan' else '0'
    df['bases'] = df['base1_run_id'].apply(func) + df['base2_run_id'].apply(func) + df['base3_run_id'].apply(func)
    df['state'] = df['bases'] + df['outs_ct'].astype(str)

    #���̑ŐȏI�����_�ł̃����i�[�~�A�E�g�J�E���g�̏�
    df['nrunner1'] = ((df['bat_dest_id']==1) | (df['run1_dest_id']==1)).astype(int)
    df['nrunner2'] = ((df['bat_dest_id']==2) | (df['run1_dest_id']==2) | (df['run2_dest_id']==2)).astype(int)
    df['nrunner3'] = ((df['bat_dest_id']==3) | (df['run1_dest_id']==3) | (df['run2_dest_id']==3) | (df['run3_dest_id']==3)).astype(int)

    df['nouts'] = df['outs_ct'] + df['event_outs_ct']

    df['new.state'] = df['nrunner1'].astype(str) + df['nrunner2'].astype(str) + df['nrunner3'].astype(str) + df['nouts'].astype(str)

    #�����i�[�̏�Ԃɕω����������A�܂��͓��_�L�^���ꂽ�v���[�ɍi��
    df = df[(df['state']!=df['new.state']) | (df['runs.scored']>0)]

    #�A�E�g�J�E���g��3�̃v���[�ɍi��i�T���i���Ȃǂ������j
    dfC = df[df['outs.inning']==3]

    #
    runs = dfC.groupby('state', as_index=False)['runs.roi'].mean()
    runs.columns = ['state', 'Mean']
    
    runs_out = pd.pivot_table(dfC, values='runs.roi', index='bases', columns='outs_ct', aggfunc='mean')
    runs_out = round(runs_out, 2)
    runs_out.columns = ['0 outs', '1 outs', '2outs']
    runs_out

    #���݂̏�Ԃ̓��_���Ғl
    df = pd.merge(df, runs, on='state', how='left')
    df.rename(columns = {'Mean': 'runs.state'}, inplace=True)

    #�v���[��̓��_���Ғl
    df = pd.merge(df, runs, left_on='new.state', right_on='state', how='left')
    df.rename(columns = {'Mean': 'runs.new.state'}, inplace=True)

    df['runs.new.state'].fillna(0, inplace=True)

    #���_���l�i�v���[��̓��_���Ғl�@�|�@�v���[�O�̓��_���Ғl�@�{�@�v���[�ɂ���ē��������_
    df['run_value'] = df['runs.new.state'] - df['runs.state'] + df['runs.scored']

    #�s�v�ȗ�̍폜
    df.drop(['runs', 'half.inning', 'runs.scored', 'outs.inning',
       'runs.inning', 'runs.start', 'max.runs', 'runs.roi', 'bases',
       'nrunner1', 'nrunner2', 'nrunner3', 'nouts', 'runs.state',
       'state_y', 'runs.new.state'], axis=1, inplace=True)
    
    df.rename(columns={'state_x': 'state'}, inplace=True)

    return df