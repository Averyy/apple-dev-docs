# UITableView

**Framework**: UIKit  
**Kind**: class

A view that presents data using rows in a single column.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableView
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)
- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
- [Estimating the height of a table’s scrolling area](estimating-the-height-of-a-table-s-scrolling-area.md)
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Overview

Table views in iOS display rows of vertically scrolling content in a single column. Each row in the table contains one piece of your app’s content. For example, the Contacts app displays the name of each contact in a separate row, and the main page of the Settings app displays the available groups of settings. You can configure a table to display a single long list of rows, or you can group related rows into sections to make navigating the content easier.

Tables are common in apps with data that’s highly structured or organized hierarchically. Apps that contain hierarchical data often use tables in conjunction with a navigation view controller, which facilitates navigation between different levels of the hierarchy. For example, the Settings app uses tables and a navigation controller to organize the system settings.

[`UITableView`](uitableview.md) manages the basic appearance of the table, but your app provides the cells ([`UITableViewCell`](uitableviewcell.md) objects) that display the actual content. The standard cell configurations display a simple combination of text and images, but you can define custom cells that display any content you want. You can also supply header and footer views to provide additional information for groups of cells.

##### Add a Table View to Your Interface

To add a table view to your interface, drag a table view controller ([`UITableViewController`](uitableviewcontroller.md)) object to your storyboard. Xcode creates a new scene that includes both the view controller and a table view, ready for you to configure and use.

Table views are data-driven, normally getting their data from a data source object that you provide. The data source object manages your app’s data and is responsible for creating and configuring the table’s cells. If the content of your table never changes, you can configure that content in your storyboard file instead.

For information about how to specify your table’s data, see [`Filling a table with data`](filling-a-table-with-data.md).

##### Save and Restore the Tables Current State

Table views support UIKit app restoration. To save and restore the table’s data, assign a nonempty value to the table view’s [`restorationIdentifier`](uiviewcontroller/restorationidentifier.md) property. When you save its parent view controller, the table view automatically saves the index paths for the currently selected and visible rows. If the table’s data source object adopts the [`UIDataSourceModelAssociation`](uidatasourcemodelassociation.md) protocol, the table stores the unique IDs that you provide for those items instead of their index paths.

For information about how to save and restore your app’s state information, see [`Preserving your app’s UI across launches`](preserving-your-app-s-ui-across-launches.md).

## Topics

### Creating a table view
- [init(frame: CGRect, style: UITableView.Style)](uitableview/init(frame:style:).md)
  Creates and returns a table view with the specified frame and style.
- [init?(coder: NSCoder)](uitableview/init(coder:).md)
  Creates a table view object from data in an unarchiver.
### Providing the data and cells
- [var dataSource: (any UITableViewDataSource)?](uitableview/datasource.md)
  The object that acts as the data source of the table view.
- [var prefetchDataSource: (any UITableViewDataSourcePrefetching)?](uitableview/prefetchdatasource.md)
  The object that acts as the prefetching data source for the table view, receiving notifications of upcoming cell data requirements.
- [var isPrefetchingEnabled: Bool](uitableview/isprefetchingenabled.md)
  A Boolean value that indicates whether to allow cell and data prefetching.
- [protocol UITableViewDataSource](uitableviewdatasource.md)
  The methods that an object adopts to manage data and provide cells for a table view.
- [protocol UITableViewDataSourcePrefetching](uitableviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a table view, allowing you to start potentially long-running data operations early.
### Recycling table view cells
- [func register(UINib?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-5q6bo.md)
  Registers a nib object that contains a cell with the table view under a specified identifier.
- [func register(AnyClass?, forCellReuseIdentifier: String)](uitableview/register(_:forcellreuseidentifier:)-3l3ct.md)
  Registers a class to use in creating new table cells.
- [func dequeueReusableCell(withIdentifier: String, for: IndexPath) -> UITableViewCell](uitableview/dequeuereusablecell(withidentifier:for:).md)
  Returns a reusable table-view cell object for the specified reuse identifier and adds it to the table.
- [func dequeueReusableCell(withIdentifier: String) -> UITableViewCell?](uitableview/dequeuereusablecell(withidentifier:).md)
  Returns a reusable table-view cell object after locating it by its identifier.
### Recycling section headers and footers
- [func register(UINib?, forHeaderFooterViewReuseIdentifier: String)](uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc.md)
  Registers a nib object that contains a header or footer with the table view under a specified identifier.
- [func register(AnyClass?, forHeaderFooterViewReuseIdentifier: String)](uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb.md)
  Registers a class to use in creating new table header or footer views.
- [func dequeueReusableHeaderFooterView(withIdentifier: String) -> UITableViewHeaderFooterView?](uitableview/dequeuereusableheaderfooterview(withidentifier:).md)
  Returns a reusable header or footer view after locating it by its identifier.
### Managing interactions with the table
- [var delegate: (any UITableViewDelegate)?](uitableview/delegate.md)
  The object that acts as the delegate of the table view.
- [protocol UITableViewDelegate](uitableviewdelegate.md)
  Methods for managing selections, configuring section headers and footers, deleting and reordering cells, and performing other actions in a table view.
### Configuring the table’s appearance
- [var style: UITableView.Style](uitableview/style-swift.property.md)
  The style of the table view.
- [UITableView.Style](uitableview/style-swift.enum.md)
  Constants for the table view styles.
- [var tableHeaderView: UIView?](uitableview/tableheaderview.md)
  The view that displays above the table’s content.
- [var tableFooterView: UIView?](uitableview/tablefooterview.md)
  The view that displays below the table’s content.
- [var backgroundView: UIView?](uitableview/backgroundview.md)
  The background view of the table view.
### Configuring cell height and layout
- [var rowHeight: CGFloat](uitableview/rowheight.md)
  The default height in points of each row in the table view.
- [var estimatedRowHeight: CGFloat](uitableview/estimatedrowheight.md)
  The estimated height of rows in the table view.
- [var fillerRowHeight: CGFloat](uitableview/fillerrowheight.md)
  The height for empty rows that fill the table view.
- [var cellLayoutMarginsFollowReadableWidth: Bool](uitableview/celllayoutmarginsfollowreadablewidth.md)
  A Boolean value that indicates whether the cell margins derive from the width of the readable content guide.
- [var insetsContentViewsToSafeArea: Bool](uitableview/insetscontentviewstosafearea.md)
  A Boolean value that indicates whether the table view adjusts the content views of its cells, headers, and footers to fit within the safe area.
### Configuring header and footer appearance
- [var sectionHeaderHeight: CGFloat](uitableview/sectionheaderheight.md)
  The height of section headers in the table view.
- [var sectionFooterHeight: CGFloat](uitableview/sectionfooterheight.md)
  The height of section footers in the table view.
- [var estimatedSectionHeaderHeight: CGFloat](uitableview/estimatedsectionheaderheight.md)
  The estimated height of section headers in the table view.
- [var estimatedSectionFooterHeight: CGFloat](uitableview/estimatedsectionfooterheight.md)
  The estimated height of section footers in the table view.
- [var sectionHeaderTopPadding: CGFloat](uitableview/sectionheadertoppadding.md)
  The amount of padding above each section header.
### Customizing the separator appearance
- [var separatorStyle: UITableViewCell.SeparatorStyle](uitableview/separatorstyle.md)
  The style for table cells to use as separators.
- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.
- [var separatorColor: UIColor?](uitableview/separatorcolor.md)
  The color of separator rows in the table view.
- [var separatorEffect: UIVisualEffect?](uitableview/separatoreffect.md)
  The effect to apply to table separators.
- [var separatorInset: UIEdgeInsets](uitableview/separatorinset.md)
  The default inset of cell separators.
- [var separatorInsetReference: UITableView.SeparatorInsetReference](uitableview/separatorinsetreference-swift.property.md)
  An indicator of how to interpret the separator inset value.
- [UITableView.SeparatorInsetReference](uitableview/separatorinsetreference-swift.enum.md)
  Constants that indicate how to interpret the separator inset value of a table view.
### Getting the number of rows and sections
- [func numberOfRows(inSection: Int) -> Int](uitableview/numberofrows(insection:).md)
  Returns the number of rows (table cells) in a specified section.
- [var numberOfSections: Int](uitableview/numberofsections.md)
  The number of sections in the table view.
### Getting cells and section-based views
- [func cellForRow(at: IndexPath) -> UITableViewCell?](uitableview/cellforrow(at:).md)
  Returns the table cell at the index path you specify.
- [func headerView(forSection: Int) -> UITableViewHeaderFooterView?](uitableview/headerview(forsection:).md)
  Returns the header view for the specified section.
- [func footerView(forSection: Int) -> UITableViewHeaderFooterView?](uitableview/footerview(forsection:).md)
  Returns the footer view for the specified section.
- [func indexPath(for: UITableViewCell) -> IndexPath?](uitableview/indexpath(for:).md)
  Returns an index path that represents the row and section of a specified table-view cell.
- [func indexPathForRow(at: CGPoint) -> IndexPath?](uitableview/indexpathforrow(at:).md)
  Returns an index path that identifies the row and section at the specified point.
- [func indexPathsForRows(in: CGRect) -> [IndexPath]?](uitableview/indexpathsforrows(in:).md)
  Returns an array of index paths, each representing a row that the specified rectangle encloses.
- [var visibleCells: [UITableViewCell]](uitableview/visiblecells.md)
  The table cells that are visible in the table view.
- [var indexPathsForVisibleRows: [IndexPath]?](uitableview/indexpathsforvisiblerows.md)
  An array of index paths, each identifying a visible row in the table view.
### Selecting rows
- [var indexPathForSelectedRow: IndexPath?](uitableview/indexpathforselectedrow.md)
  An index path that identifies the row and section of the selected row.
- [var indexPathsForSelectedRows: [IndexPath]?](uitableview/indexpathsforselectedrows.md)
  The index paths that represent the selected rows.
- [func selectRow(at: IndexPath?, animated: Bool, scrollPosition: UITableView.ScrollPosition)](uitableview/selectrow(at:animated:scrollposition:).md)
  Selects a row in the table view that an index path identifies, optionally scrolling the row to a location in the table view.
- [func deselectRow(at: IndexPath, animated: Bool)](uitableview/deselectrow(at:animated:).md)
  Deselects a row that an index path identifies, with an option to animate the deselection.
- [var allowsSelection: Bool](uitableview/allowsselection.md)
  A Boolean value that determines whether users can select a row.
- [var allowsMultipleSelection: Bool](uitableview/allowsmultipleselection.md)
  A Boolean value that determines whether users can select more than one row outside of editing mode.
- [var allowsSelectionDuringEditing: Bool](uitableview/allowsselectionduringediting.md)
  A Boolean value that determines whether users can select cells while the table view is in editing mode.
- [var allowsMultipleSelectionDuringEditing: Bool](uitableview/allowsmultipleselectionduringediting.md)
  A Boolean value that controls whether users can select more than one cell simultaneously in editing mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [class let selectionDidChangeNotification: NSNotification.Name](uitableview/selectiondidchangenotification.md)
  A notification that posts when the selected row in the posting table view changes.
### Inserting, deleting, and moving rows and sections
- [func insertRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/insertrows(at:with:).md)
  Inserts rows in the table view at the locations that an array of index paths identifies, with an option to animate the insertion.
- [func deleteRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/deleterows(at:with:).md)
  Deletes the rows that an array of index paths identifies, with an option to animate the deletion.
- [func insertSections(IndexSet, with: UITableView.RowAnimation)](uitableview/insertsections(_:with:).md)
  Inserts one or more sections in the table view, with an option to animate the insertion.
- [func deleteSections(IndexSet, with: UITableView.RowAnimation)](uitableview/deletesections(_:with:).md)
  Deletes one or more sections in the table view, with an option to animate the deletion.
- [UITableView.RowAnimation](uitableview/rowanimation.md)
  The type of animation to use when inserting or deleting rows.
- [func moveRow(at: IndexPath, to: IndexPath)](uitableview/moverow(at:to:).md)
  Moves the row at a specified location to a destination location.
- [func moveSection(Int, toSection: Int)](uitableview/movesection(_:tosection:).md)
  Moves a section to a new location in the table view.
### Performing batch updates to rows and sections
- [func performBatchUpdates((() -> Void)?, completion: ((Bool) -> Void)?)](uitableview/performbatchupdates(_:completion:).md)
  Animates multiple insert, delete, reload, and move operations as a group.
- [func beginUpdates()](uitableview/beginupdates.md)
  Begins a series of method calls that insert, delete, or select rows and sections of the table view.
- [func endUpdates()](uitableview/endupdates.md)
  Concludes a series of method calls that insert, delete, select, or reload rows and sections of the table view.
### Reloading the table view
- [var hasUncommittedUpdates: Bool](uitableview/hasuncommittedupdates.md)
  A Boolean value that indicates whether the table view’s appearance contains changes that aren’t present in its data source.
- [func reconfigureRows(at: [IndexPath])](uitableview/reconfigurerows(at:).md)
  Updates the data for the rows at the index paths you specify, preserving the existing cells for the rows.
- [func reloadData()](uitableview/reloaddata.md)
  Reloads the rows and sections of the table view.
- [func reloadRows(at: [IndexPath], with: UITableView.RowAnimation)](uitableview/reloadrows(at:with:).md)
  Reloads the specified rows using the provided animation effect.
- [func reloadSections(IndexSet, with: UITableView.RowAnimation)](uitableview/reloadsections(_:with:).md)
  Reloads the specified sections using the provided animation effect.
- [func reloadSectionIndexTitles()](uitableview/reloadsectionindextitles.md)
  Reloads the items in the index bar along the right side of the table view.
### Managing drag interactions
- [var dragDelegate: (any UITableViewDragDelegate)?](uitableview/dragdelegate.md)
  The delegate object that manages the dragging of items from the table view.
- [protocol UITableViewDragDelegate](uitableviewdragdelegate.md)
  The interface for initiating drags from a table view.
- [var hasActiveDrag: Bool](uitableview/hasactivedrag.md)
  A Boolean value that indicates whether the table view is currently tracking a drag session.
- [var dragInteractionEnabled: Bool](uitableview/draginteractionenabled.md)
  A Boolean value that indicates whether the table view supports dragging content.
### Managing drop interactions
- [var dropDelegate: (any UITableViewDropDelegate)?](uitableview/dropdelegate.md)
  The delegate object that manages the dropping of content into the table view.
- [protocol UITableViewDropDelegate](uitableviewdropdelegate.md)
  The interface for handling drops in a table view.
- [var hasActiveDrop: Bool](uitableview/hasactivedrop.md)
  A Boolean value that indicates whether the table view is currently tracking a drop session.
### Scrolling the table view
- [func scrollToRow(at: IndexPath, at: UITableView.ScrollPosition, animated: Bool)](uitableview/scrolltorow(at:at:animated:).md)
  Scrolls through the table view until a row that an index path identifies is at a particular location on the screen.
- [func scrollToNearestSelectedRow(at: UITableView.ScrollPosition, animated: Bool)](uitableview/scrolltonearestselectedrow(at:animated:).md)
  Scrolls the table view so that the selected row nearest to a specified position in the table view is at that position.
- [UITableView.ScrollPosition](uitableview/scrollposition.md)
  The position in the table view (top, middle, bottom) to scroll a specified row to.
### Putting the table into edit mode
- [func setEditing(Bool, animated: Bool)](uitableview/setediting(_:animated:).md)
  Toggles the table view into and out of editing mode.
- [var isEditing: Bool](uitableview/isediting.md)
  A Boolean value that determines whether the table view is in editing mode.
### Configuring the table index
- [var sectionIndexMinimumDisplayRowCount: Int](uitableview/sectionindexminimumdisplayrowcount.md)
  The number of table rows at which to display the index list on the right edge of the table.
- [var sectionIndexColor: UIColor?](uitableview/sectionindexcolor.md)
  The color to use for the table view’s index text.
- [var sectionIndexBackgroundColor: UIColor?](uitableview/sectionindexbackgroundcolor.md)
  The color to use for the background of the table view’s section index.
- [var sectionIndexTrackingBackgroundColor: UIColor?](uitableview/sectionindextrackingbackgroundcolor.md)
  The color to use for the table view’s index background area.
- [class let indexSearch: String](uitableview/indexsearch.md)
  A constant for adding the magnifying glass icon to the section index of a table view.
### Getting the drawing areas for the table
- [func rect(forSection: Int) -> CGRect](uitableview/rect(forsection:).md)
  Returns the drawing area for a specified section of the table view.
- [func rectForRow(at: IndexPath) -> CGRect](uitableview/rectforrow(at:).md)
  Returns the drawing area for a row that an index path identifies.
- [func rectForFooter(inSection: Int) -> CGRect](uitableview/rectforfooter(insection:).md)
  Returns the drawing area for the footer of the specified section.
- [func rectForHeader(inSection: Int) -> CGRect](uitableview/rectforheader(insection:).md)
  Returns the drawing area for the header of the specified section.
### Working with focus
- [var allowsFocus: Bool](uitableview/allowsfocus.md)
  A Boolean value that determines whether the table view allows its cells to become focused.
- [var allowsFocusDuringEditing: Bool](uitableview/allowsfocusduringediting.md)
  A Boolean value that determines whether the table view allows its cells to become focused in edit mode.
- [var selectionFollowsFocus: Bool](uitableview/selectionfollowsfocus.md)
  A Boolean value that triggers an automatic selection when focus moves to a cell.
- [var remembersLastFocusedIndexPath: Bool](uitableview/rememberslastfocusedindexpath.md)
  A Boolean value that indicates whether the table view automatically returns the focus to the cell at the last focused index path.
### Managing context menus
- [var contextMenuInteraction: UIContextMenuInteraction?](uitableview/contextmenuinteraction.md)
  The table view’s context menu interaction.
### Resizing self-sizing cells
- [var selfSizingInvalidation: UITableView.SelfSizingInvalidation](uitableview/selfsizinginvalidation-swift.property.md)
  The mode that the table view uses for invalidating the size of self-sizing cells.
- [UITableView.SelfSizingInvalidation](uitableview/selfsizinginvalidation-swift.enum.md)
  Constants that describe modes for invalidating the size of self-sizing table view cells.
### Managing content-hugging behavior
- [var contentHuggingElements: UITableViewContentHuggingElements](uitableview/contenthuggingelements.md)
  A setting that determines which type of items tightly hug their content.
- [struct UITableViewContentHuggingElements](uitableviewcontenthuggingelements.md)
  Constants that determine which types of items in a table view tightly hug their content.
### Structures
- [UITableView.SelectionDidChangeMessage](uitableview/selectiondidchangemessage.md)

## Relationships

### Inherits From
- [UIScrollView](uiscrollview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDataSourceTranslating](uidatasourcetranslating.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableview)*