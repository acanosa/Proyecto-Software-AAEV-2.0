-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema aaev2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema aaev2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `aaev2` DEFAULT CHARACTER SET utf8 ;
USE `aaev2` ;

-- -----------------------------------------------------
-- Table `aaev2`.`Carrera`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Carrera` (
  `idCarrera` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidadAnios` INT NOT NULL,
  PRIMARY KEY (`idCarrera`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Login`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Login` (
  `idLogin` INT NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `clave` VARCHAR(45) NOT NULL,
  `privilegio` INT NOT NULL,
  `activo` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idLogin`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Docente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Docente` (
  `idDocente` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `dni` INT NOT NULL,
  `idLogin` INT NOT NULL,
  PRIMARY KEY (`idDocente`, `idLogin`),
  INDEX `fk_Docente_Login1_idx` (`idLogin` ASC),
  CONSTRAINT `fk_Docente_Login1`
    FOREIGN KEY (`idLogin`)
    REFERENCES `aaev2`.`Login` (`idLogin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Alumno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Alumno` (
  `idAlumno` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `dni` MEDIUMTEXT NOT NULL,
  `idLogin` INT NOT NULL,
  PRIMARY KEY (`idAlumno`, `idLogin`),
  INDEX `fk_Alumno_Login1_idx` (`idLogin` ASC),
  CONSTRAINT `fk_Alumno_Login1`
    FOREIGN KEY (`idLogin`)
    REFERENCES `aaev2`.`Login` (`idLogin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Materia` (
  `idMateria` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `anioCarrera` INT NOT NULL,
  PRIMARY KEY (`idMateria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Examen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Examen` (
  `idExamen` INT NOT NULL AUTO_INCREMENT,
  `totalPreguntas` INT NOT NULL,
  `totalPuntos` FLOAT NOT NULL,
  `descripcion` TEXT NULL,
  `tiempoLimite` TIME NOT NULL,
  `fechaCierre` DATE NOT NULL,
  `visible` TINYINT(1) NOT NULL DEFAULT 0,
  `idMateria` INT NOT NULL,
  PRIMARY KEY (`idExamen`, `idMateria`),
  INDEX `fk_Examen_Materia1_idx` (`idMateria` ASC),
  CONSTRAINT `fk_Examen_Materia1`
    FOREIGN KEY (`idMateria`)
    REFERENCES `aaev2`.`Materia` (`idMateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`tipoPregunta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`tipoPregunta` (
  `idTipoPregunta` INT NOT NULL AUTO_INCREMENT,
  `nombreTipo` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idTipoPregunta`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Unidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Unidad` (
  `idUnidad` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `idMateria` INT NOT NULL,
  PRIMARY KEY (`idUnidad`, `idMateria`),
  INDEX `fk_Unidad_Materia1_idx` (`idMateria` ASC),
  CONSTRAINT `fk_Unidad_Materia1`
    FOREIGN KEY (`idMateria`)
    REFERENCES `aaev2`.`Materia` (`idMateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Pregunta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Pregunta` (
  `idPregunta` INT NOT NULL AUTO_INCREMENT,
  `texto` VARCHAR(45) NOT NULL,
  `idTipoPregunta` INT NOT NULL,
  `idUnidad` INT NOT NULL,
  PRIMARY KEY (`idPregunta`, `idTipoPregunta`, `idUnidad`),
  INDEX `fk_Pregunta_tipoPregunta1_idx` (`idTipoPregunta` ASC),
  INDEX `fk_Pregunta_Unidad1_idx` (`idUnidad` ASC),
  CONSTRAINT `fk_Pregunta_tipoPregunta1`
    FOREIGN KEY (`idTipoPregunta`)
    REFERENCES `aaev2`.`tipoPregunta` (`idTipoPregunta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pregunta_Unidad1`
    FOREIGN KEY (`idUnidad`)
    REFERENCES `aaev2`.`Unidad` (`idUnidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Respuesta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Respuesta` (
  `idOpcion` INT NOT NULL AUTO_INCREMENT,
  `texto` VARCHAR(45) NOT NULL,
  `correcta` TINYINT(1) NOT NULL DEFAULT 0,
  `imagen` VARCHAR(400) NULL,
  `descripcionImagen` VARCHAR(45) NULL,
  `idOpcion_correcta` INT NULL,
  `idPregunta` INT NOT NULL,
  PRIMARY KEY (`idOpcion`, `idPregunta`),
  INDEX `fk_Opcion_Pregunta_idx` (`idPregunta` ASC),
  INDEX `fk_Opcion_Opcion1_idx` (`idOpcion_correcta` ASC),
  CONSTRAINT `fk_Opcion_Pregunta`
    FOREIGN KEY (`idPregunta`)
    REFERENCES `aaev2`.`Pregunta` (`idPregunta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Opcion_Opcion1`
    FOREIGN KEY (`idOpcion_correcta`)
    REFERENCES `aaev2`.`Respuesta` (`idOpcion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Docente_has_Materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Docente_has_Materia` (
  `idDocente` INT NOT NULL,
  `idMateria` INT NOT NULL,
  PRIMARY KEY (`idDocente`, `idMateria`),
  INDEX `fk_Docente_has_Materia_Materia1_idx` (`idMateria` ASC),
  INDEX `fk_Docente_has_Materia_Docente1_idx` (`idDocente` ASC),
  CONSTRAINT `fk_Docente_has_Materia_Docente1`
    FOREIGN KEY (`idDocente`)
    REFERENCES `aaev2`.`Docente` (`idDocente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Docente_has_Materia_Materia1`
    FOREIGN KEY (`idMateria`)
    REFERENCES `aaev2`.`Materia` (`idMateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Alumno_has_Materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Alumno_has_Materia` (
  `idAlumno` INT NOT NULL,
  `idMateria` INT NOT NULL,
  `habilitado` TINYINT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`idAlumno`, `idMateria`),
  INDEX `fk_Alumno_has_Materia_Materia1_idx` (`idMateria` ASC),
  INDEX `fk_Alumno_has_Materia_Alumno1_idx` (`idAlumno` ASC),
  CONSTRAINT `fk_Alumno_has_Materia_Alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `aaev2`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Alumno_has_Materia_Materia1`
    FOREIGN KEY (`idMateria`)
    REFERENCES `aaev2`.`Materia` (`idMateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Examen_has_Alumno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Examen_has_Alumno` (
  `idExamen` INT NOT NULL,
  `idAlumno` INT NOT NULL,
  `nota` FLOAT NOT NULL,
  `nroIntentos` INT NOT NULL,
  `estado` VARCHAR(45) NOT NULL DEFAULT 'Sin realizar',
  PRIMARY KEY (`idExamen`, `idAlumno`),
  INDEX `fk_Examen_has_Alumno_Alumno1_idx` (`idAlumno` ASC),
  INDEX `fk_Examen_has_Alumno_Examen1_idx` (`idExamen` ASC),
  CONSTRAINT `fk_Examen_has_Alumno_Examen1`
    FOREIGN KEY (`idExamen`)
    REFERENCES `aaev2`.`Examen` (`idExamen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Examen_has_Alumno_Alumno1`
    FOREIGN KEY (`idAlumno`)
    REFERENCES `aaev2`.`Alumno` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Universidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Universidad` (
  `idUniversidad` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NOT NULL,
  `dominioMail` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUniversidad`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Solicitud_Registro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Solicitud_Registro` (
  `idSolicitud_Registro` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `dni` INT NOT NULL,
  `solicitud` TEXT NULL,
  PRIMARY KEY (`idSolicitud_Registro`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Universidad_has_Carrera`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Universidad_has_Carrera` (
  `Universidad_idUniversidad` INT NOT NULL,
  `Carrera_idCarrera` INT NOT NULL,
  `Materia_idMateria` INT NOT NULL,
  PRIMARY KEY (`Universidad_idUniversidad`, `Carrera_idCarrera`, `Materia_idMateria`),
  INDEX `fk_Universidad_has_Carrera_Carrera1_idx` (`Carrera_idCarrera` ASC),
  INDEX `fk_Universidad_has_Carrera_Universidad1_idx` (`Universidad_idUniversidad` ASC),
  INDEX `fk_Universidad_has_Carrera_Materia1_idx` (`Materia_idMateria` ASC),
  CONSTRAINT `fk_Universidad_has_Carrera_Universidad1`
    FOREIGN KEY (`Universidad_idUniversidad`)
    REFERENCES `aaev2`.`Universidad` (`idUniversidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Universidad_has_Carrera_Carrera1`
    FOREIGN KEY (`Carrera_idCarrera`)
    REFERENCES `aaev2`.`Carrera` (`idCarrera`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Universidad_has_Carrera_Materia1`
    FOREIGN KEY (`Materia_idMateria`)
    REFERENCES `aaev2`.`Materia` (`idMateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Unidad_has_Examen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Unidad_has_Examen` (
  `Examen_idExamen` INT NOT NULL,
  `Unidad_idUnidad` INT NOT NULL,
  `tipoPregunta_idTipoPregunta` INT NOT NULL,
  `cantPreguntas` INT NOT NULL,
  PRIMARY KEY (`Examen_idExamen`, `Unidad_idUnidad`, `tipoPregunta_idTipoPregunta`),
  INDEX `fk_Unidad_has_Examen_Examen1_idx` (`Examen_idExamen` ASC),
  INDEX `fk_Unidad_has_Examen_Unidad1_idx` (`Unidad_idUnidad` ASC),
  INDEX `fk_Unidad_has_Examen_tipoPregunta1_idx` (`tipoPregunta_idTipoPregunta` ASC),
  CONSTRAINT `fk_Unidad_has_Examen_Unidad1`
    FOREIGN KEY (`Unidad_idUnidad`)
    REFERENCES `aaev2`.`Unidad` (`idUnidad`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Unidad_has_Examen_Examen1`
    FOREIGN KEY (`Examen_idExamen`)
    REFERENCES `aaev2`.`Examen` (`idExamen`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Unidad_has_Examen_tipoPregunta1`
    FOREIGN KEY (`tipoPregunta_idTipoPregunta`)
    REFERENCES `aaev2`.`tipoPregunta` (`idTipoPregunta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `aaev2`.`Solicitud_materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `aaev2`.`Solicitud_materia` (
  `idSolicitud_materia` INT NOT NULL AUTO_INCREMENT,
  `Materia_idMateria` INT NULL,
  `Docente_idDocente` INT NOT NULL,
  `fecha` DATE NOT NULL,
  `mensaje` TEXT NULL,
  PRIMARY KEY (`idSolicitud_materia`),
  INDEX `fk_Solicitud_materia_Materia1_idx` (`Materia_idMateria` ASC),
  INDEX `fk_Solicitud_materia_Docente1_idx` (`Docente_idDocente` ASC),
  CONSTRAINT `fk_Solicitud_materia_Materia1`
    FOREIGN KEY (`Materia_idMateria`)
    REFERENCES `aaev2`.`Materia` (`idMateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Solicitud_materia_Docente1`
    FOREIGN KEY (`Docente_idDocente`)
    REFERENCES `aaev2`.`Docente` (`idDocente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
