# didMove(to:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

Performs an action after the view adds or removes the interaction from its interaction array.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency final func didMove(to view: UIView?)
```

## Parameters

- `view`: The view that owns and contains the interaction in its interaction array.

## See Also

### Responding to view events
- [func willMove(to: UIView?)](./willmove%28to%29.md)
  Performs an action before the view adds or removes the interaction from its interaction array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/didmove(to:))*