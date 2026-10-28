# interaction(_:shouldBeginAt:for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method

A default implementation that indicates that the interaction begins.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func interaction(_ interaction: ImageAnalysisInteraction, shouldBeginAt point: CGPoint, for interactionType: ImageAnalysisInteraction.InteractionTypes) -> Bool
```

## Return Value

This default implementation returns `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/interaction(_:shouldbeginat:for:)-9n9q4)*