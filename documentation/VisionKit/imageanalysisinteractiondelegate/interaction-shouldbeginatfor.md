# interaction(_:shouldBeginAt:for:)

**Framework**: Visionkit  
**Kind**: method  
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

#### Return Value

`true` if the interaction can begin; otherwise, `false`.

#### Discussion

The system calls this method once for each type of interaction. The default value is `true`, which starts the interaction immediately after the image displays.

## Parameters

- `interaction`: The object for which interaction can begin.
- `point`: The point where the interaction can begin.
- `interactionType`: The type of interaction that can begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/interaction(_:shouldbeginat:for:))*