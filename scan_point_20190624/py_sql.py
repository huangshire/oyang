# coding=utf-8
import pymssql,_mssql,decimal
import encryption_test
import time

class SQLServer:   
    def __init__(self,server,user,password,database):
    # 类的构造函数，初始化DBC连接信息
        self.server = server
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
    # 得到数据库连接信息，返回conn.cursor()
        if not self.database:
            raise(NameError,"没有设置数据库信息")
        try:
            self.conn = pymssql.connect(server=self.server,user=self.user,password=self.password,database=self.database,timeout=5,autocommit = True)
            cur = self.conn.cursor()
        except Exception as e:
            print(e)
            print("登录错误！")

        
        if not cur:
            raise(NameError,"连接数据库失败")  # 将DBC信息赋值给cur
        else:
            return cur
             
    def ExecQuery(self,sql):
        '''
        执行查询语句
        返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # 执行查询语句
        try:
            result = cur.fetchall() # fetchall()获取查询结果
        except Exception as e:
            print(e)
            # 查询完毕关闭数据库连接
            pass
        self.conn.close()
        if result is not None:
            return result
        else:
            return 0
    # def Execute(self,sql):
    #     '''
    #     '''
    #     cur = self.__GetConnect()
    #     try:
    #         cur.execute(sql) # 执行语句
    #     except Exception as e:
    #         print(e)
    #         # 查询完毕关闭数据库连接
    #         pass
    #     self.conn.close()
    #     print('complete!')

def load_login_info():
    
    temp=encryption_test.read_file('infomation.zlj')
    infobuff=temp.split('\n')
    return infobuff[0],infobuff[1],infobuff[2],infobuff[3]
    
def main(temp):
    server,user,password,database=load_login_info()
    #print(server,'\n',user,'\n',password,'\n',database)
    msg = SQLServer(server,user,password,database)
    sql_line="""SET NOCOUNT ON DECLARE @sql1 nvarchar(1000),@sql2 nvarchar(1000),@nh VARCHAR(100),@bh VARCHAR(100),@dd VARCHAR(100),@bmh VARCHAR(100),@bmh1 VARCHAR(100),@bhsx VARCHAR(100),@xjsj VARCHAR(100),@table VARCHAR(50),@dwmc VARCHAR(50),@dflag VARCHAR(50),@bj VARCHAR(50),@khzt VARCHAR(50),@xjys VARCHAR(50),@ry VARCHAR(50)
            SET @nh='{}'
            SET @xjsj='{}'
            SET @bh='{}'
            SET @dflag='1'
            SET @bj='正式上传'
            SET @khzt='准时'
            SET @xjys='{}'
            SET @ry=''
            SELECT @dd=address_name, @bmh=bmh FROM[address] WHERE address_cardID = @nh
            SELECT @bhsx=bhsx, @bmh1=bmh FROM[lwbhsz] WHERE bh = @bh
            select @dwmc=LEFT(@bmh,4)
            select @table=dwmc from[lwbm] where bmh = @dwmc
            set @sql1='INSERT INTO [' + @table+'_LWmain] (nh,dd,xjsj,bh,bhsx,bmh,dflag,bj) values(@nh,@dd,@xjsj,@bh,@bhsx, @bmh,@dflag,@bj)'
            exec sp_executesql @sql1,N'@nh VARCHAR(50),@dd VARCHAR(50),@xjsj VARCHAR(50),@bh VARCHAR(50),@bhsx VARCHAR(50), @bmh VARCHAR(50),@dflag VARCHAR(50),@bj VARCHAR(50)', @nh,@dd,@xjsj,@bh,@bhsx, @bmh,@dflag,@bj
            set @sql2='UPDATE [' + @table+'_lwjhkh] SET ry = @ry, khzt = @khzt, xjsj =@xjsj,bhsx = @bhsx,bh = @bh,xjys = @xjys WHERE  dd =@dd AND @xjsj1>kssj AND @xjsj2<jssj'
            exec sp_executesql @sql2,N'@ry VARCHAR(50),@khzt VARCHAR(50),@xjsj VARCHAR(50),@bhsx VARCHAR(50),@bh VARCHAR(50), @xjys VARCHAR(50),@dd VARCHAR(50),@xjsj1 VARCHAR(50),@xjsj2 VARCHAR(50)', @ry,@khzt,@xjsj,@bhsx,@bh, @xjys,@dd,@xjsj,@xjsj
            SELECT TOP 100 * FROM [石油化工厂_lwjhkh] WHERE dd=@dd and xjsj='{}'""".format(temp[0],temp[1],temp[2],temp[3],temp[1],)
    
    result=msg.ExecQuery(sql_line)
    #time.sleep()
    #print('数据库链接！运行完成！')
    for i in result:
        print(i)
def sql_query(temp):
    server,user,password,database=load_login_info()
    # print(server,'\n',user,'\n',password,'\n',database)
    msg = SQLServer(server,user,password,database)
    sql_bmh_table="""SET NOCOUNT ON DECLARE @sqlselect nvarchar(1000),@nh VARCHAR(100),@bh VARCHAR(100),@bmh VARCHAR(100),@bmh1 VARCHAR(100),@bhsx VARCHAR(100),@table VARCHAR(50),@dwmc VARCHAR(50)\
            SET @nh='{}'
            SELECT @bmh=bmh FROM[address] WHERE address_cardID = @nh
            SELECT @dwmc=LEFT(@bmh,4)
            SELECT @table=dwmc from[lwbm] where bmh = @dwmc
            select @bmh,@table
            """.format(temp[0],)
    result=msg.ExecQuery(sql_bmh_table)
    # print(result[0][0],result[0][1])
    sql_query_info="""SELECT * from [{}_lwjhkh] WHERE kssj='{}' and bmh={}""".format(result[0][1],temp[1],result[0][0])
    result_query=msg.ExecQuery(sql_query_info)
    # print(result_query)
    for i in result_query:
        print(i[0:8])
        if i[3] == '准时':
            return True
            # break
        else:
            return False
        # break
if __name__ == '__main__':
    temp=['000006C64606', '2019-04-09 06:45:00', '4100', 0]
    # main(temp)
    sql_query(temp)

    #load_login_info()
