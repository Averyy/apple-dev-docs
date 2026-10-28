# macOS Big Sur 11.3 Release Notes

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The macOS 11.3 SDK provides support to develop apps for Macs running macOS Big Sur 11.3. The SDK comes bundled with Xcode 12.5. For information on the compatibility requirements for Xcode 12.5, see [Xcode 12.5 Release Notes](../Xcode-Release-Notes/xcode-12_5-release-notes.md).

### General

#### Deprecations

- Support for the Developer Transition Kit is no longer available as of macOS Big Sur 11.3.

### Accessibility

#### New Features

- Many SF Symbols now have default accessibility labels. (70305995)

### Combine

#### Resolved Issues

- Using [`Published`](../Combine/published.md) in a subclass of a type conforming to [`ObservableObject`](../Combine/observableobject.md) now correctly publishes changes. (71816443)

### SwiftUI

#### New Features

- Added [`TitleAndIconLabelStyle`](../SwiftUI/titleandiconlabelstyle.md), a new style for [`Label`](../SwiftUI/label.md) views that shows both the title and icon of the label using a system-standard layout. In most cases, labels show both title and icon by default. However, some containers might apply a different default label style to their content, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, apply the title and icon label style: `Label("Lightning", systemImage: "bolt.fill").labelStyle(TitleAndIconLabelStyle())`. (64646578)
- Types conforming to any style protocol, such as [`ButtonStyle`](../SwiftUI/buttonstyle.md) or [`ToggleStyle`](../SwiftUI/togglestyle.md), are now enforced to be value types. Styles must be structures or enumerations, not classes, and conforming a class to a style protocol may trigger an assertion. This is the same restriction that the system has always enforced on types conforming to [`View`](../SwiftUI/view.md). (62886135)

#### Resolved Issues

- A custom [`CommandMenu`](../SwiftUI/commandmenu.md) in an app built against an SDK prior to macOS 11.3 now appears correctly when run on macOS 11.3. (74721633)
- Labels for some controls in a customizable toolbar now show as expected in Icon and Text display mode. (73911090)
- The outline for a [`List`](../SwiftUI/list.md) now updates correctly when its data collection changes to or from an empty value. (71264665)
- [`FocusedValue`](../SwiftUI/focusedvalue.md) and [`FocusedBinding`](../SwiftUI/focusedbinding.md) now reflect the first published value the system encounters in a leading-to-trailing traversal of the active window’s view hierarchy. This allows focused values published at the root of your view tree with `focusedValue(_:_:)` to be visible by default when there’s no focused view hierarchy from which the systems can read a more contextually-specific value. (59321659)
- [`NSViewRepresentable`](../SwiftUI/nsviewrepresentable.md) fonts are no longer overridden based on the [`controlSize`](../SwiftUI/environmentvalues/controlsize.md) of the system environment for apps built with the macOS 11.3 SDK. (72098357)
- Setting `preferredColorScheme(_:)` to `nil` now correctly resets to the system’s preferred color scheme. (67000774)
- [`DocumentGroup`](../SwiftUI/documentgroup.md) apps now show an Open panel on launch, even when iCloud isn’t in use. (66446310)
- [`UIStepper`](../UIKit/uistepper.md) controls in Optimized for Mac Catalyst apps now look and function as expected. (69932695)
- Constraints on sheet content using a [`frame(width:height:alignment:)`](../SwiftUI/view/frame%28width,height,alignment%29.md) modifier are no longer lost if the content had a [`toolbar`](../SwiftUI/commandgroupplacement/toolbar.md) applied. (70145815)
- There’s no longer default spacing between sheet content and its associated [`ToolbarItem`](../SwiftUI/toolbaritem.md) elements. Explicit padding should be added if required. (70146121)
- [`GroupBox`](../SwiftUI/groupbox.md) background colors now resolve correctly in apps built with Mac Catalyst. (70751748)
- A [`List`](../SwiftUI/list.md) now updates as expected when its [`OutlineGroup`](../SwiftUI/outlinegroup.md) data changes between being flat or empty and having hierarchy. (71354760)
- Dismissing a sheet no longer causes the window to close unexpectedly. (71541062)
- Dynamic properties such as [`State`](../SwiftUI/state.md), [`Environment`](../SwiftUI/environment.md), and others now work correctly in [`ButtonStyle`](../SwiftUI/buttonstyle.md) instances. (62886135)
- [`AppStorage`](../SwiftUI/appstorage.md) property wrappers now work as expected when contained inside an [`ObservableObject`](../Combine/observableobject.md), causing the system to emit the `objectWillChange` publisher. (65562845)
- [`ProgressView`](../SwiftUI/progressview.md) instances that the system initializes with a [`Progress`](../Foundation/progress.md) object now correctly track updates to the `Progress` object from background threads, and no longer issue a “not allowed” console warning. (69999449)
- Using [`scrollTo(_:anchor:)`](../SwiftUI/scrollviewproxy/scrollto%28_,anchor%29.md) without specifying an anchor now scrolls the [`List`](../SwiftUI/list.md) the minimum amount to make it visible. (70184639)

### Xcode

#### Deprecations

- Don’t use the iOS [`MinimumOSVersion`](../BundleResources/information-property-list/minimumosversion.md) information property list key to declare the minimum release of macOS in which your app runs. Use [`LSMinimumSystemVersion`](../BundleResources/information-property-list/lsminimumsystemversion.md) instead. (73890473)

  - Future releases of macOS ignore the `MinimumOSVersion` key in Mac apps, including apps built with Mac Catalyst.
  - Future releases of macOS use the `LSMinimumSystemVersion` key in iOS apps built with Xcode 12.5 or later. If an iOS app doesn’t include an `LSMinimumSystemVersion` key, future releases of macOS compare the app’s `MinimumOSVersion` with the version of its Mac Catalyst runtime to determine compatibility.

## See Also

### macOS 11
- [macOS Big Sur 11.5 Release Notes](./macos-big-sur-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.4 Release Notes](./macos-big-sur-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.2 Release Notes](./macos-big-sur-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.1 Release Notes](./macos-big-sur-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Release Notes](./macos-big-sur-11_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Universal Apps Release Notes](./macos-big-sur-11_0_1-universal-apps-release-notes.md)
  Update your apps to support Macs with Apple silicon.
- [macOS Big Sur 11.0.1 iOS & iPadOS Apps on Mac Release Notes](./macos-big-sur-11_0_1-ios-ipados-apps-on-mac-release-notes.md)
  Considerations for running iPhone and iPad apps on Macs with Apple silicon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-big-sur-11_3-release-notes)*