# watchOS 7.4 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 7.4 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 7.4. The SDK comes bundled with Xcode 12.5, available from the Mac App Store. For information on the compatibility requirements for Xcode 12.5, see [`Xcode 12.5 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12_5-release-notes).

##### Accessibility

###### New Features

- Many SF Symbols now have default accessibility labels. (70305995)

##### Combine

###### Resolved Issues

- Using [`Published`](https://developer.apple.com/documentation/Combine/Published) in a subclass of a type conforming to [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject) now correctly publishes changes. (71816443)

##### Swiftui

###### New Features

- Added [`TitleAndIconLabelStyle`](https://developer.apple.com/documentation/SwiftUI/TitleAndIconLabelStyle), a new style for [`Label`](https://developer.apple.com/documentation/SwiftUI/Label) views that shows both the title and icon of the label using a system-standard layout. In most cases, labels show both title and icon by default. However, some containers might apply a different default label style to their content, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, apply the title and icon label style: `Label("Lightning", systemImage: "bolt.fill").labelStyle(TitleAndIconLabelStyle())`. (64646578)
- Types conforming to any style protocol, such as [`ButtonStyle`](https://developer.apple.com/documentation/SwiftUI/ButtonStyle) or [`ToggleStyle`](https://developer.apple.com/documentation/SwiftUI/ToggleStyle), are now enforced to be value types. Styles must be structures or enumerations, not classes, and conforming a class to a style protocol may trigger an assertion. This is the same restriction that the system has always enforced on types conforming to [`View`](https://developer.apple.com/documentation/SwiftUI/View). (62886135)

###### Resolved Issues

- Dynamic properties such as [`State`](https://developer.apple.com/documentation/SwiftUI/State), [`Environment`](https://developer.apple.com/documentation/SwiftUI/Environment), and others now work correctly in [`ButtonStyle`](https://developer.apple.com/documentation/SwiftUI/ButtonStyle) instances. (62886135)
- [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) instances initialized with a [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) object now correctly track updates to the `Progress` object from background threads, and no longer issue a “not allowed” console warning. (69999449)
- [`InlinePickerStyle`](https://developer.apple.com/documentation/SwiftUI/InlinePickerStyle) now resolves as an in-line section if applied to a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) within a [`List`](https://developer.apple.com/documentation/SwiftUI/List) on iOS, watchOS, and tvOS, using a checkmark to indicate the selected option. (71383311)
- [`AppStorage`](https://developer.apple.com/documentation/SwiftUI/AppStorage) property wrappers now work as expected when contained inside an [`ObservableObject`](https://developer.apple.com/documentation/Combine/ObservableObject), causing the system to emit the doc://com.apple.documentation/documentation/combine/observableobject/objectwillchange-2oa5v publisher. (65562845)
- Using [`scrollTo(_:anchor:)`](https://developer.apple.com/documentation/SwiftUI/ScrollViewProxy/scrollTo(_:anchor:)) without specifying an anchor now scrolls the [`List`](https://developer.apple.com/documentation/SwiftUI/List) the minimum amount to make it visible. (70184639)
- A [`TabView`](https://developer.apple.com/documentation/SwiftUI/TabView) with [`PageTabViewStyle`](https://developer.apple.com/documentation/SwiftUI/PageTabViewStyle) now correctly invokes doc://com.apple.documentation/documentation/swiftui/anyview/onappear(perform:) and doc://com.apple.documentation/documentation/swiftui/anyview/ondisappear(perform:) for its tabs. (71225006)

## See Also

- [watchOS 7.6 Release Notes](watchos-7_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.5 Release Notes](watchos-7_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.3 Release Notes](watchos-7_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.2 Release Notes](watchos-7_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.1 Release Notes](watchos-7_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7 Release Notes](watchos-7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-7_4-release-notes)*