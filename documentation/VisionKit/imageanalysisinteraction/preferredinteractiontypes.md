# preferredInteractionTypes

**Framework**: VisionKit  
**Kind**: property  
**Role**: Instance Property

The types of interactions that people can perform with the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
final var preferredInteractionTypes: ImageAnalysisInteraction.InteractionTypes { get set }
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

## Discussion

You need to set this property to enable interactions with the image. If this property contains [`automatic`](./interactiontypes/automatic.md), the interaction ignores the other types in the set. The default value for this property is an empty array that disables any interactions.

If you set this property to one or more types, the interaction sets the view’s [`isUserInteractionEnabled`](../../UIKit/uiview/isuserinteractionenabled.md) property to `true` so that the interaction begins. For example, when you’re ready to start the Live Text interface, set this property to [`automatic`](./interactiontypes/automatic.md).

If you set this property to an empty array, the image analysis interaction doesn’t reset the view’s `isUserInteractionEnabled` property to `false`.

## See Also

### Configuring an image interaction
- [var delegate: (any ImageAnalysisInteractionDelegate)?](./delegate.md)
  The delegate that handles the interaction callbacks.
- [var analysis: ImageAnalysis?](./analysis.md)
  The results of analyzing an image for items that people can interact with.
- [var view: UIView?](./view.md)
  The view that uses this interaction.
- [ImageAnalysisInteraction.InteractionTypes](./interactiontypes.md)
  The types of interactions that people can perform with an image.
- [var activeInteractionTypes: ImageAnalysisInteraction.InteractionTypes](./activeinteractiontypes.md)
  The types of interactions that a person actively performs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteraction/preferredinteractiontypes)*