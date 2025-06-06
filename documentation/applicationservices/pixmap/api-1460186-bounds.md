# bounds

**Framework**: Application Services  
**Kind**: structp

The boundary rectangle, which links the local coordinate system of a graphics port to QuickDraw's global coordinate system and defines the area of the bit image into which QuickDraw can draw. By default, the boundary rectangle is the entire main screen. Do not use the `value` of this field to determine the size of the screen; instead use the `value` of the `gdRect` field of the [`GDevice`](gdevice.md) structure for the screen.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var bounds: Rect
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/pixmap/1460186-bounds)*