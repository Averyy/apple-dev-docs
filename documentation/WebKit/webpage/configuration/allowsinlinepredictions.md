# allowsInlinePredictions

**Framework**: WebKit  
**Kind**: property

Indicates whether inline predictions are allowed.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var allowsInlinePredictions: Bool
```

#### Discussion

The default value is `false`. If false, inline predictions are disabled regardless of the system setting. If true, they are enabled based on the system setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/configuration/allowsinlinepredictions)*