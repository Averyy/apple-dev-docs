# cmLUV32Space

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

An L*u*v* color space composed of L*, u*, and v* components whose values are packed with 10 bits per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.

**Availability**:
- macOS 10.0+

## Declaration

```c
cmLUV32Space = cmLUVSpace + cmLong10ColorPacking
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmluv32space)*