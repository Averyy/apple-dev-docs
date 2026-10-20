# packType

**Framework**: Application Services  
**Kind**: structp  
**Role**: Instance Property

The packing algorithm used to compress image data. Color QuickDraw currently supports a `packType` of 0, which means no packing, and values of 1 to 4 for packing direct pixels.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var packType: Int16
```

```c
short packType;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1459316-packtype)*