Create schema db_log;
use db_log;

create table user_log_info1(
    User_ID int (10),
    user_IP varchar (150) NOT NULL, 
    browser varchar (255),
    dice_num int (75),
    dice_results varchar (85),
    sum_of_dice int (150)
);

select * from user_log_infol;