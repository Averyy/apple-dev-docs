# OpenCPicParams

**Framework**: Application Services  
**Kind**: struct

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct OpenCPicParams
```

## Topics

### Initializers
- [init()](opencpicparams/1463952-init.md)
- [init(srcRect: Rect, hRes: Fixed, vRes: Fixed, version: Int16, reserved1: Int16, reserved2: Int32)](opencpicparams/1464130-init.md)
### Instance Properties
- [var hRes: Fixed](opencpicparams/1461719-hres.md)
  The best horizontal resolution for the picture. A value of 0x0048000 specifies a horizontal resolution of 72 dpi.
- [var reserved1: Int16](opencpicparams/1463913-reserved1.md)
  Reserved; set to 0.
- [var reserved2: Int32](opencpicparams/1459077-reserved2.md)
  Reserved; set to 0.
- [var srcRect: Rect](opencpicparams/1463268-srcrect.md)
  The optimal bounding rectangle for the resolution indicated by the `hRes` and `vRes` fields. To display a picture at a resolution other than that specified in the `hRes` and `vRes` fields, your application should compute an appropriate destination rectangle by scaling the image’s width and height by the destination resolution divided by the source resolution.
- [var vRes: Fixed](opencpicparams/1463078-vres.md)
  The best vertical resolution for the picture. A value of 0x0048000 specifies a vertical resolution of 72 dpi.
- [var version: Int16](opencpicparams/1462801-version.md)
  Always set this field to -2.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/opencpicparams)*