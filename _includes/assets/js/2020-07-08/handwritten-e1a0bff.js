// Built by Nick Jalbert
// Handwritten repo, commit e1a0bffa343a7747729aab1922006f33986dc18b


/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./src/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./src/index.js":
/*!**********************!*\
  !*** ./src/index.js ***!
  \**********************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }\n\nfunction _nonIterableSpread() { throw new TypeError(\"Invalid attempt to spread non-iterable instance.\\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.\"); }\n\nfunction _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === \"string\") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === \"Object\" && o.constructor) n = o.constructor.name; if (n === \"Map\" || n === \"Set\") return Array.from(o); if (n === \"Arguments\" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }\n\nfunction _iterableToArray(iter) { if (typeof Symbol !== \"undefined\" && Symbol.iterator in Object(iter)) return Array.from(iter); }\n\nfunction _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }\n\nfunction _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }\n\n// https://stackoverflow.com/a/36481059\n// Box-Muller transform that returns mean 0 and variance 1\nfunction randBoxMuller() {\n  var u = 0;\n  var v = 0;\n\n  while (u === 0) {\n    u = Math.random();\n  } // Converting [0,1) to (0,1)\n\n\n  while (v === 0) {\n    v = Math.random();\n  }\n\n  return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);\n}\n\nfunction getNormal(mean, stdev) {\n  return randBoxMuller() * stdev + mean;\n} // 7 x 5 grid:\n//\n// 0 1 2 3 4\n// 1\n// 2\n// 3\n// 4\n// 5\n// 6\n\n\nfunction getCanvas() {\n  var canvas = document.createElement('canvas');\n  canvas.height = 70;\n  canvas.width = 50;\n  canvas.stdev = 1;\n\n  canvas.getCoord = function (x, y) {\n    var canvasX = canvas.width * 0.2 * x + canvas.width * 0.05;\n    var canvasY = canvas.height * 0.14 * y + canvas.height * 0.05;\n    return [getNormal(canvasX, canvas.stdev), getNormal(canvasY, canvas.stdev)];\n  }; // canvas.style.border = '1px solid';\n\n\n  return canvas;\n}\n\nfunction getSloppyA() {\n  var canvas = getCanvas();\n  var context = canvas.getContext('2d');\n  context.lineWidth = 3;\n  context.beginPath();\n  context.moveTo.apply(context, _toConsumableArray(canvas.getCoord(2, 0)));\n  context.lineTo.apply(context, _toConsumableArray(canvas.getCoord(0, 6)));\n  context.moveTo.apply(context, _toConsumableArray(canvas.getCoord(2, 0)));\n  context.lineTo.apply(context, _toConsumableArray(canvas.getCoord(4, 6)));\n  context.moveTo.apply(context, _toConsumableArray(canvas.getCoord(1, 3)));\n  context.lineTo.apply(context, _toConsumableArray(canvas.getCoord(3, 3)));\n  context.stroke();\n  return canvas;\n}\n\nfunction getSloppyB() {\n  var canvas = getCanvas();\n  var context = canvas.getContext('2d');\n  var posX0 = canvas.width / 5 * 0 + 5;\n  var posX4 = canvas.width / 5 * 4 + 5;\n  var posY0 = canvas.height / 7 * 0 + 5;\n  var posY3 = canvas.height / 7 * 3 + 5;\n  var posY6 = canvas.height / 7 * 6 + 5;\n  context.lineWidth = 3;\n  context.beginPath();\n  context.moveTo(getNormal(posX0, 1), getNormal(posY0, 1));\n  context.lineTo(getNormal(posX0, 1), getNormal(posY6, 1));\n  context.moveTo(getNormal(posX0, 1), getNormal(posY0, 1));\n  context.bezierCurveTo(getNormal(posX4, 3), getNormal(posY0, 3), getNormal(posX4, 3), getNormal(posY3, 3), getNormal(posX0, 2), getNormal(posY3, 2));\n  context.bezierCurveTo(getNormal(posX4, 3), getNormal(posY3, 3), getNormal(posX4, 3), getNormal(posY6, 3), getNormal(posX0, 2), getNormal(posY6, 2));\n  context.stroke();\n  return canvas;\n}\n\nfunction getSloppyC() {\n  var canvas = getCanvas(); // TODO - how to handle kerning?\n\n  canvas.style.position = 'relative';\n  canvas.style.right = '12px';\n  var context = canvas.getContext('2d');\n  var posX0 = canvas.width / 5 * 0 + 5;\n  var posX4 = canvas.width / 5 * 4 + 5;\n  var posY0 = canvas.height / 7 * 0 + 5;\n  var posY6 = canvas.height / 7 * 6 + 5;\n  context.lineWidth = 3;\n  context.beginPath();\n  context.moveTo(getNormal(posX4, 2), getNormal(posY0, 2));\n  context.bezierCurveTo(getNormal(posX0 - 10, 4), getNormal(posY0, 4), getNormal(posX0 - 10, 4), getNormal(posY6, 4), getNormal(posX4, 2), getNormal(posY6, 2));\n  context.stroke();\n  return canvas;\n}\n\nfunction getSloppyD() {\n  var canvas = getCanvas();\n  var context = canvas.getContext('2d');\n  var posX0 = canvas.width / 5 * 0 + 5;\n  var posX4 = canvas.width / 5 * 4 + 5;\n  var posY0 = canvas.height / 7 * 0 + 5;\n  var posY6 = canvas.height / 7 * 6 + 5;\n  context.lineWidth = 3;\n  context.beginPath();\n  context.moveTo(getNormal(posX0, 1), getNormal(posY0, 1));\n  context.lineTo(getNormal(posX0, 1), getNormal(posY6, 1));\n  context.moveTo(getNormal(posX0, 1), getNormal(posY0, 1));\n  context.bezierCurveTo(getNormal(posX4, 5), getNormal(posY0, 5), getNormal(posX4, 5), getNormal(posY6, 5), getNormal(posX0, 2), getNormal(posY6, 2));\n  context.stroke();\n  return canvas;\n}\n\nfunction getSloppyE() {\n  var STDEV = 1;\n  var canvas = getCanvas();\n  var context = canvas.getContext('2d');\n  var posX0 = canvas.width / 5 * 0 + 5;\n  var posX4 = canvas.width / 5 * 4 + 5;\n  var posY0 = canvas.height / 7 * 0 + 5;\n  var posY3 = canvas.height / 7 * 3 + 5;\n  var posY6 = canvas.height / 7 * 6 + 5;\n  context.lineWidth = 3;\n  context.beginPath();\n  context.moveTo(getNormal(posX0, STDEV), getNormal(posY0, STDEV));\n  context.lineTo(getNormal(posX0, STDEV), getNormal(posY6, STDEV));\n  context.lineTo(getNormal(posX4, STDEV), getNormal(posY6, STDEV));\n  context.moveTo(getNormal(posX0, STDEV), getNormal(posY3, STDEV));\n  context.lineTo(getNormal(posX4, STDEV), getNormal(posY3, STDEV));\n  context.moveTo(getNormal(posX0, STDEV), getNormal(posY0, STDEV));\n  context.lineTo(getNormal(posX4, STDEV), getNormal(posY0, STDEV));\n  context.stroke();\n  return canvas;\n}\n\nfunction handwrite(el) {\n  var sloppyA = getSloppyA();\n  sloppyA.id = 'Sloppy-A';\n  el.appendChild(sloppyA);\n  var sloppyB = getSloppyB();\n  sloppyB.id = 'Sloppy-B';\n  el.appendChild(sloppyB);\n  var sloppyC = getSloppyC();\n  sloppyC.id = 'Sloppy-C';\n  el.appendChild(sloppyC);\n  var sloppyD = getSloppyD();\n  sloppyD.id = 'Sloppy-D';\n  el.appendChild(sloppyD);\n  var sloppyE = getSloppyE();\n  sloppyE.id = 'Sloppy-E';\n  el.appendChild(sloppyE);\n}\n\nfunction runHandwritten() {\n  var el = document.getElementById('handwritten-js');\n  handwrite(el);\n  var button = document.getElementById('rewrite-button');\n\n  button.onclick = function () {\n    el.innerHTML = '';\n    handwrite(el);\n  };\n} // http://youmightnotneedjquery.com/#ready\n\n\nfunction ready(fn) {\n  if (document.readyState !== 'loading') {\n    fn();\n  } else if (document.addEventListener) {\n    document.addEventListener('DOMContentLoaded', fn);\n  } else {\n    document.attachEvent('onreadystatechange', function () {\n      if (document.readyState !== 'loading') {\n        fn();\n      }\n    });\n  }\n}\n\nready(runHandwritten);\n\n//# sourceURL=webpack:///./src/index.js?");

/***/ })

/******/ });
