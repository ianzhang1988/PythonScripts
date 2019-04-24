class Config:
    WORK_TYPE_COMMON        =1
    WORK_TYPE_SHORT         =2

    VALUE = {
        #####################job config######################
        # 'work_type': Config.WORK_TYPE_COMMON,
        'work_type': WORK_TYPE_COMMON,
        #####################mysql config######################
        'db_name' : None,
        'db_host' : None,
        'db_port' : None,
        'db_user' : None,
        'db_pass' : None,
        #####################log config########################
        'log_level' : None,
        'log_path' : None,
        #####################url config########################
        'master_url' : None,
        'vrs_url' : None,
        'vrs_rcv_url' : None,
        'ugc_rcv_url' : None,
        #####################default value config########################
        'default_worker_num' : None,
        'num_per_page' : None,
        #####################gearman config###################
        'gear_servers' : None,
        #####################master config######################
        #####################zookeeper config###################
        'zookeeper_servers' : None,
    }

print (Config.VALUE['work_type'])
