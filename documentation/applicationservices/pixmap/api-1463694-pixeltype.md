# pixelType

**Framework**: Application Services  
**Kind**: structp

The storage format for a pixel image. Indexed pixels are indicated by a value of 0. Direct pixels are specified by a value of `RGBDirect`, or 16. In the `PixMap` record of the [`GDevice`](gdevice.md) structure for a direct device, this field is set to `RGBDirect` when the screen depth is set.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var pixelType: Int16
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1463694-pixeltype)*