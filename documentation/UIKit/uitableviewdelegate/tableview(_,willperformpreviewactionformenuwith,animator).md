# tableView(_:willPerformPreviewActionForMenuWith:animator:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate when a user triggers a commit by tapping the preview.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tableView(_ tableView: UITableView, willPerformPreviewActionForMenuWith configuration: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)
```

```objc
- (void) tableView:(UITableView *) tableView willPerformPreviewActionForMenuWithConfiguration:(UIContextMenuConfiguration *) configuration animator:(id<UIContextMenuInteractionCommitAnimating>) animator;
```

## Parameters

- `tableView`: The table view informing the delegate of this event.
- `configuration`: The configuration of the menu being displayed.
- `animator`: The animations to run alongside the commit transition.

## See Also

### Managing context menus
- [Adding context menus in your app](../adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func tableView(UITableView, contextMenuConfigurationForRowAt: IndexPath, point: CGPoint) -> UIContextMenuConfiguration?](./tableview%28_,contextmenuconfigurationforrowat,point%29.md)
  Returns a context menu configuration for the row at a point.
- [func tableView(UITableView, previewForDismissingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./tableview%28_,previewfordismissingcontextmenuwithconfiguration%29.md)
  Returns the destination view when dismissing a context menu.
- [func tableView(UITableView, previewForHighlightingContextMenuWithConfiguration: UIContextMenuConfiguration) -> UITargetedPreview?](./tableview%28_,previewforhighlightingcontextmenuwithconfiguration%29.md)
  Returns a view to override the default preview the table view created.
- [func tableView(UITableView, willDisplayContextMenu: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./tableview%28_,willdisplaycontextmenu,animator%29.md)
  Informs the delegate when a context menu will appear.
- [func tableView(UITableView, willEndContextMenuInteraction: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./tableview%28_,willendcontextmenuinteraction,animator%29.md)
  Informs the delegate when a context menu will disappear.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewdelegate/tableview(_:willperformpreviewactionformenuwith:animator:))*