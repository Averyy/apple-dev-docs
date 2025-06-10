# UITableViewController

**Framework**: UIKit  
**Kind**: class

A view controller that specializes in managing a table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableViewController
```

## Mentions

- [Filling a table with data](filling-a-table-with-data.md)
- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)
- [Handling row selection in a table view](handling-row-selection-in-a-table-view.md)

#### Overview

Subclass [`UITableViewController`](uitableviewcontroller.md) when your interface consists of a table view and little or no other content. Table view controllers already adopt the protocols you need to manage your table view’s content and respond to changes. In addition, [`UITableViewController`](uitableviewcontroller.md) implements the following behaviors:

- Automatically loads the table view archived in a storyboard or nib file, which you can access using the [`tableView`](uitableviewcontroller/tableview.md) property
- Sets the data source and the delegate of the table view to `self`
- Implements the [`viewWillAppear(_:)`](uiviewcontroller/viewwillappear(_:).md) method, automatically reloads the data for its table view on first appearance, and clears its selection (with or without animation, depending on the request) every time the table view appears (disable this last behavior by changing the value of [`clearsSelectionOnViewWillAppear`](uitableviewcontroller/clearsselectiononviewwillappear.md))
- Implements the [`viewDidAppear(_:)`](uiviewcontroller/viewdidappear(_:).md) method and automatically flashes the table view’s scroll indicators when it first appears
- Implements the [`setEditing(_:animated:)`](uiviewcontroller/setediting(_:animated:).md) method and automatically toggles the edit mode of the table when the user taps an Edit|Done button in the navigation bar
- Automatically resizes its table view to accommodate the appearance or disappearance of the onscreen keyboard

Create a custom subclass of [`UITableViewController`](uitableviewcontroller.md) for each table view that you manage. When you initialize the table view controller, you must specify the style of the table view (plain or grouped). You must also override the data source and delegate methods required to fill your table with data. You may override [`loadView()`](uiviewcontroller/loadview().md) or any other superclass method, but if you do, be sure to invoke the superclass implementation of the method, usually as the first method call.

## Topics

### Creating a table view controller
- [init(style: UITableView.Style)](uitableviewcontroller/init(style:).md)
  Initializes a table view controller to manage a table view of a given style.
- [init(nibName: String?, bundle: Bundle?)](uitableviewcontroller/init(nibname:bundle:).md)
  Creates a table view controller with the nib file in the specified bundle.
- [init?(coder: NSCoder)](uitableviewcontroller/init(coder:).md)
  Creates a table view controller from data in an unarchiver.
### Getting the table view
- [var tableView: UITableView!](uitableviewcontroller/tableview.md)
  Returns the table view managed by the controller object.
### Configuring the table behavior
- [var clearsSelectionOnViewWillAppear: Bool](uitableviewcontroller/clearsselectiononviewwillappear.md)
  A Boolean value indicating if the controller clears the selection when the table appears.
### Refreshing the table view
- [var refreshControl: UIRefreshControl?](uitableviewcontroller/refreshcontrol.md)
  The refresh control used to update the table contents.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIScrollViewDelegate](uiscrollviewdelegate.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITableViewDataSource](uitableviewdatasource.md)
- [UITableViewDelegate](uitableviewdelegate.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)
  Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.
- [Showing and hiding view controllers](showing-and-hiding-view-controllers.md)
  Display view controllers using different techniques, and pass data between them during transitions.
- [class UIViewController](uiviewcontroller.md)
  An object that manages a view hierarchy for your UIKit app.
- [class UICollectionViewController](uicollectionviewcontroller.md)
  A view controller that specializes in managing a collection view.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcontroller)*