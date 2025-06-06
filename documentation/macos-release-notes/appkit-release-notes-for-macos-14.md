# AppKit Release Notes for macOS 14

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

AppKit in macOS14 includes new features, as well as API changes and deprecations.

###### Nsepsimagerep

- Deprecated in macOS 14.0 as encapsulated PostScript (EPS) files are no longer supported by macOS. Learn more on Apple Support. (107052479)
- Attempting to initialize an instance of `NSEPSImageRep` will always return `nil` on macOS 14.0 and later.
- Attempting to initialize an instance of` NSImage` with an EPS file or data will always return `nil` on macOS 14.0 and later.
- If a multi-rep image is initialized by name `(NSImage(named:)`, `Bundle.image(forResource:`), etc.), it will no longer include EPS reps. If no supports (non-EPS) reps could be produced, this will result in `nil` being returned from these functions.

###### Nsimagedelegate

- Deprecated four of the five NSImageDelegate methods as of Mac OS X 10.4 Tiger. (18422088)
- `-image:willLoadRepresentation:`
- `-image:didLoadRepresentationHeader:`
- `-image:didLoadPartOfRepresentation:withValidRows:`
- `-image:didLoadRepresentation:withStatus:`
- These methods haven’t been called by AppKit since Mac OS X 10.4 Tiger.
- Using these symbols in Objective-C may produce warnings or errors, depending on the project’s build settings.
- These symbols are no longer available in Swift in the macOS 14.0 SDK.

###### Nssavepanel Nsopenpanel

- Added the property identifier. (4228269)
- Modeless and application modal open and save panels are now main windows. (14623155, 103038843)  This fixes a problem where menu items that weren’t applicable to the open or save panel remained `enabled. Open` and save panels that are displayed as sheets are unchanged.
- Removed the titlebar from modal and modeless `NSSavePanels`. (105212420)  This changes `NSSavePanel` to have consistent behavior with `NSOpenPanel`.

###### Nsprintpanel Nspagelayout

- Applications linking against SDKs released for Fall 2023 may now release the `NSPrintInfo` instance and other related objects as soon as the `NSPrintPanel` / `NSPageLayout` panel is dismissed.
- Added block based variants of the begin-sheet methods (6990600): ```None
 class NSPrintPanel {
 	open func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow, completionHandler handler: ((NSPrintPanel.Result) -> Void)? = nil)
 	open func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow) async -> NSPrintPanel.Result
 }

 class NSPageLayout {
 	open func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow, completionHandler handler: ((NSPageLayout.Result) -> Void)? = nil)
 	open func beginSheet(using printInfo: NSPrintInfo, on parentWindow: NSWindow) async -> NSPageLayout.Result
 }
```

###### Nscolor

- `NSColor.textInsertionPointColor` provides a robust way to get the current text insertion point color as defined by the system.
- To be consistent with an `NSTextView`, use `NSTextView.insertionPointColor`.
- Otherwise, if not using a text view, use `NSColor.textInsertionPointColor`.

###### Nstextinsertionindicator

- `NSTextInsertionIndicator` is a new `NSView` that encapsulates all the behavior for a text insertion indicator — such as blinking while waiting for typing and prompting during dictation. `NSTextView `uses the `NSTextInsertionIndicator`. But, if using a custom text implementation, instantiate and add an `NSTextInsertionIndicator` as a subview of the custom text view. Its text implementation only needs to set the indicator view’s display mode—automatic, visible, or hidden—and frame. Based on the display mode the indicator view will infer from the frame whether it needs to blink or not.

###### Nsview

- In macOS 14, AppKit is exposing the `clipsToBounds` property of `NSView`. For applications linked against the macOS 14 SDK, the default value of this property is `false`. Apps linked against older SDKs default to `true`. Some classes, like `NSClipView`, continue to default to `true`. The change in defaults recognizes that it is vastly easier to reason about clipping a view’s descendants than it is to unclip a view’s ancestors. Users can turn clipping back on by using the `NSView.clipsToBounds` setter or using the attributes inspector of a view in the Xcode interface builder. This property is available back to macOS 10.9. This availability is intended to allow code targeting older OSes to set this property to `true` without guarding the setter in an availability check. Setting this property to `false` on previous OSes may not work reliably. Some patterns that have historically worked will require adjustment: - Showing or hiding UI by setting an ancestor’s frame to zero. When attempting to hide a view hierarchy by shrinking the size of an ancestor, or positioning a descendent view outside an ancestors view’s bounds, it is now necessary to set the ancestor’s view’s `.clipsToBounds` property to `true`. An alternative may be to set `NSView.isHidden`, instead.
- Filling the dirty rect of a view inside of `-drawRect`. A fairly common pattern is to simply rect fill the dirty rect passed into an override of `NSView.draw()`. The dirty rect can now extend outside of your view’s bounds. This pattern can be adjusted by filling the bounds instead of the dirty rect, or by setting `clipsToBounds = true`.
- Confusing a view’s bounds and its dirty rect. The dirty rect passed to `.drawRect()` should be used to determine what to draw, not where to draw it. Use `NSView.bounds` when determining the layout of what your view draws.  (10905750)

###### Nsviewcontroller

- Added API: ```None
 open var viewIfLoaded: NSView? { get }
 open func loadViewIfNeeded()
 open func present(_ viewController: NSViewController, asPopoverRelativeTo positioningRect: NSRect, of positioningView: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)
```
- `NSViewController.loadView()` no longer throws an exception when the view controller’s nibName is nil. (81775005)

###### Textkit Api Coordinate System Changes

- Applications linking against SDKs released for Fall 2023 have behavior changes from TextKit API.
- `NSTextLineFragment.typographicBounds` is relative to `NSTextLayoutFragment.layoutFragmentFrame.origin` (instead of in the text container coordinate system as it was before)
- `NSTextLineFragment.typographicBounds.size.width` doesn’t contain `NSTextContainer.lineFragmentPadding`. The side effect of this change is that the padding is also excluded from both `NSTextLayoutFragment.layoutFragmentFrame` and `NSTextLayoutManager.usageBoundsForTextContainer`. Consequently, `NSTextLineFragment.glyphOrigin.x` no longer includes the padding, either.
- `NSTextLineFragment.locationForCharacterAtIndex()` used to return a point relative to `NSTextLayoutFragment.origin`. It now returns a point relative to the text line fragment coordinate system as documented.

###### Restorable State

- Secure coding is automatically enabled for restorable state for applications linked on the macOS 14.0 SDK. Applications that target prior versions of macOS should implement `NSApplicationDelegate.applicationSupportsSecureRestorableState()` to return `true` so it’s enabled on all supported OS versions.

###### Display Link

- A `CADisplayLink` can be created via `NSView.displayLink(target:selector:)`. The `CADisplayLink` will automatically track the display the view is on, and will be automatically suspended if it isn’t on a display. A `CADisplayLink` instance can also be created from an `NSWindow` or `NSScreen`.

###### Nstoolbar

- Applications linked against the macOS 14.0 SDK will no longer show the `.toggleSidebar` toolbar item to the leading edge of the inline window title and will instead show relative to its order in the `defaultItemIdentifiers` delegate method. It is recommended to place this item above the sidebar section of the toolbar as the leading most item of that section so that toggling the sidebar does not move the toolbar item itself. As a reminder, items placed before the `.sidebarTrackingSeparator` in the `defaultItems` delegate method will appear above the sidebar in the toolbar. Similarly, the best place for the new `.toggleInspector` item is above the inspector section of the toolbar as the trailing most item following the `.inspectorTrackingSeparator`, but it may be placed elsewhere in the toolbar if appropriate.
- `NSToolbar` now supports centering items in multiple sections of the toolbar. Use the `centeredItemIdentifiers` property to specify a set of items and they will be centered in the section they appear in. The set of centered items no longer applies to a single section of the toolbar, but may be used to center one item in the sidebar section and another item in the content section for instance.
- `NSToolbar` with `autosavesConfiguration` enabled and `allowsUserCustomization` disabled will now persist manual changes to the toolbar from `-insertItemWithIdentifier:atIndex:` and `-removeItemAtIndex:` across app launches. Previously manual inserts/removes were not persisted. Additionally, `NSToolbars` with `autosavesConfiguration` disabled will now sync manual inserts/removes to other `NSToolbar` objects with the same `identifier`, including new windows, but the toolbar’s configuration will not persist across app launches. If syncing across windows is not desired, each window’s toolbar should be given a unique `identifier`.  (103038749)

###### Menus

- In macOS 14, menus have been reimplemented from the ground up to fully use AppKit.
- New section header API provides a consistent way to organize and structure menus.
- NSMenu has new `selectionBehavior` property, which allows the menu to automatically manage state of the same selection groups, reducing the amount of code the developer has to write.
- Palette presentation style allows to show menu items in a horizontal series, embedded inline in the parent menu.
- `NSMenuItem` has new API to create section header menu items, which are used to organize and structure menus. The appearance and behavior of section header items are entirely defined by `NSMenu` and cannot be customized.  (59962793)
- For applications linked against the macOS 14 SDK, `NSMenu` will now assert if a secondary thread inserts or removes menu items from menus contained within the main menu. Making changes to the main menu from any thread other than the main thread has never been a supported or safe programming practice, because the main thread may be examining the main menu contents at any time (for example, to draw the menubar, to determine if a menu item matches a key event, to answer an accessibility request, etc), and there is no method for a background thread to modify the main menu while ensuring that the main thread is not simultaneously examining its contents. This practice is now prevented at runtime.  (96331659)

###### App Activation

- In macOS 14, app activation is driven by user intent. It is treated by the system as a request and is not always guaranteed to be honored or to succeed. Apps have the ability to provide context with activation requests in cases where a more deterministic result is desired.
- `NSApplication.activate(ignoringOtherApps:)` and `NSApplication.ActivationOptions.ignoringOtherApps` are deprecated in macOS 14 and should not be used.
- `NSApplication` has a new method, `activate`, that sends the activation request to the system. The request may provide different results based on the context in which the app is running, user activity, and other factors. If necessary for app functionality, active status can be checked by querying the isActive property on `NSApplication`. In general, apps should not assume that activation requests will always succeed.
- macOS 14 provides more ways for apps to express the context in which activation should occur. A common scenario is cooperative activation, or passing the active state from one app to another. This process can be useful for apps that need to explicitly pass activation state, such as launchers and view services. The active app can use `NSApplication.yield(to:)` method to yield its active state to an instance of `NSRunningApplication`, or `yield(toApplicationWithBundleIdentifier:)` to yield to a bundle ID, which may be used in case the receiver app is not running or its status is unknown. Note that the sender does not deactivate at the time of invoking these methods. After yielding, the sender may activate the receiver using `NSRunningApplication` API, or the target app may simply activate itself by invoking the `NSApplication.activate` method. The cooperative activation mechanism guarantees successful activation as long as the yielding app is active at the time of the request and the receiver can become active.
- Existing calls to `NSApplication.deactivate()` should be replaced by `NSApplication.yield(to:)` to make activation handoff more explicit, and to delay changing the appearance of the calling app until the target app has activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/appkit-release-notes-for-macos-14)*