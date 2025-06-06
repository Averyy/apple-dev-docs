# init(view:parameters:)

**Framework**: UIKit  
**Kind**: init

Creates a targeted preview for a view in the current window and including the specified parameters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(view: UIView, parameters: UIPreviewParameters)
```

#### Return Value

A new targeted preview object.

## Parameters

- `view`: The view to animate. This view must be in a window.
- `parameters`: The animation parameters.

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [init(view: UIView, parameters: UIPreviewParameters, target: UIPreviewTarget)](uitargetedpreview/init(view:parameters:target:).md)
  Creates a targeted preview with the specified view, parameters, and target container.
- [convenience init(view: UIView)](uitargetedpreview/init(view:).md)
  Creates a targeted preview for a view in the current window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargetedpreview/init(view:parameters:))*