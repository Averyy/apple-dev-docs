# blendedAxisValueBounds

**Framework**: hvf  
**Kind**: property

After rendering, returns the maximum and minimum blended values set on any axis in the part’s tree This is useful for detecting axes going out of range (-1.0…1.0)

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
var blendedAxisValueBounds: ClosedRange<Double> { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/partrenderer/blendedaxisvaluebounds)*