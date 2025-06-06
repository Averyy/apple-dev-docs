# UITableViewCell

**Framework**: UIKit  
**Kind**: class

The visual representation of a single row in a table view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableViewCell
```

## Mentions

- [Filling a table with data](filling-a-table-with-data.md)
- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md)

#### Overview

A [`UITableViewCell`](uitableviewcell.md) object is a specialized type of view that manages the content of a single table row. You use cells primarily to organize and present your app’s custom content, but [`UITableViewCell`](uitableviewcell.md) provides some specific customizations to support table-related behaviors, including:

- Applying a selection or highlight color to the cell
- Adding standard accessory views, such as a detail or disclosure control
- Putting the cell into an editable state
- Indenting the cell’s content to create a visual hierarchy in your table

Your app’s content occupies most of the cell’s bounds, but the cell may adjust that space to make room for other content. Cells display accessory views on the trailing edge of their content area. When you put your table into edit mode, the cell adds a delete control to the leading edge of its content area, and optionally swaps out an accessory view for a reorder control.

![Illustration showing the area of a cell by itself and with an accessory view and edit control. The content area of a cell shrinks as needed to accommodate the accessory view or edit controls.](https://docs-assets.developer.apple.com/published/3eb9dd10bf532feaef9a5a57dc24113a/media-3113230%402x.png)

Every table view must have at least one type of cell for displaying content, and tables may have multiple cell types to display different types of content. Your table’s data source object handles the creation and configuration of cells immediately before they appear onscreen. For information about how to create your table’s cells, see [`Filling a table with data`](filling-a-table-with-data.md).

##### Configure Your Cells Content

Configure the content and layout of your cells in your storyboard file. Tables have one cell type by default, but you can add more by changing the value in the table’s Prototype Cells attribute. In addition to configuring the cell’s content, make sure you configure the following attributes:

- Identifier. Use this identifier (also known as a reuse identifier) to create the cell.
- Style. Choose one of the standard types or define a custom cell.
- Class. Specify a [`UITableViewCell`](uitableviewcell.md) subclass with your custom behavior.

To configure the content and appearance of your cell, you can set its [`contentConfiguration`](uitableviewcell/contentconfiguration-9ktox.md) and [`backgroundConfiguration`](uitableviewcell/backgroundconfiguration-24e8e.md).

## Topics

### Creating a table view cell
- [init(style: UITableViewCell.CellStyle, reuseIdentifier: String?)](uitableviewcell/init(style:reuseidentifier:).md)
  Initializes a table cell with a style and a reuse identifier and returns it to the caller.
- [UITableViewCell.CellStyle](uitableviewcell/cellstyle.md)
  An enumeration for the various styles of cells.
- [init?(coder: NSCoder)](uitableviewcell/init(coder:).md)
  Creates a table view from data in an unarchiver.
### Reusing cells
- [var reuseIdentifier: String?](uitableviewcell/reuseidentifier.md)
  A string for identifying a reusable cell.
- [func prepareForReuse()](uitableviewcell/prepareforreuse.md)
  Prepares a reusable cell for reuse by the table view’s delegate.
### Configuring the background
- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uitableviewcell/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewcell/backgroundconfiguration-24e8e.md)
  The current background configuration of the cell.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uitableviewcell/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uitableviewcell/backgroundview.md)
  The view to use as the background of the cell.
- [var selectedBackgroundView: UIView?](uitableviewcell/selectedbackgroundview.md)
  The view to use as the background for a selected cell.
- [var multipleSelectionBackgroundView: UIView?](uitableviewcell/multipleselectionbackgroundview.md)
  The background view to use for a selected cell when the table view allows multiple row selections.
### Managing the content
- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewcell/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the cell’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewcell/contentconfiguration-9ktox.md)
  The current content configuration of the cell.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewcell/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the cell automatically updates its content configuration when its state changes.
- [var contentView: UIView](uitableviewcell/contentview.md)
  The content view of the cell object.
### Managing the state
- [var configurationState: UICellConfigurationState](uitableviewcell/configurationstate-4xwj0.md)
  The current configuration state of the cell.
- [func setNeedsUpdateConfiguration()](uitableviewcell/setneedsupdateconfiguration.md)
  Informs the cell to update its configuration for its current state.
- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
- [UITableViewCell.ConfigurationUpdateHandler](uitableviewcell/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the cell’s configuration using the current state.
### Managing accessory views
- [var accessoryType: UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.property.md)
  The type of standard accessory view for the cell to use in the table view’s normal state.
- [var accessoryView: UIView?](uitableviewcell/accessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s normal state.
- [var editingAccessoryType: UITableViewCell.AccessoryType](uitableviewcell/editingaccessorytype.md)
  The type of standard accessory view for the cell to use in the table view’s editing state.
- [var editingAccessoryView: UIView?](uitableviewcell/editingaccessoryview.md)
  The view to use on the right side of the cell, typically as a control, in the table view’s editing state.
- [UITableViewCell.AccessoryType](uitableviewcell/accessorytype-swift.enum.md)
  The type of standard accessory control used by a cell.
### Managing cell selection and highlighting
- [var selectionStyle: UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.property.md)
  The style of selection for a cell.
- [UITableViewCell.SelectionStyle](uitableviewcell/selectionstyle-swift.enum.md)
  The style of selected cells.
- [var isSelected: Bool](uitableviewcell/isselected.md)
  A Boolean value that indicates whether the cell is selected.
- [func setSelected(Bool, animated: Bool)](uitableviewcell/setselected(_:animated:).md)
  Sets the selected state of the cell, optionally animating the transition between states.
- [var isHighlighted: Bool](uitableviewcell/ishighlighted.md)
  A Boolean value that indicates whether the cell is highlighted.
- [func setHighlighted(Bool, animated: Bool)](uitableviewcell/sethighlighted(_:animated:).md)
  Sets the highlighted state of the cell, optionally animating the transition between states.
### Editing the cell
- [var isEditing: Bool](uitableviewcell/isediting.md)
  A Boolean value that indicates whether the cell is in an editable state.
- [func setEditing(Bool, animated: Bool)](uitableviewcell/setediting(_:animated:).md)
  Toggles the cell into and out of editing mode.
- [var editingStyle: UITableViewCell.EditingStyle](uitableviewcell/editingstyle-swift.property.md)
  The editing style of the cell.
- [UITableViewCell.EditingStyle](uitableviewcell/editingstyle-swift.enum.md)
  The editing control used by a cell.
- [var showingDeleteConfirmation: Bool](uitableviewcell/showingdeleteconfirmation.md)
  A Boolean value that indicates whether the cell is currently showing the delete-confirmation button.
- [var showsReorderControl: Bool](uitableviewcell/showsreordercontrol.md)
  A Boolean value that determines whether the cell shows the reordering control.
### Dragging the row
- [var userInteractionEnabledWhileDragging: Bool](uitableviewcell/userinteractionenabledwhiledragging.md)
  A Boolean value indicating whether users can interact with a cell while it is being dragged.
- [func dragStateDidChange(UITableViewCell.DragState)](uitableviewcell/dragstatedidchange(_:).md)
  Notifies the cell that its drag status changed.
- [UITableViewCell.DragState](uitableviewcell/dragstate.md)
  Constants indicating the current state of a row involved in a drag operation.
### Adjusting to state transitions
- [func willTransition(to: UITableViewCell.StateMask)](uitableviewcell/willtransition(to:).md)
  Notifies the cell that it’s about to transition to a new cell state.
- [func didTransition(to: UITableViewCell.StateMask)](uitableviewcell/didtransition(to:).md)
  Notifies the cell that it transitioned to a new cell state.
- [UITableViewCell.StateMask](uitableviewcell/statemask.md)
  Constants used to determine the new state of a cell as it transitions between states.
### Managing content indentation
- [var indentationLevel: Int](uitableviewcell/indentationlevel.md)
  The indentation level of the cell’s content.
- [var indentationWidth: CGFloat](uitableviewcell/indentationwidth.md)
  The width for each level of indentation of a cell’s content.
- [var shouldIndentWhileEditing: Bool](uitableviewcell/shouldindentwhileediting.md)
  A Boolean value that controls whether the cell background is indented when the table view is in editing mode.
- [var separatorInset: UIEdgeInsets](uitableviewcell/separatorinset.md)
  The inset values for the separator line drawn beneath the cell.
- [UITableViewCell.SeparatorStyle](uitableviewcell/separatorstyle.md)
  The style for cells to use as separators.
### Managing focus
- [var focusStyle: UITableViewCell.FocusStyle](uitableviewcell/focusstyle-swift.property.md)
  The appearance of the cell when focused.
- [UITableViewCell.FocusStyle](uitableviewcell/focusstyle-swift.enum.md)
  The style of focused cells.
### Deprecated
- [var textLabel: UILabel?](uitableviewcell/textlabel.md)
  The label to use for the main textual content of the table cell.
- [var detailTextLabel: UILabel?](uitableviewcell/detailtextlabel.md)
  The secondary label of the table cell, if one exists.
- [var imageView: UIImageView?](uitableviewcell/imageview.md)
  The image view of the table cell.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md)
  Specify the appearance and content of your table’s rows by defining one or more prototype cells in your storyboard.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)
  Differentiate groups of rows visually by adding header and footer views to your table view’s sections.
- [class UITableViewHeaderFooterView](uitableviewheaderfooterview.md)
  A reusable view that you place at the top or bottom of a table section to display additional information for that section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewcell)*