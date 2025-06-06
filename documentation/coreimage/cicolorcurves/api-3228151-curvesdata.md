# curvesData

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

Color values that determine the color curves transform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var curvesData: Data { get set }
```

#### Discussion

Create the curves data as an [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object containing a sequence of single-precision RGB values. These values represent a lookup table that’s applied to the input image. 

Core Image unpremultiplies the image before applying the effect, and premultiplies the result after applying the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolorcurves/3228151-curvesdata)*