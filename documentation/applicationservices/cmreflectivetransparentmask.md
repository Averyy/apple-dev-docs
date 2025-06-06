# cmReflectiveTransparentMask

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmReflectiveTransparentMask: Int { get }
```

#### Discussion

Bit 0 of `deviceAttributes[1]` specifies whether the media is transparent or reflective. If it has the value 0, the media is reflective; if it has the value 1, the media is transparent. Use the `cmReflectiveTransparentMask` mask to set the transparent/reflective bit in `deviceAttributes[1]` or to clear all bits except the transparent/reflective bit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmreflectivetransparentmask)*