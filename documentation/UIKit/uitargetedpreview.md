# UITargetedPreview

**Framework**: UIKit  
**Kind**: class

An object describing the view to use during preview-related animations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITargetedPreview
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Overview

Use a [`UITargetedPreview`](uitargetedpreview.md) to specify the view to use during an animated transition.

## Topics

### Creating a targeted preview object
- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [init(view: UIView, parameters: UIPreviewParameters, target: UIPreviewTarget)](uitargetedpreview/init(view:parameters:target:).md)
  Creates a targeted preview with the specified view, parameters, and target container.
- [convenience init(view: UIView, parameters: UIPreviewParameters)](uitargetedpreview/init(view:parameters:).md)
  Creates a targeted preview for a view in the current window and including the specified parameters.
- [convenience init(view: UIView)](uitargetedpreview/init(view:).md)
  Creates a targeted preview for a view in the current window.
### Getting the preview attributes
- [var view: UIView](uitargetedpreview/view.md)
  The view that’s the target of the animation.
- [var target: UIPreviewTarget](uitargetedpreview/target.md)
  The container for the target view.
- [var size: CGSize](uitargetedpreview/size.md)
  The size of the view.
- [var parameters: UIPreviewParameters](uitargetedpreview/parameters.md)
  Additional parameters to use when configuring the animations.
### Changing the target’s container
- [func retargetedPreview(with: UIPreviewTarget) -> UITargetedPreview](uitargetedpreview/retargetedpreview(with:).md)
  Returns a targeted preview object with the same view and parameters, but with a different target container.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UITargetedDragPreview](uitargeteddragpreview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIContextMenuInteraction](uicontextmenuinteraction.md)
  An interaction object that you use to display relevant actions for your content.
- [protocol UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
  The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [class UIPreviewTarget](uipreviewtarget.md)
  An object that specifies the container view to use for animations.
- [class UIPreviewParameters](uipreviewparameters.md)
  Additional parameters to use when animating a preview interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitargetedpreview)*