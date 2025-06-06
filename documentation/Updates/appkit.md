# AppKit updates

**Framework**: Updates

Learn about important changes to AppKit.

#### Overview

Browse notable changes in [`AppKit`](https://developer.apple.comhttps://developer.apple.com/documentation/appkit).

#### April 2025

##### Macos Pasteboard Privacy

- Prepare your app for an upcoming feature in macOS that alerts a person using a device when your app programmatically reads the general pasteboard. The system shows the alert only if the pasteboard access wasn’t a result of someone’s input on a UI element that the system considers paste-related. This behavior is similar to how [`UIPasteboard`](https://developer.apple.com/documentation/UIKit/UIPasteboard) behaves in iOS. New `detect` methods in [`NSPasteboard`](https://developer.apple.com/documentation/AppKit/NSPasteboard) and [`NSPasteboardItem`](https://developer.apple.com/documentation/AppKit/NSPasteboardItem) make it possible for an app to examine the kinds of data on the pasteboard without actually reading them and showing the alert. [`NSPasteboard`](https://developer.apple.com/documentation/AppKit/NSPasteboard) also adds an [`accessBehavior`](https://developer.apple.com/documentation/AppKit/NSPasteboard/accessBehavior-86972) property to determine if programmatic pasteboard access is always allowed, never allowed, or if it prompts an alert requesting permission. You can adopt these APIs ahead of the change, and set a user default to test the new behavior on your Mac. To do so, launch Terminal and enter the command `defaults write <your_app_bundle_id> EnablePasteboardPrivacyDeveloperPreview -bool yes` to enable the behavior for your app.

#### June 2024

##### General

- Organize your windows’ display and layout with window tiling.

##### Swift and Swiftui

- Use SwiftUI menus in AppKit with the [`NSHostingMenu`](https://developer.apple.com/documentation/SwiftUI/NSHostingMenu).
- Animate AppKit views using SwiftUI animations using [`animate(with:changes:completion:)`](https://developer.apple.com/documentation/AppKit/NSAnimationContext/animate(with:changes:completion:)).

##### Api Refinements

- Use the keyboard to open context menus for UI elements on which you are focused currently.
- Highlight text and choose from a number of highlight color schemes with [`NSAttributedString.TextHighlightStyle`](https://developer.apple.com/documentation/Foundation/NSAttributedString/TextHighlightStyle).
- Add repeat, wiggle, bounce, and rotate effects to [`SF Symbols`](https://developer.apple.comhttps://developer.apple.com/sf-symbols/).
- Leverage predefined content types when saving files using the new format picker on `NSPanel`.
- Resize frames and zoom in and out with new `NSCursor` APIs such as [`NSCursor.FrameResizeDirection`](https://developer.apple.com/documentation/AppKit/NSCursor/FrameResizeDirection) and [`NSCursor.FrameResizePosition`](https://developer.apple.com/documentation/AppKit/NSCursor/FrameResizePosition).
- Control whether your toolbars display text as well as icons using the [`allowsDisplayModeCustomization`](https://developer.apple.com/documentation/AppKit/NSToolbar/allowsDisplayModeCustomization) property.
- Offer customized type-ahead suggestions in NSTextField using the [`suggestionsDelegate`](https://developer.apple.com/documentation/AppKit/NSTextField/suggestionsDelegate).

#### June 2023

##### Views and Controls

- Use the new `userCanChangeVisibilityOf` delegate method on `NSTableView` to toggle the visibility of table columns.
- Use a new `NSProgressIndicator` property to observe progress of an ongoing task.
- Simplify how you display and style buttons with the new `.automatic` bezel style. This bezel style adapts to the most appropriate style based on the contents of the button, as well as its location in the view hierarchy.
- Display additional contextual information about currently selected documents with `NSSplitView` inspectors.
- New improvements to `NSPopover` enable you to anchor popovers from toolbar items, as well as support full-size popovers.
- Explore new UI elements in `NSMenu`. Group information more easily in section headers, lay out menu items in horizontal palettes, as well as display badge counts on menu items.

##### Cooperative App Activation

- App activation is now driven by the user, preventing unexpected switches between apps.
- Take advantage of Cooperative Activation, where your apps can yield and accept activation from other apps on the system without interrupting the user’s workflows. For more information, see the `activate()` function on `NSApp` and `NSRunningApplication`.

##### Graphics

- `CGPath` and `NSBezierPath` are now interoperable. You can create a `CGPath` from a `NSBezierPath` and vice versa.
- Leverage `CADisplayLink` to synchronize your app’s ability to draw to the refresh of the display.
- Create consistent, great visuals for your controls by taking advantage of standard system fill `NSColor` (`.systemFill`, `.secondarySystemFill`, `.tertiarySystemFill`, `.quaternarySystemFill`, and `.quinarySystemFill`).
- Views no longer clip their contents by default. This includes any drawing done by the view and its subviews. For more information, see the `clipsToBounds` property on `NSView`.
- Animate symbol images with the new `addSymbolEffect` function on ` NSImageView`. Symbol effects include: bounce, pulse, variable color, scale, appear, disappear, and replace.
- Display and manipulate high dynamic range (HDR) images.

##### Swift and Swiftui

- AppKit more fully integrates with Swift and SwiftUI with Sendable (`NSColor`, `NSColorSpace`, `NSGradient`, `NSShadow`, `NSTouch`) and Transferable (`NSImage`, `NSColor`, `NSSound`) types.
- Preview your views and view controllers alongside your code using the new `#Preview` Swift macro. Incrementally adopt SwiftUI into your AppKit life cycle by leveraging modifiers like toolbar and navigation title on `NSWindows`.
- Simplify your code with new attributes, `@ViewLoading` and `@WindowLoading`, to help with view and window loading.

##### Text Improvements

- Help people enter text more effectively with the `NSTextInsertionIndicator` that adapts to the current accent color of the app. Cursor accessories also help users visualize where and how to enter text.
- Simplify `NSTextField` entry by leveraging the new `.contentType` AutoFill feature, making it more convenient to enter types such as contact information, birthdays, names, credit cards, and street addresses.
- Adopt text styles like `.body`, `largeTitle`, and `headline` on `NSFont.preferredFont`  to take advantage of enhancements to the font system, like improved hyphenation for non-English languages and dynamic line-height adjustments for languages that require more vertical space. Access localized variants of symbol images by specifying a locale.

> **Note**: Session 10054: [`What’s new in AppKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10054/)

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.
- [Core Location updates](corelocation.md)
  Learn about important changes to Core Location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Updates/appkit)*