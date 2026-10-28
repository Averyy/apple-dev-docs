# interaction(_:shouldBeginAt:for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides a Boolean value that indicates whether the interaction can begin at the given point.

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

`true` if the interaction can begin; otherwise, `false`.

## Discussion

The system calls this method once for each type of interaction. The default value is `true`, which starts the interaction immediately after the image displays.

## Parameters

- `interaction`: The object for which interaction can begin.
- `point`: The point where the interaction can begin.
- `interactionType`: The type of interaction that can begin.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func interaction(ImageAnalysisInteraction, shouldBeginAt: CGPoint, for: ImageAnalysisInteraction.InteractionTypes) -> Bool](./interaction%28_,shouldbeginat,for%29-9n9q4.md)
  A default implementation that indicates that the interaction begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/interaction(_:shouldbeginat:for:))*