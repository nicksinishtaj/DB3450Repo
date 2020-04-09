-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema construction_company
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema construction_company
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `construction_company`;
CREATE SCHEMA IF NOT EXISTS `construction_company` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `construction_company` ;

-- -----------------------------------------------------
-- Table `construction_company`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC) VISIBLE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `construction_company`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`auth_group_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `construction_company`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `construction_company`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`auth_user_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC) VISIBLE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `construction_company`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `construction_company`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`auth_user_user_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `construction_company`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `construction_company`.`auth_user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`employee` (
  `EMPLOYEE_ID` INT NOT NULL AUTO_INCREMENT,
  `EMPLOYEE_NAME_FIRST` VARCHAR(45) NOT NULL,
  `EMPLOYEE_NAME_MIDDLE` VARCHAR(45) NULL DEFAULT NULL,
  `EMPLOYEE_NAME_LAST` VARCHAR(45) NOT NULL,
  `EMPLOYEE_TITLE` VARCHAR(45) NOT NULL,
  `EMPLOYEE_DOB` DATE NOT NULL,
  `EMPLOYEE_HIRE_DATE` DATE NOT NULL,
  `EMPLOYEE_EMAIL_WORK` VARCHAR(45) NOT NULL,
  `EMPLOYEE_EMAIL_ALT` VARCHAR(45) NULL DEFAULT NULL,
  `EMPLOYEE_TEL_WORK` CHAR(10) NOT NULL,
  `EMPLOYEE_TEL_ALT` CHAR(10) NULL DEFAULT NULL,
  `EMPLOYEE_MANAGER_ID` INT NULL DEFAULT NULL,
  `EMPLOYEE_PAY_RATE` FLOAT NOT NULL,
  `EMPLOYEE_END_DATE` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`EMPLOYEE_ID`),
  UNIQUE INDEX `employee_id_UNIQUE` (`EMPLOYEE_ID` ASC) VISIBLE,
  INDEX `fk_EMPLOYEE_EMPLOYEE1_idx` (`EMPLOYEE_MANAGER_ID` ASC) VISIBLE,
  CONSTRAINT `fk_EMPLOYEE_EMPLOYEE1`
    FOREIGN KEY (`EMPLOYEE_MANAGER_ID`)
    REFERENCES `construction_company`.`employee` (`EMPLOYEE_ID`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`customer_company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`customer_company` (
  `CUSTOMER_COMPANY_ID` INT NOT NULL AUTO_INCREMENT,
  `CUSTOMER_COMPANY_NAME` VARCHAR(45) NOT NULL,
  `CUSTOMER_COMPANY_STREET1` VARCHAR(45) NOT NULL,
  `CUSTOMER_COMPANY_STREET2` VARCHAR(45) NULL DEFAULT NULL,
  `CUSTOMER_COMPANY_CITY` VARCHAR(45) NOT NULL,
  `CUSTOMER_COMPANY_STATE` CHAR(2) NOT NULL,
  `CUSTOMER_COMPANY_ZIP` INT NOT NULL,
  `EMPLOYEE_ID` INT NOT NULL,
  PRIMARY KEY (`CUSTOMER_COMPANY_ID`),
  UNIQUE INDEX `CUSTOMER_ID_UNIQUE` (`CUSTOMER_COMPANY_ID` ASC) VISIBLE,
  INDEX `fk_CUSTOMER_EMPLOYEE1_idx` (`EMPLOYEE_ID` ASC) VISIBLE,
  CONSTRAINT `fk_CUSTOMER_EMPLOYEE1`
    FOREIGN KEY (`EMPLOYEE_ID`)
    REFERENCES `construction_company`.`employee` (`EMPLOYEE_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`customer_contact`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`customer_contact` (
  `CUSTOMER_CONTACT_ID` INT NOT NULL AUTO_INCREMENT,
  `CUSTOMER_ID` INT NOT NULL,
  `CUSTOMER_CONTACT_FNAME` VARCHAR(45) NOT NULL,
  `CUSTOMER_CONTACT_LNAME` VARCHAR(45) NOT NULL,
  `CUSTOMER_CONTACT_EMAIL` VARCHAR(45) NOT NULL,
  `CUSTOMER_CONTACT_TEL` CHAR(10) NOT NULL,
  `CUSTOMER_CONTACT_ROLE` VARCHAR(45) NOT NULL,
  `CUSTOMER_CONTACT_CURRENT` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`CUSTOMER_CONTACT_ID`),
  UNIQUE INDEX `CUSTOMER_CONTACT_ID_UNIQUE` (`CUSTOMER_CONTACT_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) VISIBLE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `construction_company`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `construction_company`.`auth_user` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`django_migrations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`employee_hours`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`employee_hours` (
  `EMPLOYEE_HOURS_ID` INT NOT NULL AUTO_INCREMENT,
  `EMPLOYEE_ID` INT NOT NULL,
  `PROJECT_ID` INT NULL DEFAULT NULL,
  `EMPLOYEE_HOURS_FIRST_DAY` DATE NOT NULL,
  `EMPLOYEE_HOURS_RATE` FLOAT NOT NULL,
  `EMPLOYEE_HOURS_SUN1` INT NOT NULL,
  `EMPLOYEE_HOURS_MON1` INT NOT NULL,
  `EMPLOYEE_HOURS_TUE1` INT NOT NULL,
  `EMPLOYEE_HOURS_WED1` INT NOT NULL,
  `EMPLOYEE_HOURS_THR1` INT NOT NULL,
  `EMPLOYEE_HOURS_FRI1` INT NOT NULL,
  `EMPLOYEE_HOURS_SAT1` INT NOT NULL,
  `EMPLOYEE_HOURS_SUN2` INT NOT NULL,
  `EMPLOYEE_HOURS_MON2` INT NOT NULL,
  `EMPLOYEE_HOURS_TUE2` INT NOT NULL,
  `EMPLOYEE_HOURS_WED2` INT NOT NULL,
  `EMPLOYEE_HOURS_THR2` INT NOT NULL,
  `EMPLOYEE_HOURS_FRI2` INT NOT NULL,
  `EMPLOYEE_HOURS_SAT2` INT NOT NULL,
  PRIMARY KEY (`EMPLOYEE_HOURS_ID`),
  UNIQUE INDEX `EMPLOYEE_HOURS_ID_UNIQUE` (`EMPLOYEE_HOURS_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`permission` (
  `PERMISSION_LEVEL` INT NOT NULL AUTO_INCREMENT,
  `PERMISSION_NAME` VARCHAR(30) NOT NULL,
  `PERMISSION_DESCRIPTION` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`PERMISSION_LEVEL`),
  UNIQUE INDEX `PERMISSION_LEVEL_UNIQUE` (`PERMISSION_LEVEL` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`project`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`project` (
  `PROJECT_ID` INT NOT NULL AUTO_INCREMENT,
  `PROJECT_STATUS` ENUM('PROSPECTIVE', 'PLANNING', 'CURRENT', 'COMPLETE') NOT NULL,
  `PROJECT_NAME` VARCHAR(45) NOT NULL,
  `PROJECT_BUDGET` DECIMAL(10,2) NOT NULL,
  `CUSTOMER_COMPANY_ID` INT NOT NULL,
  PRIMARY KEY (`PROJECT_ID`),
  UNIQUE INDEX `PROHECT_ID_UNIQUE` (`PROJECT_ID` ASC) VISIBLE,
  INDEX `CUSTOMER_ID_idx` (`CUSTOMER_COMPANY_ID` ASC) VISIBLE,
  CONSTRAINT `CUSTOMER_ID`
    FOREIGN KEY (`CUSTOMER_COMPANY_ID`)
    REFERENCES `construction_company`.`customer_company` (`CUSTOMER_COMPANY_ID`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`employee_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`employee_permission` (
  `EMPLOYEE_PERMISSION_ID` INT NOT NULL,
  `EMPLOYEE_ID` INT NOT NULL,
  `PERMISSION_LEVEL` INT NOT NULL,
  `PROJECT_ID` INT NULL DEFAULT NULL,
  `EMPLOYEE_PERMISSION_START` DATE NOT NULL,
  `EMPLOYEE_PERMISSION_END` DATE NULL DEFAULT NULL,
  PRIMARY KEY (`EMPLOYEE_PERMISSION_ID`),
  UNIQUE INDEX `EMPLOYEE_PERMISSION_ID_UNIQUE` (`EMPLOYEE_PERMISSION_ID` ASC) VISIBLE,
  INDEX `EMPLOYEE_ID_idx` (`EMPLOYEE_ID` ASC) VISIBLE,
  INDEX `PERMISSION_LEVEL_idx` (`PERMISSION_LEVEL` ASC) VISIBLE,
  INDEX `PROJECT_ID` (`PROJECT_ID` ASC) VISIBLE,
  CONSTRAINT `EMPLOYEE_ID`
    FOREIGN KEY (`EMPLOYEE_ID`)
    REFERENCES `construction_company`.`employee` (`EMPLOYEE_ID`),
  CONSTRAINT `PERMISSION_LEVEL`
    FOREIGN KEY (`PERMISSION_LEVEL`)
    REFERENCES `construction_company`.`permission` (`PERMISSION_LEVEL`),
  CONSTRAINT `PROJECT_ID`
    FOREIGN KEY (`PROJECT_ID`)
    REFERENCES `construction_company`.`project` (`PROJECT_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`inventory` (
  `INVENTORY_ID` INT NOT NULL AUTO_INCREMENT,
  `INVENTORY_NAME` VARCHAR(45) NOT NULL,
  `INVENTORY_DESCRIPTION` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`INVENTORY_ID`),
  UNIQUE INDEX `PRODUCT_ID_UNIQUE` (`INVENTORY_ID` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`supplier_company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`supplier_company` (
  `SUPPLIER_COMPANY_ID` INT NOT NULL AUTO_INCREMENT,
  `SUPPLIER_COMPANY_NAME` VARCHAR(45) NOT NULL,
  `SUPPLIER_COMPANY_STREET1` VARCHAR(45) NOT NULL,
  `SUPPLIER_COMPANY_STREET2` VARCHAR(45) NULL DEFAULT NULL,
  `SUPPLIER_COMPANY_CITY` VARCHAR(45) NOT NULL,
  `SUPPLIER_COMPANY_STATE` CHAR(2) NOT NULL,
  `SUPPLIER_COMPANY_ZIP` INT NOT NULL,
  `SUPPLIER_COMPANY_NOTES` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`SUPPLIER_COMPANY_ID`),
  UNIQUE INDEX `CUSTOMER_ID_UNIQUE` (`SUPPLIER_COMPANY_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`inventory_supplier`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`inventory_supplier` (
  `INVENTORY_ID` INT NOT NULL,
  `SUPPLIER_ID` INT NOT NULL,
  `INVENTORY_SUPPLIER_COST` DECIMAL(10,2) NOT NULL,
  `INVENTORY_SUPPLIER_AMOUNT` INT NOT NULL,
  `INVENTORY_SUPPLIER_NOTES` VARCHAR(255) NULL DEFAULT NULL,
  `INVENTORY_SUPPLIER_PREFERRED` TINYINT(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`INVENTORY_ID`, `SUPPLIER_ID`),
  INDEX `SUPPLIER_ID_idx` (`SUPPLIER_ID` ASC) VISIBLE,
  CONSTRAINT `SUPPLIER_ID`
    FOREIGN KEY (`SUPPLIER_ID`)
    REFERENCES `construction_company`.`supplier_company` (`SUPPLIER_COMPANY_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`project_inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`project_inventory` (
  `INVENTORY_ID` INT NOT NULL,
  `QUANTITY` INT NOT NULL DEFAULT '0',
  `PROJECT_ID` INT NOT NULL,
  PRIMARY KEY (`INVENTORY_ID`, `PROJECT_ID`),
  UNIQUE INDEX `project_id_UNIQUE` (`PROJECT_ID` ASC) VISIBLE,
  UNIQUE INDEX `product_id_UNIQUE` (`INVENTORY_ID` ASC) VISIBLE,
  CONSTRAINT `INVENTORY_ID`
    FOREIGN KEY (`INVENTORY_ID`)
    REFERENCES `construction_company`.`inventory` (`INVENTORY_ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`purchase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`purchase` (
  `PURCHASE_ID` INT NOT NULL AUTO_INCREMENT,
  `PROJECT_ID` INT NOT NULL,
  `INVENTORY_ID` INT NOT NULL,
  `PURCHASE_QUANTITY` INT NOT NULL,
  `PURCHASE_TOTAL` DECIMAL(10,2) NOT NULL,
  `PURCHASE_DATE` DATE NOT NULL,
  `EMPLOYEE_ID` INT NOT NULL,
  PRIMARY KEY (`PURCHASE_ID`),
  UNIQUE INDEX `TRANSACTION_ID_UNIQUE` (`PURCHASE_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `construction_company`.`supplier_contact`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `construction_company`.`supplier_contact` (
  `SUPPLIER_CONTACT_ID` INT NOT NULL,
  `SUPPLIER_ID` INT NOT NULL,
  `SUPPLIER_CONTACT_FNAME` VARCHAR(45) NOT NULL,
  `SUPPLIER_CONTACT_LNAME` VARCHAR(45) NOT NULL,
  `SUPPLIER_CONTACT_EMAIL` VARCHAR(45) NOT NULL,
  `SUPPLIER_CONTACT_TEL` CHAR(10) NOT NULL,
  `SUPPLIER_CONTACT_ROLE` VARCHAR(45) NOT NULL,
  `SUPPLIER_CONTACT_CURRENT` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`SUPPLIER_CONTACT_ID`),
  UNIQUE INDEX `SUPPLIER_CONTACT_ID_UNIQUE` (`SUPPLIER_CONTACT_ID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;