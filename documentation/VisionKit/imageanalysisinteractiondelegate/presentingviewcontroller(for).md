# presentingViewController(for:)

**Framework**: VisionKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the view controller that presents the interface objects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentingViewController(for interaction: ImageAnalysisInteraction) -> UIViewController?
```

#### Return Value

The view controller that presents the interaction object’s highlights, menus, and other elements.

#### Discussion

The default return value is the window’s root view controller.

## Parameters

- `interaction`: The associated interaction object for the presented view.

## Default Implementations

### ImageAnalysisInteractionDelegate Implementations
- [func presentingViewController(for: ImageAnalysisInteraction) -> UIViewController?](./presentingviewcontroller%28for%29-3gzbq.md)
  A default implementation that provides the interaction view’s root view controller.

## See Also

### Providing interface details
- [func contentView(for: ImageAnalysisInteraction) -> UIView?](./contentview%28for%29.md)
  Provides the view that contains the image.
- [func contentsRect(for: ImageAnalysisInteraction) -> CGRect](./contentsrect%28for%29.md)
  Returns the rectangle, in unit coordinates, that contains the image within the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/presentingviewcontroller(for:))*