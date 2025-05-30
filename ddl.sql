CREATE TABLE `tb_account` (
  `account_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'key',
  `account_key` varchar(30) NOT NULL,
  `join_type` varchar(10) DEFAULT NULL COMMENT 'user, kakao, naver, google, apple',
  `sns_key` varchar(60) DEFAULT NULL COMMENT 'kakao, naver, google, apple key',
  `password` varchar(255) NOT NULL COMMENT '비밀번호',
  `user_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '이름',
  `phone` varchar(20) NOT NULL COMMENT '연락처',
  `language` varchar(12) DEFAULT NULL,
  `postcode` varchar(6) DEFAULT NULL COMMENT '우편번호',
  `address` varchar(60) DEFAULT NULL COMMENT '도로명주소',
  `address_region` varchar(60) DEFAULT NULL COMMENT '지번주소',
  `address_detail` varchar(60) DEFAULT NULL COMMENT '상세주소',
  `latitude` double DEFAULT NULL COMMENT '위도',
  `longitude` double DEFAULT NULL COMMENT '경도',
  `email` varchar(100) DEFAULT NULL COMMENT '이메일',
  `role` varchar(20) DEFAULT NULL COMMENT 'ROLE_ADMIN, ROLE_MANAGER, ROLE_USER, ROLE_TESTER, ROLE_PARTNER',
  `level` varchar(20) DEFAULT 'Normal' COMMENT '활동 등을 기반으로',
  `fcm_token` varchar(255) DEFAULT NULL COMMENT 'FCM token',
  `web_socket_key` varchar(120) DEFAULT NULL COMMENT 'web socket key',
  `refresh_token` varchar(140) DEFAULT NULL COMMENT 'refresh token',
  `use_fg` bit(1) DEFAULT b'1' COMMENT '사용 여부 : 1=사용, 0=삭제',
  `approved` bit(1) DEFAULT b'0' COMMENT '승인 여부 : 1=승인, 0=미승인',
  `created_at` datetime DEFAULT NULL COMMENT '가입/등록 일시',
  `updated_at` datetime DEFAULT NULL COMMENT '수정 일시',
  `login_at` datetime DEFAULT NULL COMMENT '최종 로그인 일시',
  `password_at` datetime DEFAULT NULL COMMENT '최종 비번 수정 일시',
  PRIMARY KEY (`account_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='계정';

CREATE TABLE `tb_board` (
  `board_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'key',
  `board_kind` varchar(20) NOT NULL DEFAULT 'notice' COMMENT 'notice , faq, clause_service 이용약관, clause_position 위치정보, policy_private 개인정보, policy_identity 고유정보, policy_health 건강정보',
  `writer_id` int(11) unsigned DEFAULT 0 COMMENT '작성자 key(account_id)',
  `title` varchar(90) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '제목',
  `contents` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '본문',
  `read_count` int(11) unsigned DEFAULT 0 COMMENT '조회수',
  `use_fg` bit(1) DEFAULT b'1' COMMENT '사용 여부 : 1=사용, 0=삭제',
  `created_at` datetime DEFAULT NULL COMMENT '등록 일시',
  `updated_at` datetime DEFAULT NULL COMMENT '수정 일시',
  PRIMARY KEY (`board_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `tb_code` (
  `code_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'key',
  `p_code` varchar(30) NOT NULL COMMENT '상위코드',
  `code` varchar(30) NOT NULL COMMENT '코드',
  `code_label` varchar(60) NOT NULL COMMENT '코드명칭',
  `memo` varchar(120) DEFAULT NULL COMMENT '메모',
  `str_val` varchar(255) DEFAULT NULL,
  `num_val` float DEFAULT NULL,
  `use_fg` bit(1) DEFAULT b'1' COMMENT '사용 여부 : 1=사용, 0=삭제',
  `edited_at` datetime DEFAULT NULL COMMENT '편집 일시',
  PRIMARY KEY (`code_id`) USING BTREE,
  UNIQUE KEY `UK_CODE_ID` (`p_code`,`code`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE `tb_file` (
  `file_id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'key',
  `link_info` varchar(30) NOT NULL DEFAULT 'none' COMMENT 'table_field',
  `link_key` int(11) unsigned NOT NULL DEFAULT 0 COMMENT '연결 key',
  `real_name` varchar(120) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '파일명',
  `file_url` varchar(120) NOT NULL,
  `file_size` int(11) unsigned DEFAULT 0 COMMENT '파일크기',
  `saved_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`file_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
