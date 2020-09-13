import pandas as pd
import requests
import datetime 
import json
import xmltodict
import html
import urllib

#EMES
cookie='JSESSIONID=p6qrrcgvRwoX2J_N5AI1WWkD6AP9y-oGtuPGwQup.svw-c2sn02001; isc_cState=ready; EMES_SSO=NTRhZWI5ZTktNGFkYS00Y2U4LTkxN2EtMzc2ZDA0MGE0NzBl'
message_logbook_url = "http://172.30.1.95/webgui.alarm.war/EMES/sc/IDACall?isc_rpc=1&isc_v=v9.1p_2015-02-24&isc_xhr=1"
formdata_msglog="isc_tnum=25&_transaction=%3Ctransaction%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2F10%2FXMLSchema-instance%22%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CtransactionNum%20xsi%3Atype%3D%22xsd%3Along%22%3E25%3C%2FtransactionNum%3E%3Coperations%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Coperator%3Eand%3C%2Foperator%3E%3C_constructor%3EAdvancedCriteria%3C%2F_constructor%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ETSBEGIN%3C%2FfieldName%3E%3Coperator%3EgreaterOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-08-18T16%3A00%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ETSBEGIN%3C%2FfieldName%3E%3Coperator%3ElessOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-08-28T15%3A59%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ETEXT%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3Einvalid%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EMESSAGEGROUP%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3EFM%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EPLC%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3ELF2911%3C%2Felem%3E%3Celem%3ELF3912%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EFUNCTIONGROUP%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3ERB320%3C%2Fvalue%3E%3C%2Felem%3E%3C%2Fcriteria%3E%3C%2Fcriteria%3E%3CoperationConfig%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CdataSource%3Ealarm_all%3C%2FdataSource%3E%3Crepo%20xsi%3Anil%3D%22true%22%2F%3E%3CoperationType%3Efetch%3C%2FoperationType%3E%3CtextMatchStyle%3Esubstring%3C%2FtextMatchStyle%3E%3C%2FoperationConfig%3E%3CstartRow%20xsi%3Atype%3D%22xsd%3Along%22%3E0%3C%2FstartRow%3E%3CendRow%20xsi%3Atype%3D%22xsd%3Along%22%3E75%3C%2FendRow%3E%3CsortBy%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3E-TSBEGIN%3C%2Felem%3E%3C%2FsortBy%3E%3CcomponentId%3EALARM_HISTORY_ListGrid%3C%2FcomponentId%3E%3CappID%3EbuiltinApplication%3C%2FappID%3E%3Coperation%3Eref%3Aalarm_all_fetch%3C%2Foperation%3E%3ColdValues%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Coperator%3Eand%3C%2Foperator%3E%3C_constructor%3EAdvancedCriteria%3C%2F_constructor%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ETSBEGIN%3C%2FfieldName%3E%3Coperator%3EgreaterOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-08-18T16%3A00%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ETSBEGIN%3C%2FfieldName%3E%3Coperator%3ElessOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-08-28T15%3A59%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ETEXT%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3Einvalid%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EMESSAGEGROUP%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3EFM%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EPLC%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3ELF2911%3C%2Felem%3E%3Celem%3ELF3912%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EFUNCTIONGROUP%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3ERB320%3C%2Fvalue%3E%3C%2Felem%3E%3C%2Fcriteria%3E%3C%2FoldValues%3E%3C%2Felem%3E%3C%2Foperations%3E%3C%2Ftransaction%3E&protocolVersion=1.0"

bodytracking_url="http://172.30.1.95/webgui.amf.war/EMES/sc/IDACall?isc_rpc=1&isc_v=v9.1p_2015-02-24&isc_xhr=1"
formdata_bodytrack="isc_tnum=9&_transaction=%3Ctransaction%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2F10%2FXMLSchema-instance%22%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CtransactionNum%20xsi%3Atype%3D%22xsd%3Along%22%3E9%3C%2FtransactionNum%3E%3Coperations%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Coperator%3Eand%3C%2Foperator%3E%3C_constructor%3EAdvancedCriteria%3C%2F_constructor%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3EgreaterOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-09-08T02%3A00%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3ElessOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-09-12T15%3A59%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EBODY_EXTID%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3E782020*%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EPLCIN%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3E112010%3C%2Felem%3E%3Celem%3E112360%3C%2Felem%3E%3Celem%3E112400%3C%2Felem%3E%3Celem%3E125001%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3C%2Fcriteria%3E%3C%2Fcriteria%3E%3CoperationConfig%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CdataSource%3Ebts_history%3C%2FdataSource%3E%3Crepo%20xsi%3Anil%3D%22true%22%2F%3E%3CoperationType%3Efetch%3C%2FoperationType%3E%3CtextMatchStyle%3Eexact%3C%2FtextMatchStyle%3E%3C%2FoperationConfig%3E%3CstartRow%20xsi%3Atype%3D%22xsd%3Along%22%3E0%3C%2FstartRow%3E%3CendRow%20xsi%3Atype%3D%22xsd%3Along%22%3E75%3C%2FendRow%3E%3CsortBy%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3E-CREATED%3C%2Felem%3E%3C%2FsortBy%3E%3CcomponentId%3EAMF_BTS_HISTORY_ListGrid%3C%2FcomponentId%3E%3CappID%3EbuiltinApplication%3C%2FappID%3E%3Coperation%3Eref%3Abts_history_fetch%3C%2Foperation%3E%3ColdValues%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Coperator%3Eand%3C%2Foperator%3E%3C_constructor%3EAdvancedCriteria%3C%2F_constructor%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3EgreaterOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-09-08T02%3A00%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3ElessOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-09-12T15%3A59%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EBODY_EXTID%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3E782020*%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EPLCIN%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3E112010%3C%2Felem%3E%3Celem%3E112360%3C%2Felem%3E%3Celem%3E112400%3C%2Felem%3E%3Celem%3E125001%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3C%2Fcriteria%3E%3C%2FoldValues%3E%3C%2Felem%3E%3C%2Foperations%3E%3C%2Ftransaction%3E&protocolVersion=1.0"


paintlog_url="http://172.30.1.95/webgui.amf.war/EMES/sc/IDACall?isc_rpc=1&isc_v=v9.1p_2015-02-24&isc_xhr=1"
formdata_paintlog="isc_tnum=25&_transaction=%3Ctransaction%20xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2F10%2FXMLSchema-instance%22%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CtransactionNum%20xsi%3Atype%3D%22xsd%3Along%22%3E25%3C%2FtransactionNum%3E%3Coperations%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Coperator%3Eand%3C%2Foperator%3E%3C_constructor%3EAdvancedCriteria%3C%2F_constructor%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EBODY_EXTID%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3E78202093616224%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EMDS_CURRENT_LOCATION_TEXT%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3EHandover%20to%20E-Shuttle%20PT%20-%20type%20check%3C%2Felem%3E%3Celem%3EMessage%20point%20processing%20result%20ED%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3EgreaterOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-08-24T16%3A00%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3ElessOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-09-08T15%3A59%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3C%2Fcriteria%3E%3C%2Fcriteria%3E%3CoperationConfig%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CdataSource%3Eamf_bts_paint_log_book%3C%2FdataSource%3E%3Crepo%20xsi%3Anil%3D%22true%22%2F%3E%3CoperationType%3Efetch%3C%2FoperationType%3E%3CtextMatchStyle%3Eexact%3C%2FtextMatchStyle%3E%3C%2FoperationConfig%3E%3CstartRow%20xsi%3Atype%3D%22xsd%3Along%22%3E0%3C%2FstartRow%3E%3CendRow%20xsi%3Atype%3D%22xsd%3Along%22%3E75%3C%2FendRow%3E%3CsortBy%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3ECREATED%3C%2Felem%3E%3C%2FsortBy%3E%3CappID%3EbuiltinApplication%3C%2FappID%3E%3Coperation%3Eamf_bts_paint_log_book_fetch%3C%2Foperation%3E%3ColdValues%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3Coperator%3Eand%3C%2Foperator%3E%3C_constructor%3EAdvancedCriteria%3C%2F_constructor%3E%3Ccriteria%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EBODY_EXTID%3C%2FfieldName%3E%3Coperator%3EiContainsPattern%3C%2Foperator%3E%3Cvalue%3E78202093616224%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3EMDS_CURRENT_LOCATION_TEXT%3C%2FfieldName%3E%3Coperator%3EinSet%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3AList%22%3E%3Celem%3EHandover%20to%20E-Shuttle%20PT%20-%20type%20check%3C%2Felem%3E%3Celem%3EMessage%20point%20processing%20result%20ED%3C%2Felem%3E%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3EgreaterOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-08-24T16%3A00%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3Celem%20xsi%3Atype%3D%22xsd%3AObject%22%3E%3CfieldName%3ECREATED%3C%2FfieldName%3E%3Coperator%3ElessOrEqual%3C%2Foperator%3E%3Cvalue%20xsi%3Atype%3D%22xsd%3Adatetime%22%3E2020-09-08T15%3A59%3A00.000%3C%2Fvalue%3E%3C%2Felem%3E%3C%2Fcriteria%3E%3C%2FoldValues%3E%3C%2Felem%3E%3C%2Foperations%3E%3C%2Ftransaction%3E&protocolVersion=1.0"

def Getdata(url,formdata):
    headers={
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,de-DE;q=0.6,de;q=0.5,en-AU;q=0.4',
        'Connection': 'keep-alive',
        'Content-Length': '3537',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'172.30.1.95',
        'Origin': 'http://172.30.1.95',
        'Referer': 'http://172.30.1.95/webgui.alarm.war/?startup=ALARM_HISTORY&profile=1707633&locale=en_US',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    }
#     requestdata=formdata_clean(formdata)
    requestdata= formdata
    cookies=coo_regular(cookie)
    print(cookies)
    res=requests.post(url,headers=headers,cookies=cookies,data=requestdata) #,params={'search_text':'python','cat':'1001'} 
    return res
def formdata_clean(formdata):
    requestJSONdata=formdata
    requestJSONdata=str(requestJSONdata).replace("+", "%2B")
    requestdata=requestJSONdata.encode("utf-8")
    return requestdata
def coo_regular(cookie):
    coo={}
    for item in cookie.split(';'):
        k,v=item.split('=',1)
        coo[k.strip()]=v.replace('"','')
    return coo
def xml_to_dict(xml):
    return eval(json.dumps(xmltodict.parse(xml)))
def dict_to_xml(dic):
    return xmltodict.unparse(dic).split("\n")[1]
def str_to_xml(s):#url to xml
    return urllib.parse.unquote_plus(s, encoding='utf-8')#, errors='replace'
def xml_to_str(xml):
#     print(type(xml.encode(encoding = "utf-8")))
    return xml.encode(encoding = "utf-8")
def parse(res):
    """解析返回数据"""
    def date(val):
        return datetime.datetime.fromtimestamp(val/1000)
    if res.status_code==200:
        try:
            data = res.text.split("-->")[1].split("//")[0]
        except:
            print("爬取不成功，请检查cookies或网络状态！")
        data = (data.replace('{','dict(').replace('}',')').replace(':','=')
             .replace('false','False').replace('true','True').replace('new Date','date'))
        data = eval(data)
        print(f"此次返回{len(data[0]['data'])}条数据，共{data[0]['totalRows']}条数据")
        return data
def crawl_rest(data):#还需要完善优化
    if len(data[0]['data']) < data[0]['totalRows']:#为爬取所有
        for i in range(1,data[0]['totalRows'] // 75):
            start_end_rows = [str(i*75),str((i+1)*75)]
        
            

# Message logbook模块
def modify_messagelog_params(transaction,begin_start=None,begin_end=None,text=None,PLC=None,FunctionGroup=None,start_end_rows=[]):
    a=transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]
    dic={}
    for k,v in zip(["begin_start","begin_end","text","MESSAGEGROUP","PLC","FunctionGroup"],a):
        dic[k] = v
    del dic["MESSAGEGROUP"]    
    try:
        if begin_start:
            # 解决8小时时区偏差
            begin_start = (datetime.datetime.strptime(begin_start,"%Y-%m-%dT%H:%M:%S.000")- datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.000")
            dic["begin_start"]['value']['#text']=begin_start
        else:
            del dic["begin_start"]
        if begin_end:
            begin_end = (datetime.datetime.strptime(begin_end,"%Y-%m-%dT%H:%M:%S.000")- datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.000")
            dic["begin_end"]['value']['#text']=begin_end
        else:
            del dic["begin_end"]
        if text:
            dic["text"]['value']=text
        else:
            del dic["text"]
        if PLC:
            if len(PLC)>=2:
                dic["PLC"]['value']['elem']=PLC
            else:
                dic["PLC"]['value']=PLC
        else:
            del dic["PLC"]
        if FunctionGroup:
            dic["FunctionGroup"]['value']=FunctionGroup
        else:
            del dic["FunctionGroup"]
        transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]=list(dic.values())
        if start_end_rows:
            transaction['transaction']['operations']["elem"]['startRow']["#text"] = start_end_rows[0]
            transaction['transaction']['operations']["elem"]['startRow']["#text"] = start_end_rows[1]
    except:
        print("Parameters not found, modify fail!")
    return xml_to_str(dict_to_xml(transaction))  
def message_logbook_crawl():
    begin_start='2020-08-08T00:00:00.000'
    begin_end='2020-08-21T23:59:00.000'
    text = 'invalid free'
    PLC = ["LF2911","LF3912"]#可根据需要添加
    FunctionGroup = "RB320"#只能写1个

    transaction = xml_to_dict(str_to_xml(formdata_msglog.split("&")[1]).split("=",1)[1])
    data = modify_messagelog_params(transaction,begin_start=begin_start,begin_end=begin_end,text=text,PLC=None,FunctionGroup=None,start_end_rows=['75','150'])#根据参数需求调用
    form_data={
        'isc_tnum': 25,#好像这个值无所谓
        '_transaction': data,
        'protocolVersion': '1.0'
    }
    res=Getdata(message_logbook_url,form_data)
    data = parse(res)
    # print(data)

# Body tracking模块
def get_bodytracking_info_byPIN(transaction,PIN=None):
    '''获取指定FIS号的车身过点信息'''
    a = transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]
    a.pop(0)
    a.pop(0)
    a.pop()
    a[0]['value']=PIN
    return xml_to_str(dict_to_xml(transaction))
def modify_bodytracking_params(transaction,Date_begin=None,Date_end=None,PIN=None,Location=None):
    """四个参数可以任意选择"""
    a=transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]
    b={}
    for k,v in zip(["Date_begin","Date_end","PIN","Location"],a):
        b[k]=v
    try:
        if Date_begin and a[0]["fieldName"]== 'CREATED' and a[0]["operator"]== 'greaterOrEqual':
            Date_begin = (datetime.datetime.strptime(Date_begin,"%Y-%m-%dT%H:%M:%S.000")- datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.000")
            b["Date_begin"]['value']['#text']=Date_begin
        else:
            del b["Date_begin"]
        if Date_end and a[1]["fieldName"]== 'CREATED' and a[1]["operator"]== 'lessOrEqual':
            Date_begin = (datetime.datetime.strptime(Date_end,"%Y-%m-%dT%H:%M:%S.000")- datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.000")
            b["Date_end"]['value']['#text']=Date_end
        else:
            del b["Date_end"]
        if PIN and a[2]["fieldName"]== 'BODY_EXTID' and a[2]["operator"]== 'iContainsPattern':
            b["PIN"]['value']=PIN
        else:
            del b["PIN"]
        if Location and a[3]["fieldName"]== 'PLCIN' and a[3]["operator"]== 'inSet':
            if len(Location) >=2:
                a[3]['value']['elem']=Location
            else:
                a[3]['value']=Location
        else:
            del b["Location"]
        transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]=list(b.values())    
    except:
        print("Parameters not found, modify fail!")
    return xml_to_str(dict_to_xml(transaction))
def body_tracking_crawl():
    date_begin = '2020-09-08T00:00:00.000'
    date_end = '2020-09-08T23:59:00.000'
    PIN = "78202093616224"#78202092811897
    Location = ['112360', "112010"]#可以是1个或多个
    transaction = xml_to_dict(str_to_xml(formdata_bodytrack.split("&")[1]).split("=",1)[1])
    transaction = modify_bodytracking_params(transaction,Date_begin=date_begin,Date_end=date_end,Location=Location)#PIN=PIN,
    # transaction=get_bodytracking_info_byPIN(transaction,PIN = PIN)#,Location=Location
    form_data={
        'isc_tnum': 9,#不确定用途，好像这个值无所谓
        '_transaction': transaction,
        'protocolVersion': '1.0'
    }
    res=Getdata(bodytracking_url,form_data)
    data = parse(res)
    # print(data)

# Paint log 模块
def get_paintlog_byPIN(transaction,PIN=None,Location=None):
    '''获取指定FIS号的车身过点信息'''
    a = transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]
    a.pop()
    a.pop()
    if not Location:
        a.pop()
        a[0]['value']=PIN
    else:
        a[0]['value']=PIN
        a[1]['value']['elem']=Location
    print(a)
    return xml_to_str(dict_to_xml(transaction))
def modify_paintlog_params(transaction,PIN=None,Location=None,Start=None,End=None):
    a=transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]
    b = {}
    for k,v in zip(["PIN","Location","Start","End"],a):
        b[k]=v
    try:
        if PIN and a[0]["fieldName"]== 'BODY_EXTID' and a[0]["operator"]== 'iContainsPattern':
            b["PIN"]['value']=PIN
        else:
            del b["PIN"]
        if Location and a[1]["fieldName"]== 'MDS_CURRENT_LOCATION_TEXT' and a[1]["operator"]== 'inSet':
            if len(Location)==1:
                b["Location"]['value']=Location
            else:
                b["Location"]['value']['elem']=Location
        else:
            del b["Location"]
        if Start:
            b["Start"]['value']['#text']=Start
        else:
            del b["Start"]
        if End:
            b["End"]['value']['#text']=End
        else:
            del b["End"]
        transaction['transaction']['operations']["elem"]["criteria"]["criteria"]["elem"]=list(b.values())
    except:
        print("Parameters not found, modify fail!")
    return xml_to_str(dict_to_xml(transaction))
def paint_log_crawl():
    BODY_EXTID = '78202093616224'#""78202092811897
    Location = ['244001 - Message point processing result pre- paint Robots line 1','Message point processing result ED']#可以为1个或多个
    Start = '2020-09-08T00:00:00.000'
    End = '2020-09-10T00:00:00.000'
    transaction = xml_to_dict(str_to_xml(formdata_paintlog.split("&")[1]).split("=",1)[1])
    transaction=modify_paintlog_params(transaction,Location=Location,Start=Start,End=End)
    # transaction=get_paintlog_byPIN(transaction,PIN=BODY_EXTID,Location=Location)#按Fis和Location爬取信息
    form_data={
        'isc_tnum': 25,#不确定用途，好像这个值无所谓
        '_transaction': transaction,
        'protocolVersion': '1.0'
    }
    res=Getdata(paintlog_url,form_data)
    data = parse(res)
    # print(data)
if __name__ == "__main__":
    message_logbook_crawl()
    # body_tracking_crawl()
    # paint_log_crawl()