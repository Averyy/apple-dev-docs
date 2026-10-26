# cmHLS32Space

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

An HLS color space composed of hue, lightness, and saturation components whose values are packed with 10 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.

**Availability**:
- macOS 10.0+

## Declaration

```c
cmHLS32Space = cmHLSSpace + cmLong10ColorPacking
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmhls32space)*