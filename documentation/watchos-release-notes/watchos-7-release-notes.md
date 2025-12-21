# watchOS 7 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 7 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 7. The SDK comes bundled with Xcode 12, available from the Mac App Store. For information on the compatibility requirements for Xcode 12, see [`Xcode 12 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-12-release-notes).

##### Clock

###### Known Issues

- Kaleidoscope faces created using the Photos app on watchOS 7 beta 4 or earlier might cause your watch to repeatedly restart unexpectedly. (65224164)  Use the Watch app on your phone to remove the Kaleidoscope face.
- Watch faces created using watchOS 7 beta 5 and earlier are no longer compatible with watchOS. Use watchOS 7 beta 6 or later to generate new `.watchface` files. (66592614)
- If you added a Sleep complication to a Watch face in watchOS 7 beta, it might disappear after updating to watchOS 7 beta 2 or later. (63699282)  Add the Sleep complication again.
- The Sleep complication might appear twice in the complication picker when editing a Watch face. (64709508)  Remove the Sleep app, then reinstall it using App Store on your watch.

##### Logging

###### New Features

- New APIs are available for using `os_log` from Swift as part of the framework [`os`](https://developer.apple.com/documentation/os). A new type, [`Logger`](https://developer.apple.com/documentation/os/Logger), can be instantiated using a subsystem and category and provides methods for logging at different levels (`Logger.debug`, `Logger.error`, `Logger.fault`).
- The [`Logger`](https://developer.apple.com/documentation/os/Logger) APIs support specifying most formatting and privacy options supported by legacy `os_log` APIs. The new APIs provide significant performance improvements over the legacy APIs. You can now pass Swift string interpolation to the `os_log` function.  The new APIs can’t be back deployed; however, the existing `os_log` API remains available for back deployment. (22539144)

##### Networking

###### New Features

- [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) metrics support is now available. (29448748)

##### Software Update

###### Known Issues

- You might be unable to update Apple Watch Series 3 to watchOS 7 due to limited storage. (64793483)  Unpair your watch, then pair it again with your phone. Set it up as a new watch rather than restoring from a backup. Use General > Software Update in the Watch app to update to watchOS 7. If you want to restore your watch from its latest backup after the update is complete, repeat these steps while choosing to restore from a backup rather than setting up as new.

##### Swiftui

###### New Features

- [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) can be converted to and from [`cgColor`](https://developer.apple.com/documentation/UIKit/UIColor/cgColor). The [`ColorPicker`](https://developer.apple.com/documentation/SwiftUI/ColorPicker) can also now be configured with a binding to a `CGColor`. (56939085)
- Introduced [`ToolbarItemGroup`](https://developer.apple.com/documentation/SwiftUI/ToolbarItemGroup) as a convenient way to place multiple items in a specific location of non-customizable toolbars. (64178863)
- [`ProgressView`](https://developer.apple.com/documentation/SwiftUI/ProgressView) now supports adding a secondary “current value label” that describes the current progress level of the task. Use the [`label`](https://developer.apple.com/documentation/SwiftUI/ProgressViewStyleConfiguration/label-swift.property) to describe the overall task, and the [`currentValueLabel`](https://developer.apple.com/documentation/SwiftUI/ProgressViewStyleConfiguration/currentValueLabel-swift.property) to provide more specific details about the progress of the task. (63580200)
- [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) is now redacted when the `redacted(reason:)` modifier is applied. (65047189)
- [`InlinePickerStyle`](https://developer.apple.com/documentation/SwiftUI/InlinePickerStyle) is now available and allows a [`Picker`](https://developer.apple.com/documentation/SwiftUI/Picker) to appear in-line with the rest of the content in its surrounding container. The style will adapt its appearance for different containers and platforms, such as individual menu items in a menu. (59868844)
- [`List`](https://developer.apple.com/documentation/SwiftUI/List) may now be used with [`ScrollViewReader`](https://developer.apple.com/documentation/SwiftUI/ScrollViewReader). (35471164)
- [`Text`](https://developer.apple.com/documentation/SwiftUI/Text) gains a new initializer accepting a [`Formatter`](https://developer.apple.com/documentation/Foundation/Formatter). (63641785)
- `body` is now implicitly a [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) and [`body`](https://developer.apple.com/documentation/SwiftUI/App/body-swift.property) is now implicitly a [`SceneBuilder`](https://developer.apple.com/documentation/SwiftUI/SceneBuilder). (63606493)

## See Also

- [watchOS 7.6 Release Notes](watchos-7_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.5 Release Notes](watchos-7_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.4 Release Notes](watchos-7_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.3 Release Notes](watchos-7_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.2 Release Notes](watchos-7_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.1 Release Notes](watchos-7_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-7-release-notes)*