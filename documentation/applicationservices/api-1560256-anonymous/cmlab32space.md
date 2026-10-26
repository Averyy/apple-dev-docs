# cmLAB32Space

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
cmLAB32Space = cmLABSpace + cmLong10ColorPacking
```

#### Discussion

An L*a*b* color space composed of L*, a*, and b* components whose values are packed with 10 bits per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used. The 10-bit unsigned a* and b* channels are interpreted numerically as ranging from -128.0 to approximately 128.0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab32space)*