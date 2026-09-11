# isValid

**Framework**: USDKit  
**Kind**: property

A Boolean value indicating whether this attribute is valid.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var isValid: Bool { get }
```

#### Discussion

An attribute’s validity is connected to a [`USDStage`](usdstage.md). An attribute becomes invalid when the lifetime of its stage ends.

An attribute will also expire if its stage no longer defines a value for the attribute. `isValid` is false if this attribute has expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/isvalid)*