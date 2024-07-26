from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()
    # Set your local paths here.
    settings.art_path = ''
    settings.davis_dir = ''
    settings.got10k_lmdb_path = ''
    settings.got10k_path = ''
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = ''
    settings.lasot_extension_subset_path_path = ''
    settings.lasot_lmdb_path = ''
    settings.lasot_path = ''
    settings.network_path = ''    # Where tracking networks are stored.
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.prj_dir = '/dataW/yifan/Trackingcode/RGBDT_baseline/'
    settings.result_plot_path = ''
    settings.results_path = '/dataW/yifan/Trackingcode/RGBDT_baseline/results/rgbdt/new'    # Where to store tracking results
    settings.save_dir = '/dataW/yifan/Trackingcode/RGBDT_baseline/save'
    settings.segmentation_path = ''
    settings.tc128_path = ''
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = ''
    settings.tpl_path = ''
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.vot18_path = ''
    settings.vot22_path = ''
    settings.vot_path = ''
    settings.rgbdt_test_dir = '/dataZ/yifan/RGBDT500/Test_100'

    return settings

