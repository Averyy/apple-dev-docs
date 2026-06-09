# isValid

**Framework**: USDKit  
**Kind**: property

A Boolean value indicating whether this attribute is valid.

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

An attribute’s validity is connected to a [`USDStage`](usdstage-4sfi1.md). An attribute becomes invalid when the lifetime of its stage ends.

An attribute will also expire if its stage no longer defines a value for the attribute. `isValid` is false if this attribute has expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/isvalid)*