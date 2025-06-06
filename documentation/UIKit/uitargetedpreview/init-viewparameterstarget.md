# init(view:parameters:target:)

**Framework**: UIKit  
**Kind**: init

Creates a targeted preview with the specified view, parameters, and target container.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(view: UIView, parameters: UIPreviewParameters, target: UIPreviewTarget)
```

#### Return Value

A new targeted preview object.

## Parameters

- `view`: The view to animate.
- `parameters`: The animation parameters.
- `target`: The container for the view.

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [convenience init(view: UIView, parameters: UIPreviewParameters)](uitargetedpreview/init(view:parameters:).md)
  Creates a targeted preview for a view in the current window and including the specified parameters.
- [convenience init(view: UIView)](uitargetedpreview/init(view:).md)
  Creates a targeted preview for a view in the current window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargetedpreview/init(view:parameters:target:))*