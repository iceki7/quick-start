--zxc  sql语句都是作用于一个db，因为可能会有联合多张表查询的时候


SHOW INDEX FROM tab;
---yd   key_name相同的是联合索引
drop index on tab;




CREATE DATABASE test_db;
USE test_db;




CREATE TABLE tb_users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    temp INT,
    
    -- 全文索引
    FULLTEXT (description)  
    
);




CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES tb_users(id) ON DELETE CASCADE
    --zxc  外键。如果没有对应的user_id，无法引用，也就无法插入
    -- 如果删除了tb_user中的那一项，这张表也会同步更新
);


INSERT INTO orders (user_id, total_amount) VALUES 
(1, 100.50),  -- 张三的订单
(2, 250.00),  -- 李四的订单
(1, 75.00);   -- 张三的另一个订单



-- yd 列聚合 from在group by之前
SELECT user_id as iop, sum(total_amount) AS qwe
FROM orders where user_id>1
GROUP BY user_id;



SELECT o.id AS order_id, u.name AS user_name, o.total_amount, o.order_date
FROM orders o
JOIN tb_users u ON o.user_id = u.id      -- zxc
WHERE u.name = '张三';





SELECT * FROM tb_user ORDER BY username LIMIT 10000, 7;
---yd   先order by，然后再取。
---深分页：会从0一直找到10000，所以慢。另一方面还需要回表。
---1、为了避免回表：可以先只查ID，然后根据ID去查主键索引（也就是只有这7条的主键索引）
SELECT * FROM tb_user WHERE id in (上面的sql);
或者
SELECT * FROM tb_user INNER JOIN (xxx) temp_tb
ON tb_user.id=temp_tb.id;


---2 使用覆盖索引（=避免回表）

    -- 如果要查所有的列，可以先只查一部分索引列，然后再构建一个子查询。


---3 使用 标记分页：通过保存上一次查询中，最后一个记录的ID


-- mysql深分页
-- https://blog.csdn.net/2401_85373732/article/details/145061201
-- 用索引排序


------------------------------------------------------------------------------


SELECT * FROM tb_user
LEFT JOIN tb_order ON A.id = B.id;
-- 返回左表（A）所有的记录，如果右表中缺失了这条记录，就填充NULL。
-- Inner join：只返回两个表中都匹配的记录。





-----------------------------------------------------------------------------------------


CREATE TABLE `cms_subject` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `category_id` bigint(20) DEFAULT NULL,
    `title` varchar(100) DEFAULT NULL,
    `pic` varchar(500) DEFAULT NULL COMMENT '专题主图',
    `product_count` int(11) DEFAULT NULL COMMENT '关联产品数量',
    `recommend_status` int(1) DEFAULT NULL,
    `create_time` datetime DEFAULT NULL,
    
    email VARCHAR(100) UNIQUE, 
    -- 唯一索引

    first_name VARCHAR(50),
    last_name VARCHAR(50),

    `comment_count` int(11) DEFAULT NULL,
    `album_pics` varchar(1000) DEFAULT NULL COMMENT '画册图片用逗号分割',
    `description` varchar(1000) DEFAULT NULL,
    `show_status` int(1) DEFAULT NULL COMMENT '显示状态：0->不显示；1->显示',
    `content` text,
    `forward_count` int(11) DEFAULT NULL COMMENT '转发数',
    `category_name` varchar(200) DEFAULT NULL COMMENT '专题分类名称',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='专题表';


CREATE UNIQUE INDEX idx_unique_email ON employees (email); 
-- 创建唯一索引

CREATE FULLTEXT INDEX idx_fulltext_first_name ON employees (first_name);
--- 全文索引


SELECT * FROM employees WHERE MATCH(description) AGAINST('database');
--- 全文索引
--- yd 它必须是一个完整的词语，用空格分隔



CREATE INDEX idx_fullname ON tb_users (first_name, last_name);
--- 组合索引


SELECT balance FROM account WHERE userid=123 FOR UPDATE;
-- 行锁。其他访问这一行的事务就会被阻塞

UPDATE account SET balance=balance+100.0 WHERE userid=123;

update table0 set count=count+1, version=version+1 where version=#{version}








--但如果分页就是用b+树的索引，它就会很快。用主键。




CREATE INDEX id_age ON tb_user(age);
-- 非聚簇索引


INSERT INTO usertab (id, name, email)
VALUES (1, 'John Doe', 'john.doe@example.com')
ON DUPLICATE KEY UPDATE
name = VALUES(name),
email = VALUES(email);
-- yd 插入，如果存在，就更新


----------------------------------------------------------------------------------------

START TRANSACTION;

-- 锁定账户A和账户B，-- 加行锁
SELECT balance FROM tb_accounts WHERE account_id = 1 FOR UPDATE;
SELECT balance FROM tb_accounts WHERE account_id = 2 FOR UPDATE;

-- 检查余额并执行转账
DECLARE a_balance DECIMAL(10, 2);
DECLARE b_balance DECIMAL(10, 2);


-- yd
SET a_balance = (SELECT balance FROM tb_accounts WHERE account_id = 1);
SET b_balance = (SELECT balance FROM tb_accounts WHERE account_id = 2);

-- yd
IF a_balance >= 100 THEN
    UPDATE tb_accounts SET balance = balance - 100 WHERE account_id = 1;
    UPDATE tb_accounts SET balance = balance + 100 WHERE account_id = 2;
ELSE
    -- 回滚事务
    ROLLBACK;
    -- 或者处理余额不足的情况
END IF;


SAVEPOINT sp1;
-- zxc mysql事务不能嵌套，但是可以用这个

ROLLBACK TO sp1;

COMMIT;


--------------------------------------------------------------------
-- 间隙锁

START TRANSACTION;
SELECT * FROM orders WHERE amount BETWEEN 100 AND 200 FOR UPDATE;
-- zxc 这样即使其他事务插入一个 amount = 150 的记录也会被阻塞
COMMIT;


-----------------------------------------------------------------------

-- yd 
-- u是简写，from里面要列出来它是什么
-- 先join了，再select
-- 逗号
SELECT 
    u.user_id, 
    u.username,
    COUNT(o.order_id) AS order_count
    -- zxc
FROM 
    bigdata_users u
LEFT JOIN 
    bigdata_order o ON u.user_id = o.user_id
GROUP BY 
    u.user_id;


---------------------------------------------------------------------

SELECT * FROM articles
WHERE content LIKE '%My%';
