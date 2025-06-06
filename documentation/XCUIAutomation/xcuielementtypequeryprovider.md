# XCUIElementTypeQueryProvider

**Framework**: Xcuiautomation  
**Kind**: protocol

A type that provides ready-made queries for locating descendant UI elements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
protocol XCUIElementTypeQueryProvider
```

#### Overview

Accessing the properties to get queries for descendant elements on an instance of a conforming class (such as an [`XCUIElement`](xcuielement.md) or [`XCUIElementQuery`](xcuielementquery.md) instance) is equivalent to calling [`descendants(matching:)`](xcuielementquery/descendants(matching:).md) for the corresponding element type.

## Topics

### Finding the first matching element
- [var firstMatch: XCUIElement](xcuielementtypequeryprovider/firstmatch.md)
  The first element that matches the query.
### Querying descendant elements
- [var activityIndicators: XCUIElementQuery](xcuielementtypequeryprovider/activityindicators.md)
  A query that matches activity-indicator view elements.
- [var alerts: XCUIElementQuery](xcuielementtypequeryprovider/alerts.md)
  A query that matches alert view elements.
- [var browsers: XCUIElementQuery](xcuielementtypequeryprovider/browsers.md)
  A query that matches browser elements.
- [var buttons: XCUIElementQuery](xcuielementtypequeryprovider/buttons.md)
  A query that matches button control elements.
- [var cells: XCUIElementQuery](xcuielementtypequeryprovider/cells.md)
  A query that matches cell elements.
- [var checkBoxes: XCUIElementQuery](xcuielementtypequeryprovider/checkboxes.md)
  A query that matches checkbox control elements.
- [var collectionViews: XCUIElementQuery](xcuielementtypequeryprovider/collectionviews.md)
  A query that matches collection view elements.
- [var colorWells: XCUIElementQuery](xcuielementtypequeryprovider/colorwells.md)
  A query that matches color-well elements.
- [var comboBoxes: XCUIElementQuery](xcuielementtypequeryprovider/comboboxes.md)
  A query that matches combo-box control elements.
- [var datePickers: XCUIElementQuery](xcuielementtypequeryprovider/datepickers.md)
  A query that matches date-picker control elements.
- [var decrementArrows: XCUIElementQuery](xcuielementtypequeryprovider/decrementarrows.md)
  A query that matches decrement-arrow control elements.
- [var dialogs: XCUIElementQuery](xcuielementtypequeryprovider/dialogs.md)
  A query that matches dialog view elements.
- [var disclosureTriangles: XCUIElementQuery](xcuielementtypequeryprovider/disclosuretriangles.md)
  A query that matches disclosure-triangle control elements.
- [var disclosedChildRows: XCUIElementQuery](xcuielementtypequeryprovider/disclosedchildrows.md)
  A query that matches disclosed child row elements.
- [var dockItems: XCUIElementQuery](xcuielementtypequeryprovider/dockitems.md)
  A query that matches dock-item control elements.
- [var drawers: XCUIElementQuery](xcuielementtypequeryprovider/drawers.md)
  A query that matches drawer elements.
- [var grids: XCUIElementQuery](xcuielementtypequeryprovider/grids.md)
  A query that matches grid view elements.
- [var groups: XCUIElementQuery](xcuielementtypequeryprovider/groups.md)
  A query that matches group elements.
- [var handles: XCUIElementQuery](xcuielementtypequeryprovider/handles.md)
  A query that matches handle control elements.
- [var helpTags: XCUIElementQuery](xcuielementtypequeryprovider/helptags.md)
  A query that matches help-tag elements.
- [var icons: XCUIElementQuery](xcuielementtypequeryprovider/icons.md)
  A query that matches icon elements.
- [var images: XCUIElementQuery](xcuielementtypequeryprovider/images.md)
  A query that matches image-view elements.
- [var incrementArrows: XCUIElementQuery](xcuielementtypequeryprovider/incrementarrows.md)
  A query that matches increment-arrow control elements.
- [var keyboards: XCUIElementQuery](xcuielementtypequeryprovider/keyboards.md)
  A query that matches keyboard elements.
- [var keys: XCUIElementQuery](xcuielementtypequeryprovider/keys.md)
  A query that matches key elements.
- [var layoutAreas: XCUIElementQuery](xcuielementtypequeryprovider/layoutareas.md)
  A query that matches layout-area elements.
- [var layoutItems: XCUIElementQuery](xcuielementtypequeryprovider/layoutitems.md)
  A query that matches layout-item elements.
- [var levelIndicators: XCUIElementQuery](xcuielementtypequeryprovider/levelindicators.md)
  A query that matches level-indicator elements.
- [var links: XCUIElementQuery](xcuielementtypequeryprovider/links.md)
  A query that matches link elements.
- [var maps: XCUIElementQuery](xcuielementtypequeryprovider/maps.md)
  A query that matches map-view elements.
- [var mattes: XCUIElementQuery](xcuielementtypequeryprovider/mattes.md)
  A query that matches matte elements.
- [var menuBarItems: XCUIElementQuery](xcuielementtypequeryprovider/menubaritems.md)
  A query that matches menu bar item elements.
- [var menuBars: XCUIElementQuery](xcuielementtypequeryprovider/menubars.md)
  A query that matches menu bar elements.
- [var menuButtons: XCUIElementQuery](xcuielementtypequeryprovider/menubuttons.md)
  A query that matches menu button elements.
- [var menuItems: XCUIElementQuery](xcuielementtypequeryprovider/menuitems.md)
  A query that matches menu item elements.
- [var menus: XCUIElementQuery](xcuielementtypequeryprovider/menus.md)
  A query that matches menu elements.
- [var navigationBars: XCUIElementQuery](xcuielementtypequeryprovider/navigationbars.md)
  A query that matches navigation bar elements.
- [var otherElements: XCUIElementQuery](xcuielementtypequeryprovider/otherelements.md)
  A query that matches other view or control elements.
- [var outlineRows: XCUIElementQuery](xcuielementtypequeryprovider/outlinerows.md)
  A query that matches outline row elements.
- [var outlines: XCUIElementQuery](xcuielementtypequeryprovider/outlines.md)
  A query that matches outline view elements.
- [var pageIndicators: XCUIElementQuery](xcuielementtypequeryprovider/pageindicators.md)
  A query that matches page-indicator control elements.
- [var pickerWheels: XCUIElementQuery](xcuielementtypequeryprovider/pickerwheels.md)
  A query that matches picker-wheel control elements.
- [var pickers: XCUIElementQuery](xcuielementtypequeryprovider/pickers.md)
  A query that matches picker control elements.
- [var popUpButtons: XCUIElementQuery](xcuielementtypequeryprovider/popupbuttons.md)
  A query that matches popup-button control elements.
- [var popovers: XCUIElementQuery](xcuielementtypequeryprovider/popovers.md)
  A query that matches popover view elements.
- [var progressIndicators: XCUIElementQuery](xcuielementtypequeryprovider/progressindicators.md)
  A query that matches progress-indicator control elements.
- [var radioButtons: XCUIElementQuery](xcuielementtypequeryprovider/radiobuttons.md)
  A query that matches radio-button control elements.
- [var radioGroups: XCUIElementQuery](xcuielementtypequeryprovider/radiogroups.md)
  A query that matches radio group elements.
- [var ratingIndicators: XCUIElementQuery](xcuielementtypequeryprovider/ratingindicators.md)
  A query that matches rating-indicator view elements.
- [var relevanceIndicators: XCUIElementQuery](xcuielementtypequeryprovider/relevanceindicators.md)
  A query that matches relevance-indicator view elements.
- [var rulerMarkers: XCUIElementQuery](xcuielementtypequeryprovider/rulermarkers.md)
  A query that matches ruler marker elements.
- [var rulers: XCUIElementQuery](xcuielementtypequeryprovider/rulers.md)
  A query that matches ruler view elements.
- [var scrollBars: XCUIElementQuery](xcuielementtypequeryprovider/scrollbars.md)
  A query that matches scroll bar elements.
- [var scrollViews: XCUIElementQuery](xcuielementtypequeryprovider/scrollviews.md)
  A query that matches scroll view elements.
- [var searchFields: XCUIElementQuery](xcuielementtypequeryprovider/searchfields.md)
  A query that matches search field elements.
- [var secureTextFields: XCUIElementQuery](xcuielementtypequeryprovider/securetextfields.md)
  A query that matches secure text field elements.
- [var segmentedControls: XCUIElementQuery](xcuielementtypequeryprovider/segmentedcontrols.md)
  A query that matches segmented control elements.
- [var sheets: XCUIElementQuery](xcuielementtypequeryprovider/sheets.md)
  A query that matches sheet elements.
- [var sliders: XCUIElementQuery](xcuielementtypequeryprovider/sliders.md)
  A query that matches slider elements.
- [var splitGroups: XCUIElementQuery](xcuielementtypequeryprovider/splitgroups.md)
  A query that matches split group elements.
- [var splitters: XCUIElementQuery](xcuielementtypequeryprovider/splitters.md)
  A query that matches splitter elements.
- [var staticTexts: XCUIElementQuery](xcuielementtypequeryprovider/statictexts.md)
  A query that matches static-text view elements.
- [var statusBars: XCUIElementQuery](xcuielementtypequeryprovider/statusbars.md)
  A query that matches status bar elements.
- [var statusItems: XCUIElementQuery](xcuielementtypequeryprovider/statusitems.md)
  A query that matches status item elements.
- [var steppers: XCUIElementQuery](xcuielementtypequeryprovider/steppers.md)
  A query that matches stepper elements.
- [var switches: XCUIElementQuery](xcuielementtypequeryprovider/switches.md)
  A query that matches switch control elements.
- [var tabBars: XCUIElementQuery](xcuielementtypequeryprovider/tabbars.md)
  A query that matches tab bar elements.
- [var tabGroups: XCUIElementQuery](xcuielementtypequeryprovider/tabgroups.md)
  A query that matches tab group elements.
- [var tableColumns: XCUIElementQuery](xcuielementtypequeryprovider/tablecolumns.md)
  A query that matches table column elements.
- [var tableRows: XCUIElementQuery](xcuielementtypequeryprovider/tablerows.md)
  A query that matches table row elements.
- [var tables: XCUIElementQuery](xcuielementtypequeryprovider/tables.md)
  A query that matches table elements.
- [var tabs: XCUIElementQuery](xcuielementtypequeryprovider/tabs.md)
  A query that matches tab elements.
- [var textFields: XCUIElementQuery](xcuielementtypequeryprovider/textfields.md)
  A query that matches text field elements.
- [var textViews: XCUIElementQuery](xcuielementtypequeryprovider/textviews.md)
  A query that matches text view elements.
- [var timelines: XCUIElementQuery](xcuielementtypequeryprovider/timelines.md)
  A query that matches timeline view elements.
- [var toggles: XCUIElementQuery](xcuielementtypequeryprovider/toggles.md)
  A query that matches toggle control elements.
- [var toolbarButtons: XCUIElementQuery](xcuielementtypequeryprovider/toolbarbuttons.md)
  A query that matches toolbar button elements.
- [var toolbars: XCUIElementQuery](xcuielementtypequeryprovider/toolbars.md)
  A query that matches toolbar elements.
- [var touchBars: XCUIElementQuery](xcuielementtypequeryprovider/touchbars.md)
  A query that matches touch bar elements.
- [var valueIndicators: XCUIElementQuery](xcuielementtypequeryprovider/valueindicators.md)
  A query that matches value indicator elements.
- [var webViews: XCUIElementQuery](xcuielementtypequeryprovider/webviews.md)
  A query that matches web view elements.
- [var windows: XCUIElementQuery](xcuielementtypequeryprovider/windows.md)
  A query that matches window elements.

## Relationships

### Conforming Types
- [XCUIApplication](xcuiapplication.md)
- [XCUIElement](xcuielement.md)
- [XCUIElementQuery](xcuielementquery.md)
- [XCUISiriService](xcuisiriservice.md)

## See Also

- [class XCUIElementQuery](xcuielementquery.md)
  An object that defines the search criteria a test uses to identify UI elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuielementtypequeryprovider)*