# tvOS 14.5 Release Notes

**Framework**: tvOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 14.5 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 14.5. The SDK comes bundled with Xcode 12.5. For information on the compatibility requirements for Xcode 12.5, see [Xcode 12.5 Release Notes](../Xcode-Release-Notes/xcode-12_5-release-notes.md).

##### Accessibility

###### New Features

- Many SF Symbols now have default accessibility labels. (70305995)

##### Combine

###### Resolved Issues

- Using [`Published`](../Combine/published.md) in a subclass of a type conforming to [`ObservableObject`](../Combine/observableobject.md) now correctly publishes changes. (70305995)

##### SwiftUI

###### New Features

- Added [`TitleAndIconLabelStyle`](../SwiftUI/titleandiconlabelstyle.md), a new style for [`Label`](../SwiftUI/label.md) views that shows both the title and icon of the label using a system-standard layout. In most cases, labels show both title and icon by default. However, some containers might apply a different default label style to their content, such as only showing icons within toolbars on macOS and iOS. To opt in to showing both the title and the icon, apply the title and icon label style: `Label("Lightning", systemImage: "bolt.fill").labelStyle(TitleAndIconLabelStyle())`. (64646578)
- Types conforming to any style protocol, such as [`ButtonStyle`](../SwiftUI/buttonstyle.md) or [`ToggleStyle`](../SwiftUI/togglestyle.md), are now enforced to be value types. Styles must be structures or enumerations, not classes, and conforming a class to a style protocol may trigger an assertion. This is the same restriction that the system has always enforced on types conforming to [`View`](../SwiftUI/view.md). (62886135)

###### Resolved Issues

- You can now apply multiple [`sheet(isPresented:onDismiss:content:)`](../SwiftUI/view/sheet%28ispresented,ondismiss,content%29.md) and [`fullScreenCover(item:onDismiss:content:)`](../SwiftUI/view/fullscreencover%28item,ondismiss,content%29.md) modifiers in the same view hierarchy. (74246633)
- Dynamic properties such as [`State`](../SwiftUI/state.md), [`Environment`](../SwiftUI/environment.md), and others now work correctly in [`ButtonStyle`](../SwiftUI/buttonstyle.md) instances. (62886135)
- [`ProgressView`](../SwiftUI/progressview.md) instances initialized with a [`Progress`](../Foundation/progress.md) object now correctly track updates to the `Progress` object from background threads, and no longer issue a “not allowed” console warning. (69999449)
- [`InlinePickerStyle`](../SwiftUI/inlinepickerstyle.md) now resolves as an in-line section if applied to a [`Picker`](../SwiftUI/picker.md) within a [`List`](../SwiftUI/list.md) on iOS, watchOS, and tvOS, using a checkmark to indicate the selected option. (71383311)
- [`AppStorage`](../SwiftUI/appstorage.md) property wrappers now work as expected when contained inside an [`ObservableObject`](../Combine/observableobject.md), causing the system to emit the `objectWillChange` publisher. (65562845)
- Using [`scrollTo(_:anchor:)`](../SwiftUI/scrollviewproxy/scrollto%28_,anchor%29.md) without specifying an anchor now scrolls the [`List`](../SwiftUI/list.md) the minimum amount to make it visible. (70184639)

##### UIKit

###### Resolved Issues

- [`leadingAccessoryView`](../UIKit/uitabbar/leadingaccessoryview.md) and [`trailingAccessoryView`](../UIKit/uitabbar/trailingaccessoryview.md) in [`UITabBar`](../UIKit/uitabbar.md) now appear correctly with right-to-left languages. (66755869)
- In a [`UICollectionView`](../UIKit/uicollectionview.md), the focusability of a cell no longer depends on the delegate returning `YES` from the [`collectionView(_:shouldHighlightItemAt:)`](../UIKit/uicollectionviewdelegate/collectionview%28_,shouldhighlightitemat%29.md) and [`collectionView(_:shouldSelectItemAt:)`](../UIKit/uicollectionviewdelegate/collectionview%28_,shouldselectitemat%29.md) methods if they are implemented and [`collectionView(_:canFocusItemAt:)`](../UIKit/uicollectionviewdelegate/collectionview%28_,canfocusitemat%29.md) method is not implemented. (70245159)

##### Xcode

###### Resolved Issues

- The View Debugger no longer crashes when viewing an app that includes custom Shapes. (72300793)

## See Also

### tvOS 14
- [tvOS 14.7 Release Notes](./tvos-14_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.6 Release Notes](./tvos-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.4 Release Notes](./tvos-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.3 Release Notes](./tvos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.2 Release Notes](./tvos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14 Release Notes](./tvos-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-14_5-release-notes)*