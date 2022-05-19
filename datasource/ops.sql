 select * from `order`  where order_id =347;
 update `order` set user_mail = "barry.xu@163.com",status="paid" where order_id =347;
 INSERT INTO `order` ( user_mail,goods_id,status,good_count,amount,create_time,update_time ) VALUES( 'pony@qq.com',5,'unpaid',1,505.0,'2022-05-17 11:15:34','2022-05-17 11:15:34' )