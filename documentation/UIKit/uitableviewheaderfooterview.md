# UITableViewHeaderFooterView

**Framework**: UIKit  
**Kind**: class

A reusable view that you place at the top or bottom of a table section to display additional information for that section.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UITableViewHeaderFooterView
```

## Mentions

- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md)

#### Overview

Use [`UITableViewHeaderFooterView`](uitableviewheaderfooterview.md) objects to manage the header and footer content of your table’s sections efficiently. A header-footer view is a reusable view that you can subclass or use as is. To configure the content and appearance of a header-footer view, you can set its [`contentConfiguration`](uitableviewheaderfooterview/contentconfiguration-6b4eg.md) and [`backgroundConfiguration`](uitableviewheaderfooterview/backgroundconfiguration-52wng.md).

To promote the reuse of your header-footer views, register them by calling the [`register(_:forHeaderFooterViewReuseIdentifier:)`](uitableview/register(_:forheaderfooterviewreuseidentifier:)-20ybb.md) or [`register(_:forHeaderFooterViewReuseIdentifier:)`](uitableview/register(_:forheaderfooterviewreuseidentifier:)-1rgvc.md) method of the table view. In the [`tableView(_:viewForHeaderInSection:)`](uitableviewdelegate/tableview(_:viewforheaderinsection:).md) or [`tableView(_:viewForFooterInSection:)`](uitableviewdelegate/tableview(_:viewforfooterinsection:).md) method of your delegate object, call the table view’s [`dequeueReusableHeaderFooterView(withIdentifier:)`](uitableview/dequeuereusableheaderfooterview(withidentifier:).md) method to create your view. That method returns a recycled view (if one is available) or creates a new view using the information you registered.

A simple alternative to creating custom header-footer views is to implement the [`tableView(_:titleForHeaderInSection:)`](uitableviewdatasource/tableview(_:titleforheaderinsection:).md) and [`tableView(_:titleForFooterInSection:)`](uitableviewdatasource/tableview(_:titleforfooterinsection:).md) methods of your data source object. When you implement those methods, the table view creates a standard header or footer view and displays the text you supply.

## Topics

### Creating the view
- [init(reuseIdentifier: String?)](uitableviewheaderfooterview/init(reuseidentifier:).md)
  Initializes a header-footer view with the specified reuse identifier.
- [init?(coder: NSCoder)](uitableviewheaderfooterview/init(coder:).md)
  Creates a header-footer view from data in an unarchiver.
### Managing view reuse
- [var reuseIdentifier: String?](uitableviewheaderfooterview/reuseidentifier.md)
  A string used to identify a reusable header or footer.
- [func prepareForReuse()](uitableviewheaderfooterview/prepareforreuse.md)
  Prepares a reusable header or footer view for reuse by the table.
### Configuring the background
- [func defaultBackgroundConfiguration() -> UIBackgroundConfiguration](uitableviewheaderfooterview/defaultbackgroundconfiguration.md)
  Retrieves a background configuration with system default values.
- [var backgroundConfiguration: UIBackgroundConfiguration?](uitableviewheaderfooterview/backgroundconfiguration-52wng.md)
  The current background configuration of the view.
- [var automaticallyUpdatesBackgroundConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration.md)
  A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [var backgroundView: UIView?](uitableviewheaderfooterview/backgroundview.md)
  The background view of the header or footer.
### Managing the content
- [func defaultContentConfiguration() -> UIListContentConfiguration](uitableviewheaderfooterview/defaultcontentconfiguration.md)
  Retrieves a default list content configuration for the view’s style.
- [var contentConfiguration: (any UIContentConfiguration)?](uitableviewheaderfooterview/contentconfiguration-6b4eg.md)
  The current content configuration of the view.
- [var automaticallyUpdatesContentConfiguration: Bool](uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.md)
  A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [var contentView: UIView](uitableviewheaderfooterview/contentview.md)
  The content view of the header or footer.
### Managing the state
- [var configurationState: UIViewConfigurationState](uitableviewheaderfooterview/configurationstate-7xj7r.md)
  The current configuration state of the view.
- [func setNeedsUpdateConfiguration()](uitableviewheaderfooterview/setneedsupdateconfiguration.md)
  Informs the view to update its configuration for its current state.
- [func updateConfiguration(using: UIViewConfigurationState)](uitableviewheaderfooterview/updateconfiguration(using:).md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.
- [UITableViewHeaderFooterView.ConfigurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-swift.typealias.md)
  The type of block for handling updates to the view’s configuration using the current state.
### Deprecated
- [var textLabel: UILabel?](uitableviewheaderfooterview/textlabel.md)
  A primary text label for the view.
- [var detailTextLabel: UILabel?](uitableviewheaderfooterview/detailtextlabel.md)
  A detail text label for the view.

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
- [class UITableViewCell](uitableviewcell.md)
  The visual representation of a single row in a table view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview)*