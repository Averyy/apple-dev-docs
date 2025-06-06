# pmVersion

**Framework**: Application Services  
**Kind**: structp

The version number of Color QuickDraw that created this `PixMap` structure. The value of `pmVersion` is normally 0. If `pmVersion` is 4, Color QuickDraw treats the `PixMap` record's `baseAddr` field as 32-bit clean. All other flags are private. Most applications never need to set this field

**Availability**:
- macOS 10.0+

## Declaration

```swift
var pmVersion: Int16
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1460848-pmversion)*