# isValid

**Framework**: USDKit  
**Kind**: property

A Boolean value indicating whether this relationship is valid.

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

A relationship’s validity is connected to a [`USDStage`](usdstage.md). A relationship becomes invalid when the lifetime of its stage ends.

A relationship will also expire if its stage no longer defines a value for the relationship. `isValid` is false if this relationship has expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/relationship/isvalid)*