# AppKit Release Notes for macOS Ventura 13

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

AppKit in macOS Ventura 13 includes new features, as well as API changes and deprecations.

### New Features

#### NSColorWell

- Color wells have a modernized appearance and two new styles in macOS 13. See the new [`colorWellStyle`](../AppKit/nscolorwell/colorwellstyle.md) property and associated [`NSColorWell.Style`](../AppKit/nscolorwell/style.md) type for more information on configuring a color well’s style.
- The two new color well styles, [`NSColorWell.Style.minimal`](../AppKit/nscolorwell/style/minimal.md) and [`NSColorWell.Style.expanded`](../AppKit/nscolorwell/style/expanded.md), offer a pull-down capability. By default, interacting with the well displays a popover with a palette of color choices for quick picking. Applications can customize this interaction using the new [`pulldownTarget`](../AppKit/nscolorwell/pulldowntarget.md) and [`pulldownAction`](../AppKit/nscolorwell/pulldownaction.md) properties.
- Borderless color wells will be deprecated in a future release. The [`isBordered`](../AppKit/nscolorwell/isbordered.md) property has been annotated as such.

#### NSComboButton

- macOS 13 introduces a new type of control: [`NSComboButton`](../AppKit/nscombobutton.md). NSComboButton provides the functionality of a pull-down menu along with a primary action.
- NSComboButton is configurable with two styles, [`NSComboButton.Style.split`](../AppKit/nscombobutton/style-swift.enum/split.md) and [`NSComboButton.Style.unified`](../AppKit/nscombobutton/style-swift.enum/unified.md). Refer to the class documentation for guidance on the appearance and behavior of each case.

#### NSNib

- The `initWithContentsOfURL` initializer (deprecated since 10.8) now throws an assertion. Use [`init(nibNamed:bundle:)`](../AppKit/nsnib/init%28nibnamed,bundle%29.md) instead.

#### NSTableView and NSOutlineView

- On macOS 13 and higher, changing the [`autosaveName`](../AppKit/nstableview/autosavename-swift.property.md) property from one value to another will automatically persist autosave data for the old value before changing to the new value. Setting `autosaveName` to `nil` removes the persistence data for the previously set `autosaveName`.
- NSTableView and NSOutlineView now automatically estimate row heights for view-based table views whose delegates implement [`tableView(_:heightOfRow:)`](../AppKit/nstableviewdelegate/tableview%28_,heightofrow%29.md) and provide variable row heights. This provides performance improvements for table views with large numbers of rows by reducing the frequency of the calls to [`tableView(_:heightOfRow:)`](../AppKit/nstableviewdelegate/tableview%28_,heightofrow%29.md).

> **Note**: To get the benefit of row height estimation, the table view must be view-based and not override [`rect(ofRow:)`](../AppKit/nstableview/rect%28ofrow%29.md), [`row(at:)`](../AppKit/nstableview/row%28at%29.md), or [`rows(in:)`](../AppKit/nstableview/rows%28in%29.md).

- For cell-based table views, checking Autosave Column Information in Interface Builder now correctly persists column information for columns that have automatic column identifiers.
- For apps linked against the macOS 13 SDK, [`NSTableRowView`](../AppKit/nstablerowview.md) and subclasses that override [`drawSeparator(in:)`](../AppKit/nstablerowview/drawseparator%28in%29.md) now draw their separators correctly, even when displayed as floating group rows.

### Deprecations

#### NSToolbar

- Placing an NSToolbarItem item taller than the toolbar height is not supported and will result in clipping. When drawing a custom badge, use alignmentRectInsets of the control to describe where the button is and draw within the inset area.

## See Also

### AppKit
- [AppKit Release Notes for macOS Sonoma 14](./appkit-release-notes-for-macos-14.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Monterey 12](./appkit-release-notes-for-macos-12.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Big Sur 11](./appkit-release-notes-for-macos-11.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS 10.14](./appkit-release-notes-for-macos-10_14.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/appkit-release-notes-for-macos-13)*