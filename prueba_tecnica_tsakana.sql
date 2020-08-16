-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 15-08-2020 a las 18:40:21
-- Versión del servidor: 5.7.31
-- Versión de PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `prueba_tecnica_tsakana`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `cedula` int(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `direccion` varchar(255) NOT NULL,
  `telefono` varchar(255) NOT NULL,
  PRIMARY KEY (`cedula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`cedula`, `nombre`, `direccion`, `telefono`) VALUES
(66902888, 'carlos sanchez', 'cra 10 c # 10 sur 53', '3113211097'),
(123325236, 'francelly florez', 'cra 10 c # 10 sur 53', '3125888670'),
(1234189374, 'juan fernandez', 'cra 10 c # 10 sur 53', '3104288857');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturas`
--

DROP TABLE IF EXISTS `facturas`;
CREATE TABLE IF NOT EXISTS `facturas` (
  `codigo` int(255) NOT NULL AUTO_INCREMENT,
  `cliente` varchar(255) NOT NULL,
  `productos` varchar(255) NOT NULL,
  `cantidad` int(255) NOT NULL,
  `fecha` varchar(255) NOT NULL,
  `total` float NOT NULL,
  `metodo_pago` varchar(255) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `facturas`
--

INSERT INTO `facturas` (`codigo`, `cliente`, `productos`, `cantidad`, `fecha`, `total`, `metodo_pago`) VALUES
(1, 'juan fernandez', 'correa, pantalón, camiseta, pantaloneta', 4, '14/08/2020', 2000000, 'tarjeta de credito'),
(2, 'francelly florez', 'correa, pantalón, camiseta, pantaloneta, percha', 5, '15/08/2020', 10000, 'efectivo'),
(3, 'carlos fernandez', 'correa, pantalon, camiseta, reloj, zapatillas, chaleco, camisa', 7, '15/08/2020', 50000000, 'tarjeta de credito');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

DROP TABLE IF EXISTS `productos`;
CREATE TABLE IF NOT EXISTS `productos` (
  `codigo` int(255) NOT NULL AUTO_INCREMENT,
  `categoria` varchar(255) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `precio` float NOT NULL,
  `cantidad` int(255) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`codigo`, `categoria`, `nombre`, `precio`, `cantidad`, `estado`) VALUES
(8, 'niños', 'camiseta', 20000, 11, 1),
(9, 'caballero', 'pantalon ', 30000, 3, 1),
(19, 'adulto mayor', 'pañal', 12000, 2, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
