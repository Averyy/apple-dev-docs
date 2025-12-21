# AppKit Release Notes for macOS Ventura 13

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

AppKit in macOS Ventura 13 includes new features, as well as API changes and deprecations.

##### New Features

###### Nscolorwell

- Color wells have a modernized appearance and two new styles in macOS 13. See the new [`colorWellStyle`](https://developer.apple.com/documentation/AppKit/NSColorWell/colorWellStyle) property and associated [`NSColorWell.Style`](https://developer.apple.com/documentation/AppKit/NSColorWell/Style) type for more information on configuring a color well’s style.
- The two new color well styles, [`NSColorWell.Style.minimal`](https://developer.apple.com/documentation/AppKit/NSColorWell/Style/minimal) and [`NSColorWell.Style.expanded`](https://developer.apple.com/documentation/AppKit/NSColorWell/Style/expanded), offer a pull-down capability. By default, interacting with the well displays a popover with a palette of color choices for quick picking. Applications can customize this interaction using the new [`pulldownTarget`](https://developer.apple.com/documentation/AppKit/NSColorWell/pulldownTarget) and [`pulldownAction`](https://developer.apple.com/documentation/AppKit/NSColorWell/pulldownAction) properties.
- Borderless color wells will be deprecated in a future release. The [`isBordered`](https://developer.apple.com/documentation/AppKit/NSColorWell/isBordered) property has been annotated as such.

###### Nscombobutton

- macOS 13 introduces a new type of control: [`NSComboButton`](https://developer.apple.com/documentation/AppKit/NSComboButton). NSComboButton provides the functionality of a pull-down menu along with a primary action.
- NSComboButton is configurable with two styles, [`NSComboButton.Style.split`](https://developer.apple.com/documentation/AppKit/NSComboButton/Style-swift.enum/split) and [`NSComboButton.Style.unified`](https://developer.apple.com/documentation/AppKit/NSComboButton/Style-swift.enum/unified). Refer to the class documentation for guidance on the appearance and behavior of each case.

###### Nsnib

- The `initWithContentsOfURL` initializer (deprecated since 10.8) now throws an assertion. Use [`init(nibNamed:bundle:)`](https://developer.apple.com/documentation/AppKit/NSNib/init(nibNamed:bundle:)) instead.

###### Nstableview and Nsoutlineview

- On macOS 13 and higher, changing the [`autosaveName`](https://developer.apple.com/documentation/AppKit/NSTableView/autosaveName-swift.property) property from one value to another will automatically persist autosave data for the old value before changing to the new value. Setting `autosaveName` to `nil` removes the persistence data for the previously set `autosaveName`.
- NSTableView and NSOutlineView now automatically estimate row heights for view-based table views whose delegates implement [`tableView(_:heightOfRow:)`](https://developer.apple.com/documentation/AppKit/NSTableViewDelegate/tableView(_:heightOfRow:)) and provide variable row heights. This provides performance improvements for table views with large numbers of rows by reducing the frequency of the calls to [`tableView(_:heightOfRow:)`](https://developer.apple.com/documentation/AppKit/NSTableViewDelegate/tableView(_:heightOfRow:)).

> **Note**: To get the benefit of row height estimation, the table view must be view-based and not override [`rect(ofRow:)`](https://developer.apple.com/documentation/AppKit/NSTableView/rect(ofRow:)), [`row(at:)`](https://developer.apple.com/documentation/AppKit/NSTableView/row(at:)), or [`rows(in:)`](https://developer.apple.com/documentation/AppKit/NSTableView/rows(in:)).

- For cell-based table views, checking Autosave Column Information in Interface Builder now correctly persists column information for columns that have automatic column identifiers.
- For apps linked against the macOS 13 SDK, [`NSTableRowView`](https://developer.apple.com/documentation/AppKit/NSTableRowView) and subclasses that override [`drawSeparator(in:)`](https://developer.apple.com/documentation/AppKit/NSTableRowView/drawSeparator(in:)) now draw their separators correctly, even when displayed as floating group rows.

##### Deprecations

###### Nstoolbar

- Placing an NSToolbarItem item taller than the toolbar height is not supported and will result in clipping. When drawing a custom badge, use alignmentRectInsets of the control to describe where the button is and draw within the inset area.

## See Also

- [AppKit Release Notes for macOS Sonoma 14](appkit-release-notes-for-macos-14.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Monterey 12](appkit-release-notes-for-macos-12.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Big Sur 11](appkit-release-notes-for-macos-11.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS 10.14](appkit-release-notes-for-macos-10_14.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/appkit-release-notes-for-macos-13)*