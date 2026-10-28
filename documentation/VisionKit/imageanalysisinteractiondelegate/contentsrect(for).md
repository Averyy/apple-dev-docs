# contentsRect(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the rectangle, in unit coordinates, that contains the image within the view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentsRect(for interaction: ImageAnalysisInteraction) -> CGRect
```

## Mentions

- [Enabling Live Text interactions with images](../enabling-live-text-interactions-with-images.md)

## Return Value

The rectangle of the image within the view, in unit coordinates. The default return value is the unit rectangle, `[0.0, 0.0, 1.0, 1.0]`, which represents the whole view contents.

## Discussion

Implement this method when the interaction view type isn’t [`UIImageView`](../../UIKit/uiimageview.md).

## Parameters

- `interaction`: The associated interaction object for the contents rectangle.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func contentsRect(for: ImageAnalysisInteraction) -> CGRect](./contentsrect%28for%29-90dek.md)
  A default unit rectangle that represents the full size of the interaction view.

## See Also

### Providing interface details
- [func contentView(for: ImageAnalysisInteraction) -> UIView?](./contentview%28for%29.md)
  Provides the view that contains the image.
- [func presentingViewController(for: ImageAnalysisInteraction) -> UIViewController?](./presentingviewcontroller%28for%29.md)
  Provides the view controller that presents the interface objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/contentsrect(for:))*