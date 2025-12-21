# AppKit Release Notes for macOS Monterey 12

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

AppKit in macOS Monterey 12 includes new features, as well as API changes and deprecations.

##### New Features

###### Nsbutton

- Buttons no longer highlight using the accent color when clicked. Before using any subclass that performs custom drawing, inspect the button cell’s `interiorBackgroundStyle` property to determine if the bezel draws in a normal or emphasized state.
- Buttons now support custom tinting with the [`bezelColor`](https://developer.apple.com/documentation/AppKit/NSButton/bezelColor) property. This property — previously applied only in the Touch Bar — now functions for all in-window buttons using the `NSButtonTypeMomentaryPushIn` style.

###### Nsslider

- When clicking on the track, for linear sliders, circular sliders, or dial, the slider now animates to the new value.
- You can now tint sliders with colorful track fills using the [`trackFillColor`](https://developer.apple.com/documentation/AppKit/NSSlider/trackFillColor) property. This property now functions for all in-window sliders.

###### Nssegmentedcontrol

- Segmented controls now support custom tinting via the [`selectedSegmentBezelColor`](https://developer.apple.com/documentation/AppKit/NSSegmentedControl/selectedSegmentBezelColor) property. This property now functions for all in-window segmented control styles that draw colorful selected segments.

###### Nspopover

- [`NSPopover`](https://developer.apple.com/documentation/AppKit/NSPopover) has a new animation when appearing and dismissing.

###### Symbol Images

- SF Symbols now support layered symbol images. Layered symbol images use an updated data format to annotate each path element of the symbol with a level in a hierarchy: primary, secondary, tertiary, and so on. At draw time, AppKit can assign different colors to each layer of the symbol using new APIs on [`NSImage.SymbolConfiguration`](https://developer.apple.com/documentation/AppKit/NSImage/SymbolConfiguration-swift.class). Many system-provided symbol images redesigned to include layered versions.
- [`NSImage.SymbolConfiguration`](https://developer.apple.com/documentation/AppKit/NSImage/SymbolConfiguration-swift.class) now supports merging two configurations with [`applying(_:)`](https://developer.apple.com/documentation/UIKit/UIImage/Configuration-swift.class/applying(_:)) method.
- [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) now includes a read-only property, [`NSImage.SymbolConfiguration`](https://developer.apple.com/documentation/AppKit/NSImage/SymbolConfiguration-swift.class), for its current symbol configuration. You can use this property to configure other symbol images to match a reference image, or to merge an image’s existing configuration with a set of new configuration options.

###### Restorable State

- To enable secure coding for a restorable state, implement [`applicationSupportsSecureRestorableState(_:)`](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/applicationSupportsSecureRestorableState(_:)). When opted in: - The system requires classes passed to [`restorationClass`](https://developer.apple.com/documentation/AppKit/NSWindow/restorationClass) to explicitly conform to [`NSWindowRestoration`](https://developer.apple.com/documentation/AppKit/NSWindowRestoration).
- Set [`requiresSecureCoding`](https://developer.apple.com/documentation/Foundation/NSCoder/requiresSecureCoding) to `true` and the [`decodingFailurePolicy`](https://developer.apple.com/documentation/Foundation/NSCoder/decodingFailurePolicy-swift.property) to [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](https://developer.apple.com/documentation/Foundation/NSCoder/DecodingFailurePolicy-swift.enum/setErrorAndReturn) for any coder the following implementations or overrides use [`decodingFailurePolicy`](https://developer.apple.com/documentation/Foundation/NSCoder/decodingFailurePolicy-swift.property) set to [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](https://developer.apple.com/documentation/Foundation/NSCoder/DecodingFailurePolicy-swift.enum/setErrorAndReturn): - [`restoreWindow(withIdentifier:state:completionHandler:)`](https://developer.apple.com/documentation/AppKit/NSWindowRestoration/restoreWindow(withIdentifier:state:completionHandler:))
- [`restoreWindow(withIdentifier:state:completionHandler:)`](https://developer.apple.com/documentation/AppKit/NSApplication/restoreWindow(withIdentifier:state:completionHandler:))
- [`encodeRestorableState(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/encodeRestorableState(with:))
- [`encodeRestorableState(with:backgroundQueue:)`](https://developer.apple.com/documentation/AppKit/NSResponder/encodeRestorableState(with:backgroundQueue:))
- [`restoreState(with:)`](https://developer.apple.com/documentation/AppKit/NSResponder/restoreState(with:))
- [`restoreWindow(withIdentifier:state:completionHandler:)`](https://developer.apple.com/documentation/AppKit/NSDocument/restoreWindow(withIdentifier:state:completionHandler:))
- [`encodeRestorableState(with:)`](https://developer.apple.com/documentation/AppKit/NSDocument/encodeRestorableState(with:))
- [`encodeRestorableState(with:backgroundQueue:)`](https://developer.apple.com/documentation/AppKit/NSDocument/encodeRestorableState(with:backgroundQueue:))
- [`restoreState(with:)`](https://developer.apple.com/documentation/AppKit/NSDocument/restoreState(with:))
- Additionally, [`restorableStateKeyPaths`](https://developer.apple.com/documentation/AppKit/NSDocument/restorableStateKeyPaths) must only point at `NSSecureCoding`-compliant values and you need to implement [`allowedClasses(forRestorableStateKeyPath:)`](https://developer.apple.com/documentation/AppKit/NSDocument/allowedClasses(forRestorableStateKeyPath:)) to specify the type of the object.

###### Nsmenu

- The new user preference “Automatically hide and show the menu bar in full screen” in Dock & Menu Bar preferences is enabled by default. In macOS Monterey 12, the user can choose to disable this setting to always show the menu bar in full screen spaces. Standard full screen windows are resized to fit below the menu bar. Some apps assume a full screen-sized window, and don’t work well with this setting.

###### Nstableview

- 20-point spacing precedes each group row to make the separation between sections more visible. Source lists have a similar, but smaller, 13-point spacing. This applies to the [`NSTableView.Style.inset`](https://developer.apple.com/documentation/AppKit/NSTableView/Style-swift.enum/inset) and [`NSTableView.Style.fullWidth`](https://developer.apple.com/documentation/AppKit/NSTableView/Style-swift.enum/fullWidth) effective styles in apps linked against the macOS 12 SDK. [`NSTableView.Style.plain`](https://developer.apple.com/documentation/AppKit/NSTableView/Style-swift.enum/plain) doesn’t display the spacing.
- The floating group row transition — previously a push transition — instantly replaces the new floating group row. It occurs when the `x-height` of the group row’s label meets the bottom of a currently floating group row.

###### Nsoutlineview

- The disclosure button now aligns with the cell view’s [`firstBaselineOffsetFromTop`](https://developer.apple.com/documentation/AppKit/NSView/firstBaselineOffsetFromTop). The system overrides it in [`NSTableCellView`](https://developer.apple.com/documentation/AppKit/NSTableCellView) so it matches the baseline of its [`textField`](https://developer.apple.com/documentation/AppKit/NSTableCellView/textField) (assuming `textfield` sets the baseline). Overriding the property and returning `0` reverts to the previous behavior.
- When collapsing several items, the [`selectionDidChangeNotification`](https://developer.apple.com/documentation/AppKit/NSOutlineView/selectionDidChangeNotification) only posts once. Previously, it posted once per collapsed item.

###### Nsopenpanel

- Setting [`canChooseFiles`](https://developer.apple.com/documentation/AppKit/NSOpenPanel/canChooseFiles) to `false` automatically disabled files, but all of the directory contents were sent to [`panel(_:shouldEnable:)`](https://developer.apple.com/documentation/AppKit/NSOpenSavePanelDelegate/panel(_:shouldEnable:)) or [`panel:shouldShowFilename:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/panel:shouldShowFilename:). In macOS Monterey 12, files aren’t sent to the delegate methods unless `canChooseFiles` is `true`. In addition, file packages are excluded unless `treatsFilePackagesAsDirectoriesis` is `true`. This change allows optimization in the delegate method.

###### Textkit 2

- TextKit 2 introduces a new text layout engine and its associated API. You can use TextKit 2  alongside the existing [`TextKit`](https://developer.apple.com/documentation/AppKit/textkit) API.
- [`NSTextContentStorage`](https://developer.apple.com/documentation/UIKit/NSTextContentStorage) and [`NSTextLayoutManager`](https://developer.apple.com/documentation/UIKit/NSTextLayoutManager) are the two main controller objects superseding [`NSTextStorage`](https://developer.apple.com/documentation/AppKit/NSTextStorage) and [`NSLayoutManager`](https://developer.apple.com/documentation/AppKit/NSLayoutManager) respectively. [`NSTextParagraph`](https://developer.apple.com/documentation/UIKit/NSTextParagraph) managed by `NSTextContentStorage` represents a paragraph of text. `NSTextLayoutManager` stores the layout information in its model objects: [`NSTextLayoutFragment`](https://developer.apple.com/documentation/UIKit/NSTextLayoutFragment) and [`NSTextLineFragment`](https://developer.apple.com/documentation/UIKit/NSTextLineFragment).
- In TextKit 2, [`NSTextSelection`](https://developer.apple.com/documentation/UIKit/NSTextSelection) encapsulates information associated with a text selection while [`NSTextSelectionNavigation`](https://developer.apple.com/documentation/UIKit/NSTextSelectionNavigation) manipulates and converts the selection object based on keyboard and mouse navigation actions.

## See Also

- [AppKit Release Notes for macOS Sonoma 14](appkit-release-notes-for-macos-14.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Ventura 13](appkit-release-notes-for-macos-13.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Big Sur 11](appkit-release-notes-for-macos-11.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS 10.14](appkit-release-notes-for-macos-10_14.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/appkit-release-notes-for-macos-12)*