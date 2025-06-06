# rowBytes

**Framework**: Application Services  
**Kind**: structp

The offset in bytes from one row of the image to the next. The value must be even, less than 0x4000, and for best performance it should be a multiple of 4. The high 2 bits of `rowBytes` are used as flags. If bit 15 =1, the data structure pointed to is a `PixMap` structure; otherwise it is a [`BitMap`](bitmap.md) structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var rowBytes: Int16
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1462797-rowbytes)*