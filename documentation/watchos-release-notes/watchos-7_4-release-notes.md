# watchOS 7.4 Release Notes

**Framework**: watchOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The watchOS 7.4 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 7.4. The SDK comes bundled with Xcode 12.5. For information on the compatibility requirements for Xcode 12.5, see [Xcode 12.5 Release Notes](../Xcode-Release-Notes/xcode-12_5-release-notes.md).

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

- Dynamic properties such as [`State`](../SwiftUI/state.md), [`Environment`](../SwiftUI/environment.md), and others now work correctly in [`ButtonStyle`](../SwiftUI/buttonstyle.md) instances. (62886135)
- [`ProgressView`](../SwiftUI/progressview.md) instances initialized with a [`Progress`](../Foundation/progress.md) object now correctly track updates to the `Progress` object from background threads, and no longer issue a “not allowed” console warning. (69999449)
- [`InlinePickerStyle`](../SwiftUI/inlinepickerstyle.md) now resolves as an in-line section if applied to a [`Picker`](../SwiftUI/picker.md) within a [`List`](../SwiftUI/list.md) on iOS, watchOS, and tvOS, using a checkmark to indicate the selected option. (71383311)
- [`AppStorage`](../SwiftUI/appstorage.md) property wrappers now work as expected when contained inside an [`ObservableObject`](../Combine/observableobject.md), causing the system to emit the `objectWillChange` publisher. (65562845)
- Using [`scrollTo(_:anchor:)`](../SwiftUI/scrollviewproxy/scrollto%28_,anchor%29.md) without specifying an anchor now scrolls the [`List`](../SwiftUI/list.md) the minimum amount to make it visible. (70184639)
- A [`TabView`](../SwiftUI/tabview.md) with [`PageTabViewStyle`](../SwiftUI/pagetabviewstyle.md) now correctly invokes `onAppear(perform:)` and `onDisappear(perform:)` for its tabs. (71225006)

## See Also

### watchOS 7
- [watchOS 7.6 Release Notes](./watchos-7_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.5 Release Notes](./watchos-7_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.3 Release Notes](./watchos-7_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.2 Release Notes](./watchos-7_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.1 Release Notes](./watchos-7_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7 Release Notes](./watchos-7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-7_4-release-notes)*