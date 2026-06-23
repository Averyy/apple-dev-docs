# isValid

**Framework**: USDKit  
**Kind**: property

A Boolean value indicating whether this property is valid.

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

A property’s validity is connected to a [`USDStage`](usdstage.md). A property becomes invalid when the lifetime of its stage ends.

A property will also expire if its stage no longer defines a value for the property. `isValid` is false if this property has expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/isvalid)*