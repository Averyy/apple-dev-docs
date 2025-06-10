# presentingViewController(for:)

**Framework**: VisionKit  
**Kind**: method  
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

## See Also

- [func contentView(for: ImageAnalysisInteraction) -> UIView?](imageanalysisinteractiondelegate/contentview(for:).md)
  Provides the view that contains the image.
- [func contentsRect(for: ImageAnalysisInteraction) -> CGRect](imageanalysisinteractiondelegate/contentsrect(for:).md)
  Returns the rectangle, in unit coordinates, that contains the image within the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/imageanalysisinteractiondelegate/presentingviewcontroller(for:))*