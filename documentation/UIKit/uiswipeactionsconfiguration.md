# UISwipeActionsConfiguration

**Framework**: UIKit  
**Kind**: class

The set of actions to perform when swiping on rows of a table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UISwipeActionsConfiguration
```

#### Overview

Create a [`UISwipeActionsConfiguration`](uiswipeactionsconfiguration.md) object to associate custom swipe actions with a row of your table view. Users swipe horizontally left or right in a table view to reveal the actions associated with a row. Each swipe-actions object contains the set of actions to display for each type of swipe.

To add custom actions to your table view’s rows, implement the [`tableView(_:leadingSwipeActionsConfigurationForRowAt:)`](uitableviewdelegate/tableview(_:leadingswipeactionsconfigurationforrowat:).md) or [`tableView(_:trailingSwipeActionsConfigurationForRowAt:)`](uitableviewdelegate/tableview(_:trailingswipeactionsconfigurationforrowat:).md) method of your table view’s delegate. In those methods, create and return the actions for the indicated row. The table displays your action buttons and executes the appropriate handler block when the user taps one of them.

## Topics

### Initializing the swipe actions
- [convenience init(actions: [UIContextualAction])](uiswipeactionsconfiguration/init(actions:).md)
  Creates a swipe action configuration object with the specified set of actions.
### Getting the swipe action information
- [var actions: [UIContextualAction]](uiswipeactionsconfiguration/actions.md)
  The swipe actions.
- [var performsFirstActionWithFullSwipe: Bool](uiswipeactionsconfiguration/performsfirstactionwithfullswipe.md)
  A Boolean value indicating whether a full swipe automatically performs the first action.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIContextualAction](uicontextualaction.md)
  An action to display when the user swipes a table row.
- [class UITableViewRowAction](uitableviewrowaction.md)
  A single action to present when the user swipes horizontally in a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration)*