# tableView(_:willEndContextMenuInteraction:animator:)

**Framework**: UIKit  
**Kind**: method

Informs the delegate when a context menu will disappear.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tableView(_ tableView: UITableView, willEndContextMenuInteraction configuration: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)
```

## Parameters

- `tableView`: The table view informing the delegate of this event.
- `configuration`: The ending configuration.
- `animator`: The animations to run alongside the disappearance transition.

## See Also

- [Adding context menus in your app](adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func tableView(UITableView, contextMenuConfigurationForRowAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](uitableviewdelegate/tableview(_:contextmenuconfigurationforrowat:point:).md)
  Returns a context menu configuration for the row at a point.
- [func tableView(UITableView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uitableviewdelegate/tableview(_:previewfordismissingcontextmenuwithconfiguration:).md)
  Returns the destination view when dismissing a context menu.
- [func tableView(UITableView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](uitableviewdelegate/tableview(_:previewforhighlightingcontextmenuwithconfiguration:).md)
  Returns a view to override the default preview the table view created.
- [func tableView(UITableView, willDisplayContextMenu: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](uitableviewdelegate/tableview(_:willdisplaycontextmenu:animator:).md)
  Informs the delegate when a context menu will appear.
- [func tableView(UITableView, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](uitableviewdelegate/tableview(_:willperformpreviewactionformenuwith:animator:).md)
  Informs the delegate when a user triggers a commit by tapping the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willendcontextmenuinteraction:animator:))*