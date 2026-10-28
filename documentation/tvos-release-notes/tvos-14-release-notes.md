# tvOS 14 Release Notes

**Framework**: tvOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The tvOS 14 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 14. The SDK comes bundled with Xcode 12. For information on the compatibility requirements for Xcode 12, see [Xcode 12 Release Notes](../Xcode-Release-Notes/xcode-12-release-notes.md).

### AVKit

#### New Features

- Picture in Picture on tvOS allows for simultaneous video playback and the ability to swap between full-screen content and Picture in Picture. Use [`AVPlayerViewController`](../AVKit/avplayerviewcontroller.md) for adopting Picture in Picture in a standard player or AVKit framework’s [`AVPictureInPictureController`](../AVKit/avpictureinpicturecontroller.md) class for your custom player. (54986706)

### Game Center

#### New Features

- With multiuser support for gaming, your game can switch dynamically between users, and use both Game Center and iCloud to keep track of multiple players’ individual game levels, leaderboards, and invitations. The User Management entitlement has been expanded to include `runs-as-current-user`. This new value grants access to a separate set of data for your app for each user from Game Center, iCloud, and local storage. (56116380)

### Logging

#### New Features

- New APIs are available for using `os_log` from Swift as part of the framework `os`:

  - A new type, [`Logger`](../os/logger.md), can be instantiated using a subsystem and category, and provides methods for logging at different levels (`Logger.debug`, `Logger.error`, `Logger.fault`).
  - The `Logger` APIs support specifying most formatting and privacy options supported by legacy  [Logging](../os/logging.md) APIs.
  - The new APIs provide significant performance improvements over the legacy APIs.
  - You can now pass Swift string interpolation to the [`os_log`](../os/os_log.md) function.

  **Note:** The new APIs can’t be back deployed; however, the existing `os_log` API remains available for back deployment. (22539144)

### SwiftUI

#### New Features

- [`ProgressView`](../SwiftUI/progressview.md) now supports adding a secondary “current value label” that describes the current progress level of the task. Use the [`label`](../SwiftUI/progressviewstyleconfiguration/label-swift.property.md) to describe the overall task, and the [`ProgressViewStyleConfiguration.CurrentValueLabel`](../SwiftUI/progressviewstyleconfiguration/currentvaluelabel-swift.struct.md) to provide more specific details about the progress of the task. (63580200)
- Introduced [`ToolbarItemGroup`](../SwiftUI/toolbaritemgroup.md) as a convenient way to place multiple items in a specific location of non-customizable toolbars. (64178863)
- [`Color`](../SwiftUI/color.md) can be converted to and from [`cgColor`](../UIKit/uicolor/cgcolor.md). The [`ColorPicker`](../SwiftUI/colorpicker.md) can also now be configured with a binding to a `CGColor`. (56939085)
- [`Image`](../SwiftUI/image.md) is now redacted when the `redacted(reason:)` modifier is applied. (65047189)
- [`InlinePickerStyle`](../SwiftUI/inlinepickerstyle.md) is now available and allows a [`Picker`](../SwiftUI/picker.md) to appear in-line with the rest of the content in its surrounding container. The style will adapt its appearance for different containers and platforms, such as individual menu items in a menu. (59868844)
- [`List`](../SwiftUI/list.md) may now be used with [`ScrollViewReader`](../SwiftUI/scrollviewreader.md). (35471164)
- [`Text`](../SwiftUI/text.md) gains a new initializer accepting a [`Formatter`](../Foundation/formatter.md). (63641785)
- `body` is now implicitly a [`ViewBuilder`](../SwiftUI/viewbuilder.md) and [`body`](../SwiftUI/app/body-swift.property.md) is now implicitly a [`SceneBuilder`](../SwiftUI/scenebuilder.md). (63606493)

## See Also

### tvOS 14
- [tvOS 14.7 Release Notes](./tvos-14_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.6 Release Notes](./tvos-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.5 Release Notes](./tvos-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.4 Release Notes](./tvos-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.3 Release Notes](./tvos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 14.2 Release Notes](./tvos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-14-release-notes)*