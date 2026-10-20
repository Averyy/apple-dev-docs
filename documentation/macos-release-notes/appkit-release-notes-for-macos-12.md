# AppKit Release Notes for macOS Monterey 12

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

AppKit in macOS Monterey 12 includes new features, as well as API changes and deprecations.

##### New Features

###### NSButton

- Buttons no longer highlight using the accent color when clicked. Before using any subclass that performs custom drawing, inspect the button cell’s `interiorBackgroundStyle` property to determine if the bezel draws in a normal or emphasized state.
- Buttons now support custom tinting with the [`bezelColor`](../AppKit/nsbutton/bezelcolor.md) property. This property — previously applied only in the Touch Bar — now functions for all in-window buttons using the `NSButtonTypeMomentaryPushIn` style.

###### NSSlider

- When clicking on the track, for linear sliders, circular sliders, or dial, the slider now animates to the new value.
- You can now tint sliders with colorful track fills using the [`trackFillColor`](../AppKit/nsslider/trackfillcolor.md) property. This property now functions for all in-window sliders.

###### NSSegmentedControl

- Segmented controls now support custom tinting via the [`selectedSegmentBezelColor`](../AppKit/nssegmentedcontrol/selectedsegmentbezelcolor.md) property. This property now functions for all in-window segmented control styles that draw colorful selected segments.

###### NSPopover

- [`NSPopover`](../AppKit/nspopover.md) has a new animation when appearing and dismissing.

###### Symbol Images

- SF Symbols now support layered symbol images. Layered symbol images use an updated data format to annotate each path element of the symbol with a level in a hierarchy: primary, secondary, tertiary, and so on. At draw time, AppKit can assign different colors to each layer of the symbol using new APIs on [`NSImage.SymbolConfiguration`](../AppKit/nsimage/symbolconfiguration-swift.class.md). Many system-provided symbol images redesigned to include layered versions.
- [`NSImage.SymbolConfiguration`](../AppKit/nsimage/symbolconfiguration-swift.class.md) now supports merging two configurations with [`applying(_:)`](../UIKit/uiimage/configuration-swift.class/applying%28_%29.md) method.
- [`NSImage`](../AppKit/nsimage.md) now includes a read-only property, [`NSImage.SymbolConfiguration`](../AppKit/nsimage/symbolconfiguration-swift.class.md), for its current symbol configuration. You can use this property to configure other symbol images to match a reference image, or to merge an image’s existing configuration with a set of new configuration options.

###### Restorable State

- To enable secure coding for a restorable state, implement [`applicationSupportsSecureRestorableState(_:)`](../AppKit/nsapplicationdelegate/applicationsupportssecurerestorablestate%28_%29.md). When opted in:

  - The system requires classes passed to [`restorationClass`](../AppKit/nswindow/restorationclass.md) to explicitly conform to [`NSWindowRestoration`](../AppKit/nswindowrestoration.md).
  - Set [`requiresSecureCoding`](../Foundation/nscoder/requiressecurecoding.md) to `true` and the [`decodingFailurePolicy`](../Foundation/nscoder/decodingfailurepolicy-swift.property.md) to [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](../Foundation/nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md) for any coder the following implementations or overrides use [`decodingFailurePolicy`](../Foundation/nscoder/decodingfailurepolicy-swift.property.md) set to [`NSCoder.DecodingFailurePolicy.setErrorAndReturn`](../Foundation/nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md):

    - [`restoreWindow(withIdentifier:state:completionHandler:)`](../AppKit/nswindowrestoration/restorewindow%28withidentifier,state,completionhandler%29.md)
    - [`restoreWindow(withIdentifier:state:completionHandler:)`](../AppKit/nsapplication/restorewindow%28withidentifier,state,completionhandler%29.md)
    - [`encodeRestorableState(with:)`](../AppKit/nsresponder/encoderestorablestate%28with%29.md)
    - [`encodeRestorableState(with:backgroundQueue:)`](../AppKit/nsresponder/encoderestorablestate%28with,backgroundqueue%29.md)
    - [`restoreState(with:)`](../AppKit/nsresponder/restorestate%28with%29.md)
    - [`restoreWindow(withIdentifier:state:completionHandler:)`](../AppKit/nsdocument/restorewindow%28withidentifier,state,completionhandler%29.md)
    - [`encodeRestorableState(with:)`](../AppKit/nsdocument/encoderestorablestate%28with%29.md)
    - [`encodeRestorableState(with:backgroundQueue:)`](../AppKit/nsdocument/encoderestorablestate%28with,backgroundqueue%29.md)
    - [`restoreState(with:)`](../AppKit/nsdocument/restorestate%28with%29.md)
  - Additionally, [`restorableStateKeyPaths`](../AppKit/nsdocument/restorablestatekeypaths.md) must only point at `NSSecureCoding`-compliant values and you need to implement [`allowedClasses(forRestorableStateKeyPath:)`](../AppKit/nsdocument/allowedclasses%28forrestorablestatekeypath%29.md) to specify the type of the object.

###### NSMenu

- The new user preference “Automatically hide and show the menu bar in full screen” in Dock & Menu Bar preferences is enabled by default. In macOS Monterey 12, the user can choose to disable this setting to always show the menu bar in full screen spaces. Standard full screen windows are resized to fit below the menu bar. Some apps assume a full screen-sized window, and don’t work well with this setting.

###### NSTableView

- 20-point spacing precedes each group row to make the separation between sections more visible. Source lists have a similar, but smaller, 13-point spacing. This applies to the [`NSTableView.Style.inset`](../AppKit/nstableview/style-swift.enum/inset.md) and [`NSTableView.Style.fullWidth`](../AppKit/nstableview/style-swift.enum/fullwidth.md) effective styles in apps linked against the macOS 12 SDK. [`NSTableView.Style.plain`](../AppKit/nstableview/style-swift.enum/plain.md) doesn’t display the spacing.
- The floating group row transition — previously a push transition — instantly replaces the new floating group row. It occurs when the `x-height` of the group row’s label meets the bottom of a currently floating group row.

###### NSOutlineView

- The disclosure button now aligns with the cell view’s [`firstBaselineOffsetFromTop`](../AppKit/nsview/firstbaselineoffsetfromtop.md). The system overrides it in [`NSTableCellView`](../AppKit/nstablecellview.md) so it matches the baseline of its [`textField`](../AppKit/nstablecellview/textfield.md) (assuming `textfield` sets the baseline). Overriding the property and returning `0` reverts to the previous behavior.
- When collapsing several items, the [`selectionDidChangeNotification`](../AppKit/nsoutlineview/selectiondidchangenotification.md) only posts once. Previously, it posted once per collapsed item.

###### NSOpenPanel

- Setting [`canChooseFiles`](../AppKit/nsopenpanel/canchoosefiles.md) to `false` automatically disabled files, but all of the directory contents were sent to [`panel(_:shouldEnable:)`](../AppKit/nsopensavepaneldelegate/panel%28_,shouldenable%29.md) or [`panel:shouldShowFilename:`](../ObjectiveC/nsobject-swift.class/panel_shouldshowfilename_.md). In macOS Monterey 12, files aren’t sent to the delegate methods unless `canChooseFiles` is `true`. In addition, file packages are excluded unless `treatsFilePackagesAsDirectoriesis` is `true`. This change allows optimization in the delegate method.

###### TextKit 2

- TextKit 2 introduces a new text layout engine and its associated API. You can use TextKit 2  alongside the existing [TextKit](../AppKit/textkit.md) API.
- [`NSTextContentStorage`](../UIKit/nstextcontentstorage.md) and [`NSTextLayoutManager`](../UIKit/nstextlayoutmanager.md) are the two main controller objects superseding [`NSTextStorage`](../AppKit/nstextstorage.md) and [`NSLayoutManager`](../AppKit/nslayoutmanager.md) respectively. [`NSTextParagraph`](../UIKit/nstextparagraph.md) managed by `NSTextContentStorage` represents a paragraph of text. `NSTextLayoutManager` stores the layout information in its model objects: [`NSTextLayoutFragment`](../UIKit/nstextlayoutfragment.md) and [`NSTextLineFragment`](../UIKit/nstextlinefragment.md).
- In TextKit 2, [`NSTextSelection`](../UIKit/nstextselection.md) encapsulates information associated with a text selection while [`NSTextSelectionNavigation`](../UIKit/nstextselectionnavigation.md) manipulates and converts the selection object based on keyboard and mouse navigation actions.

## See Also

### AppKit
- [AppKit Release Notes for macOS Sonoma 14](./appkit-release-notes-for-macos-14.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Ventura 13](./appkit-release-notes-for-macos-13.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS Big Sur 11](./appkit-release-notes-for-macos-11.md)
  Update your apps to use new features, and test your apps against API changes.
- [AppKit Release Notes for macOS 10.14](./appkit-release-notes-for-macos-10_14.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/appkit-release-notes-for-macos-12)*