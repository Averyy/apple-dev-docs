# kCIApplyOptionExtent

**Framework**: Core Image  
**Kind**: var

The extent of the image.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let kCIApplyOptionExtent: String
```

#### Discussion

The size of the produced image. The associated value is a four-element array ([`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray)) that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

## See Also

- [let kCIApplyOptionDefinition: String](kciapplyoptiondefinition.md)
  The domain of definition (DOD) of the produced image.
- [let kCIApplyOptionUserInfo: String](kciapplyoptionuserinfo.md)
  Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.
- [let kCIApplyOptionColorSpace: String](kciapplyoptioncolorspace.md)
  The color space of the produced image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/kciapplyoptionextent)*