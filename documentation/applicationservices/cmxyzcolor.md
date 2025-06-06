# CMXYZColor

**Framework**: Application Services  
**Kind**: struct

Contains values for a color specified in XYZ color space.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CMXYZColor
```

#### Overview

Three color component values defined by the `CMXYZComponent` type definition combine to form a color value specified in the XYZ color space. The color value is defined by the `CMXYZColor` type definition.

Your application uses the `CMXYZColor` data structure to specify a color value in the `CMColor` union to use in general purpose color matching, color checking, or color conversion. You also use the `CMXYZColor` data structure to specify the XYZ white point reference used in the conversion of colors to or from the XYZ color space.  

## Topics

### Initializers
- [init()](cmxyzcolor/1462111-init.md)
- [init(X: CMXYZComponent, Y: CMXYZComponent, Z: CMXYZComponent)](cmxyzcolor/1459192-init.md)
### Instance Properties
- [var X: CMXYZComponent](cmxyzcolor/1458784-x.md)
- [var Y: CMXYZComponent](cmxyzcolor/1463301-y.md)
- [var Z: CMXYZComponent](cmxyzcolor/1460905-z.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmxyzcolor)*