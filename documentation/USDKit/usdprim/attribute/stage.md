# stage

**Framework**: USDKit  
**Kind**: property

The stage that owns this attribute.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var stage: USDStage { get }
```

#### Discussion

An attribute’s state and validity is connected to its stage. An attribute becomes invalid when the lifetime of its stage ends. It can also become invalid when the stage is modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/attribute/stage)*