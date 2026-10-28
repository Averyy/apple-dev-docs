# contentView(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the view that contains the image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentView(for interaction: ImageAnalysisInteraction) -> UIView?
```

## Return Value

The view that contains the image for this interaction.

## Discussion

Implement this delegate method only when the view that contains the image isn’t the same as the interaction’s view.

## Parameters

- `interaction`: The associated interaction object for the content view.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func contentView(for: ImageAnalysisInteraction) -> UIView?](./contentview%28for%29-28l6r.md)
  A default implementation that provides the interaction’s view.

## See Also

### Providing interface details
- [func contentsRect(for: ImageAnalysisInteraction) -> CGRect](./contentsrect%28for%29.md)
  Returns the rectangle, in unit coordinates, that contains the image within the view.
- [func presentingViewController(for: ImageAnalysisInteraction) -> UIViewController?](./presentingviewcontroller%28for%29.md)
  Provides the view controller that presents the interface objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/contentview(for:))*