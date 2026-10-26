# cmRGBA32Space

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

An RGB color space composed of red, green, and blue color value components, followed by an alpha channel component. Values are packed with 8 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits.

**Availability**:
- macOS 10.0+

## Declaration

```c
cmRGBA32Space = cmRGBASpace + cm32_8ColorPacking + cmAlphaLastPacking
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba32space)*