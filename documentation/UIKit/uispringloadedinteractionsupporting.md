# UISpringLoadedInteractionSupporting

**Framework**: UIKit  
**Kind**: protocol

The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UISpringLoadedInteractionSupporting : NSObjectProtocol
```

## Topics

### Checking the spring-loaded interaction status
- [var isSpringLoaded: Bool](uispringloadedinteractionsupporting/isspringloaded.md)
  A Boolean value that specifies whether the object is participating in spring-loaded interaction for a drag and drop activity.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIAlertController](uialertcontroller.md)
- [UIBarButtonItem](uibarbuttonitem.md)
- [UIButton](uibutton.md)
- [UICollectionView](uicollectionview.md)
- [UISearchTab](uisearchtab.md)
- [UISegmentedControl](uisegmentedcontrol.md)
- [UITab](uitab.md)
- [UITabBar](uitabbar.md)
- [UITabBarItem](uitabbaritem.md)
- [UITabGroup](uitabgroup.md)
- [UITableView](uitableview.md)

## See Also

- [protocol UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md)
  The interface for specifying the behavior of a spring-loaded interaction.
- [class UISpringLoadedInteraction](uispringloadedinteraction.md)
  An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [protocol UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md)
  The interface an object implements to provide information about a spring-loaded interaction.
- [protocol UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md)
  The interface for providing visual styling to a spring-loaded interaction based on the interaction state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uispringloadedinteractionsupporting)*