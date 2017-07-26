# mysql
DROP TABLE IF EXISTS `interface_mock`;
CREATE TABLE `interface_mock` (
  `id` int(4) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL COMMENT 'rule名',
  `domain` varchar(100) NOT NULL COMMENT '域名',
  `uri` varchar(100) NOT NULL COMMENT 'uri',
  `parms` mediumtext COMMENT '参数',
  `method` char(10) NOT NULL DEFAULT 'GET' COMMENT '请求方法：post或get',
  `expect` mediumtext COMMENT '期望值',
  `http_status` char(10) NOT NULL DEFAULT '200' COMMENT 'http返回值，默认为200',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '0为失效；1为生效',
  `comment` varchar(128) DEFAULT 'none',
  `last_updatetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

BEGIN;
    INSERT INTO `interface_mock` VALUES ('1', 'GET TEST', 'a.daling.com', '/api/home/getFitting', 'a=b&c=d&e=f', 'GET', '{\"message\":\"Goods 379240 not found\",\"status\":140001}', '200', '1', 'none', '2016-12-02 19:57:20'), ('2', 'POST TEST', 'a.daling.com ', '/api/home/getFitting', 'loadGuess=no&page=1', 'POST', 'aaaa', '200', '1', 'none', '2016-12-02 19:59:52');
COMMIT;