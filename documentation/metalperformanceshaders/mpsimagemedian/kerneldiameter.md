# kernelDiameter

**Framework**: Metal Performance Shaders  
**Kind**: property

The diameter, in pixels, of the filter window.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var kernelDiameter: Int { get }
```

#### Discussion

The median filter is applied to a `kernelDiameter * kernelDiameter` window of pixels centered on the corresponding source pixel for each destination pixel.  The kernel diameter must be an odd number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/kerneldiameter)*