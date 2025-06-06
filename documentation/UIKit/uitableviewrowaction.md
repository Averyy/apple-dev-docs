# UITableViewRowAction

**Framework**: UIKit  
**Kind**: class

A single action to present when the user swipes horizontally in a table row.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class UITableViewRowAction
```

#### Overview

Create a [`UITableViewRowAction`](uitableviewrowaction.md) object to define a single, custom action for a table row. Users swipe horizontally in a table view to reveal the actions associated with a row. Each row-action object contains the text display, the action to perform, and any specific formatting to apply to that action.

To add custom actions to your table view’s rows, implement the [`tableView(_:editActionsForRowAt:)`](uitableviewdelegate/tableview(_:editactionsforrowat:).md) method in your table view’s delegate object. In that method, create and return the actions for the indicated row. The table displays your action buttons and executes the appropriate handler block when the user taps one of them.

## Topics

### Creating a table row action
- [convenience init(style: UITableViewRowAction.Style, title: String?, handler: (UITableViewRowAction, IndexPath) -> Void)](uitableviewrowaction/init(style:title:handler:).md)
  Creates and returns a new table view row action object.
### Configuring the action’s appearance
- [var style: UITableViewRowAction.Style](uitableviewrowaction/style-swift.property.md)
  The style applied to the action button.
- [UITableViewRowAction.Style](uitableviewrowaction/style-swift.enum.md)
  Constants that specify the appearance of action buttons.
- [var title: String?](uitableviewrowaction/title.md)
  The title of the action button.
- [var backgroundColor: UIColor?](uitableviewrowaction/backgroundcolor.md)
  The background color of the action button.
- [var backgroundEffect: UIVisualEffect?](uitableviewrowaction/backgroundeffect.md)
  The visual effect to apply to the button.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

- [class UISwipeActionsConfiguration](uiswipeactionsconfiguration.md)
  The set of actions to perform when swiping on rows of a table.
- [class UIContextualAction](uicontextualaction.md)
  An action to display when the user swipes a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewrowaction)*