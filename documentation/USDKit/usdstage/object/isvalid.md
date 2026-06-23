# isValid

**Framework**: USDKit  
**Kind**: property

A Boolean value indicating whether this object is valid.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

An object’s validity is connected to a [`USDStage`](usdstage.md). An object becomes invalid when the lifetime of its stage ends.

An object will also expire if its stage no longer defines a value for the object. `isValid` is false if this object has expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/isvalid)*