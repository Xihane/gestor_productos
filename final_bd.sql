-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema final_bd
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema final_bd
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `final_bd` DEFAULT CHARACTER SET utf8 ;
USE `final_bd` ;

-- -----------------------------------------------------
-- Table `final_bd`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`categoria` (
  `id_categoria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_categoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final_bd`.`producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`producto` (
  `id_producto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `precio` FLOAT NULL,
  `stock` INT NULL,
  `estado` INT NULL,
  `id_categoria` INT NOT NULL,
  PRIMARY KEY (`id_producto`, `id_categoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final_bd`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`cliente` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `telefono` INT NULL,
  `direccion` VARCHAR(45) NULL,
  `fecha_registro` DATE NULL,
  `estado` VARCHAR(45) NULL,
  PRIMARY KEY (`id_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final_bd`.`pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`pedido` (
  `id_pedido` INT NOT NULL AUTO_INCREMENT,
  `fecha_pedido` DATE NULL,
  `total` FLOAT NULL,
  `estado` VARCHAR(45) NULL,
  `cliente_id_cliente` INT NOT NULL,
  PRIMARY KEY (`id_pedido`, `cliente_id_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final_bd`.`metodo_pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`metodo_pago` (
  `id_metodopago` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  PRIMARY KEY (`id_metodopago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final_bd`.`detalle_pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`detalle_pedido` (
  `id_detalle_pedido` INT NOT NULL AUTO_INCREMENT,
  `id_pedido` INT NOT NULL,
  `id_producto` INT NOT NULL,
  `cantidad` INT NULL,
  `precio_unidad` INT NULL,
  `id_metodopago` INT NOT NULL,
  PRIMARY KEY (`id_detalle_pedido`, `id_pedido`, `id_producto`, `id_metodopago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final_bd`.`envio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `final_bd`.`envio` (
  `id_envio` INT NOT NULL AUTO_INCREMENT,
  `id_pedido` INT NOT NULL,
  `direccion_envio` VARCHAR(45) NULL,
  PRIMARY KEY (`id_envio`, `id_pedido`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
