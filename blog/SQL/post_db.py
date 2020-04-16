'''
Created on 2020. 3. 10.

@author: user
'''
import cx_Oracle
import os

class Post_List():
    os.putenv('NLS_LANG', '.UTF8')
    
    con = cx_Oracle.connect('ksis/dbkinacksis@211.199.110.237:50301/kinacorcl') 
    
    cur = con.cursor()
    
    cur.execute("SELECT MBA_CD FROM T_KC_MBA_ADMN")
    
    for MBA_CD in cur:
        print(f"MBA_CD : /{MBA_CD}/")
        print("MBA_CD : /{}/".format(MBA_CD))  
    '''
    SELECT MBA_CD
           , '[' || MBA_CD || '] ' || MBA_NM AS MBA_NM
           , FACL_CD
           , MBA_SHOT_NM
        FROM T_KC_MBA_ADMN
       WHERE USE_YN = 'Y'
         AND CURR_REPT_STAT = '1'
    ORDER BY UP_CD
           , MBA_TYP
           , MBA_CD 
    '''
    
    cur.close()
    con.close()

    return 
