CREATE TABLE IF NOT EXISTS `order` (
    order_id INT AUTO_INCREMENT NOT NULL,
    goods_id INT NOT NULL,
    user_mail varchar(20) NOT NULL,
    status char(10) NOT NULL, 
    good_count INT NOT NULL,
    amount FLOAT NOT NULL,
    create_time datetime NOT NULL,
    update_time datetime NOT NULL,
    PRIMARY KEY (`order_id`)
);

CREATE TABLE IF NOT EXISTS `user` (
    user_mail varchar(20) NOT NULL,
    city varchar(20) NOT NULL,
    sex char(10) NOT NULL
);


INSERT INTO `user` VALUES("barry.xu@163.com","shanghai","man");
INSERT INTO `user` VALUES("dandan@qq.com","shanghai","female");
INSERT INTO `user` VALUES("pony@qq.com","shengzhen","man");
INSERT INTO `user` VALUES("focus@qq.com","beijing","female");

CREATE TABLE IF NOT EXISTS `goods` (
    goods_id INT,
    sku varchar(20) NOT NULL,
    spu  varchar(20) NOT NULL
);

INSERT INTO `goods` VALUES(0,"boy shirt","shirt");
INSERT INTO `goods` VALUES(1,"girl shirt","shirt");
INSERT INTO `goods` VALUES(2,"boy shoes","shoes");
INSERT INTO `goods` VALUES(3,"girl shoes","shirt");
INSERT INTO `goods` VALUES(4,"boy pants","pants");
INSERT INTO `goods` VALUES(5,"girl pants","pants");
INSERT INTO `goods` VALUES(6,"boy coat","coat");
INSERT INTO `goods` VALUES(7,"girl coat","coat");
INSERT INTO `goods` VALUES(8,"girl skirt","skirt");


CREATE TABLE `vip` (
    user_mail varchar(20) NOT NULL,
    vip_name varchar(20) NOT NULL,
    vip_level INT NOT NULL,
    update_time datetime NOT NULL,
    PRIMARY KEY (`user_mail`)
);

INSERT INTO `vip` VALUES("barry.xu@163.com","普通用户",0,NOW());
INSERT INTO `vip` VALUES("dandan@qq.com","普通用户",0,NOW());
INSERT INTO `vip` VALUES("pony@qq.com","普通用户",0,NOW());
INSERT INTO `vip` VALUES("focus@qq.com","普通用户",0,NOW());