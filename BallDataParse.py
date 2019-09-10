class BallDataParse:
    @classmethod
    def getObbs(cls,value):
        win_p = value['had']['h'] if "had" in value else 0.00
        flat_p = value['had']['d']if "had" in value else 0.00
        lose_p = value['had']['a']if "had" in value else 0.00
        let_win_p = value['hhad']['h']
        let_flat_p = value['hhad']['d']
        let_lose_p = value['hhad']['a']
        hh_p = value['hafu']['hh']
        hd_p = value['hafu']['hd']
        ha_p = value['hafu']['ha']
        dh_p = value['hafu']['dh']
        dd_p = value['hafu']['dd']
        da_p = value['hafu']['da']
        ah_p = value['hafu']['ah']
        ad_p = value['hafu']['ad']
        aa_p = value['hafu']['aa']
        s0_p = value['ttg']['s0']
        s1_p = value['ttg']['s1']
        s2_p = value['ttg']['s2']
        s3_p = value['ttg']['s3']
        s4_p = value['ttg']['s4']
        s5_p = value['ttg']['s5']
        s6_p = value['ttg']['s6']
        s7_p = value['ttg']['s7']

        s_1_0_p = value['crs']['0100']
        s_2_0_p = value['crs']['0200']
        s_3_0_p = value['crs']['0300']
        s_4_0_p = value['crs']['0400']
        s_5_0_p = value['crs']['0500']
        s_2_1_p = value['crs']['0201']
        s_3_2_p = value['crs']['0302']
        s_3_1_p = value['crs']['0301']
        s_4_1_p = value['crs']['0401']
        s_4_2_p = value['crs']['0402']
        s_5_1_p = value['crs']['0501']
        s_5_2_p = value['crs']['0502']
        s_3_p = value['crs']['-1-h']
        s_0_0_p = value['crs']['0000']
        s_1_1_p = value['crs']['0101']
        s_2_2_p = value['crs']['0202']
        s_3_3_p = value['crs']['0303']
        s_1_p = value['crs']['-1-d']
        s_0_1_p = value['crs']['0001']
        s_0_2_p = value['crs']['0002']
        s_0_3_p = value['crs']['0003']
        s_0_4_p = value['crs']['0004']
        s_0_5_p = value['crs']['0005']
        s_1_2_p = value['crs']['0102']
        s_1_3_p = value['crs']['0103']
        s_2_3_p = value['crs']['0203']
        s_1_4_p = value['crs']['0104']
        s_2_4_p = value['crs']['0204']
        s_1_5_p = value['crs']['0105']
        s_2_5_p = value['crs']['0205']
        s_0_p = value['crs']['-1-a']
        key=value['id']

        replace_data = (
        key, win_p, flat_p, lose_p, let_win_p, let_flat_p, let_lose_p, hh_p, hd_p, ha_p, dh_p, dd_p, da_p, ah_p, ad_p,
        aa_p,
        s0_p, s1_p, s2_p, s3_p, s4_p, s5_p, s6_p, s7_p, s_1_0_p, s_2_0_p, s_3_0_p, s_4_0_p, s_5_0_p, s_2_1_p, s_3_2_p,
        s_3_1_p, s_4_1_p, s_4_2_p, s_5_1_p, s_5_2_p, s_3_p, s_0_0_p, s_1_1_p, s_2_2_p, s_3_3_p, s_1_p, s_0_1_p, s_0_2_p,
        s_0_3_p, s_0_4_p, s_0_5_p, s_1_2_p, s_1_3_p, s_2_3_p, s_1_4_p, s_2_4_p, s_1_5_p, s_2_5_p, s_0_p)
        print(replace_data)
        return """insert into match_option_odds(match_key,win_p,flat_p,lose_p,let_win_p,let_flat_p,let_lose_p,hh_p,hd_p,ha_p,dh_p,dd_p,da_p,ah_p,ad_p,aa_p,
        s0_p,s1_p,s2_p,s3_p,s4_p,s5_p,s6_p,s7_p,s_1_0_p,s_2_0_p,s_3_0_p,s_4_0_p,s_5_0_p,s_2_1_p,s_3_2_p,
        s_3_1_p,s_4_1_p,s_4_2_p,s_5_1_p,s_5_2_p,s_3_p,s_0_0_p,s_1_1_p,s_2_2_p,s_3_3_p,s_1_p,s_0_1_p,s_0_2_p,
        s_0_3_p,s_0_4_p,s_0_5_p,s_1_2_p,s_1_3_p,s_2_3_p,s_1_4_p,s_2_4_p,s_1_5_p,s_2_5_p,s_0_p)
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
        '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
        '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % replace_data



    @classmethod
    def getMatch(self,value):
        date=value['date']+' '+value['time']
        weekday= value['b_date']
        number = value['num']
        match = value['l_cn']
        weather=value['weather']+' '+value['temperature']
        home_order = value['h_order']
        away_order = value['a_order']
        home_t=value['h_cn']
        away_t=value['a_cn']
        lets=value['hhad']['fixedodds']
        key=value['id']
        replace_data = (date, weekday, number, match, weather, home_order, away_order, home_t,away_t,lets,key)
        print(replace_data)
        return """insert into today_match(bdate,weekday,num,matcher,weather,home_order,away_order, home_t,away_t,lets,keyer)
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % replace_data



