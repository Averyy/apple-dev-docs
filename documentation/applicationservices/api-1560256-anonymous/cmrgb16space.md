# cmRGB16Space

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

An RGB color space composed of red, green, and blue components whose values are packed with 5 bits of storage per component. The storage size for a color value expressed in this color space is 16 bits, with the high-order bit not used.

**Availability**:
- macOS 10.0+

## Declaration

```c
cmRGB16Space = cmRGBSpace + cmWord5ColorPacking
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb16space)*