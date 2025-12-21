# tvOS 14 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 14 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 14. The SDK comes bundled with Xcode 12, available from the Mac App Store. For information on the compatibility requirements for Xcode 12, see [`Xcode 12 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12-release-notes).

##### Avkit

###### New Features

- Picture in Picture on tvOS allows for simultaneous video playback and the ability to swap between full-screen content and Picture in Picture. Use [`AVPlayerViewController`](https://developer.apple.com/documentation/AVKit/AVPlayerViewController) for adopting Picture in Picture in a standard player or AVKit framework’s [`AVPictureInPictureController`](https://developer.apple.com/documentation/AVKit/AVPictureInPictureController) class for your custom player. (54986706)

##### Game Center

###### New Features

- With multiuser support for gaming, your game can switch dynamically between users, and use both Game Center and iCloud to keep track of multiple players’ individual game levels, leaderboards, and invitations. The User Management entitlement has been expanded to include `runs-as-current-user`. This new value grants access to a separate set of data for your app for each user from Game Center, iCloud, and local storage. (56116380)

##### Logging

###### New Features

- New APIs are available for using `os_log` from Swift as part of the framework `os`: - A new type, [`Logger`](https://developer.apple.com/documentation/os/Logger), can be instantiated using a subsystem and category, and provides methods for logging at different levels (`Logger.debug`, `Logger.error`, `Logger.fault`).
- The `Logger` APIs support specifying most formatting and privacy options supported by legacy  [`Logging`](https://developer.apple.com/documentation/os/logging) APIs.
- The new APIs provide significant performance improvements over the legacy APIs.
- You can now pass Swift string interpolation to the [`os_log`](https://developer.apple.com/documentation/os/os_log) function.  The new APIs can’t be back deployed; however, the existing `os_log` API remains available for back deployment. (22539144)

##### Swiftui

###### New Features

- [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) now supports adding a secondary “current value label” that describes the current progress level of the task. Use the [`label`](https://developer.apple.com/documentation/SwiftUI/ProgressViewStyleConfiguration/label-swift.property) to describe the overall task, and the [`ProgressViewStyleConfiguration.CurrentValueLabel`](https://developer.apple.com/documentation/SwiftUI/ProgressViewStyleConfiguration/CurrentValueLabel-swift.struct) to provide more specific details about the progress of the task. (63580200)
- Introduced [`ToolbarItemGroup`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemGroup) as a convenient way to place multiple items in a specific location of non-customizable toolbars. (64178863)
- [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) can be converted to and from [`cgColor`](https://developer.apple.com/documentation/UIKit/UIColor/cgColor). The [`ColorPicker`](https://developer.apple.com/documentation/SwiftUI/ColorPicker) can also now be configured with a binding to a `CGColor`. (56939085)
- [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) is now redacted when the `redacted(reason:)` modifier is applied. (65047189)
- [`InlinePickerStyle`](https://developer.apple.com/documentation/SwiftUI/InlinePickerStyle) is now available and allows a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) to appear in-line with the rest of the content in its surrounding container. The style will adapt its appearance for different containers and platforms, such as individual menu items in a menu. (59868844)
- [`List`](https://developer.apple.com/documentation/SwiftUI/List) may now be used with [`ScrollViewReader`](https://developer.apple.com/documentation/SwiftUI/ScrollViewReader). (35471164)
- [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) gains a new initializer accepting a [`Formatter`](https://developer.apple.com/documentation/Foundation/Formatter). (63641785)
- `body` is now implicitly a [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) and [`body`](https://developer.apple.com/documentation/SwiftUI/App/body-swift.property) is now implicitly a [`SceneBuilder`](https://developer.apple.com/documentation/SwiftUI/SceneBuilder). (63606493)

## See Also

- [tvOS 14.7 Release Notes](tvos-14_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.6 Release Notes](tvos-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.5 Release Notes](tvos-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.4 Release Notes](tvos-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.3 Release Notes](tvos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.2 Release Notes](tvos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-14-release-notes)*