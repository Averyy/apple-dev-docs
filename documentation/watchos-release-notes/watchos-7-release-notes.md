# watchOS 7 Release Notes

**Framework**: watchOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The watchOS 7 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 7. The SDK comes bundled with Xcode 12. For information on the compatibility requirements for Xcode 12, see [Xcode 12 Release Notes](../Xcode-Release-Notes/xcode-12-release-notes.md).

### Clock

#### Known Issues

- Kaleidoscope faces created using the Photos app on watchOS 7 beta 4 or earlier might cause your watch to repeatedly restart unexpectedly. (65224164)

  **Workaround:** Use the Watch app on your phone to remove the Kaleidoscope face.
- Watch faces created using watchOS 7 beta 5 and earlier are no longer compatible with watchOS. Use watchOS 7 beta 6 or later to generate new `.watchface` files. (66592614)
- If you added a Sleep complication to a Watch face in watchOS 7 beta, it might disappear after updating to watchOS 7 beta 2 or later. (63699282)

  **Workaround:** Add the Sleep complication again.
- The Sleep complication might appear twice in the complication picker when editing a Watch face. (64709508)

  **Workaround:** Remove the Sleep app, then reinstall it using App Store on your watch.

### Logging

#### New Features

- New APIs are available for using `os_log` from Swift as part of the framework [os](../os/os.md). A new type, [`Logger`](../os/logger.md), can be instantiated using a subsystem and category and provides methods for logging at different levels (`Logger.debug`, `Logger.error`, `Logger.fault`).
- The [`Logger`](../os/logger.md) APIs support specifying most formatting and privacy options supported by legacy `os_log` APIs. The new APIs provide significant performance improvements over the legacy APIs. You can now pass Swift string interpolation to the `os_log` function.

  **Note:** The new APIs can’t be back deployed; however, the existing `os_log` API remains available for back deployment. (22539144)

### Networking

#### New Features

- [`URLSession`](../Foundation/urlsession.md) metrics support is now available. (29448748)

### Software Update

#### Known Issues

- You might be unable to update Apple Watch Series 3 to watchOS 7 due to limited storage. (64793483)

  **Workaround:** Unpair your watch, then pair it again with your phone. Set it up as a new watch rather than restoring from a backup. Use General > Software Update in the Watch app to update to watchOS 7. If you want to restore your watch from its latest backup after the update is complete, repeat these steps while choosing to restore from a backup rather than setting up as new.

### SwiftUI

#### New Features

- [`Color`](../SwiftUI/color.md) can be converted to and from [`cgColor`](../UIKit/uicolor/cgcolor.md). The [`ColorPicker`](../SwiftUI/colorpicker.md) can also now be configured with a binding to a `CGColor`. (56939085)
- Introduced [`ToolbarItemGroup`](../SwiftUI/toolbaritemgroup.md) as a convenient way to place multiple items in a specific location of non-customizable toolbars. (64178863)
- [`ProgressView`](../SwiftUI/progressview.md) now supports adding a secondary “current value label” that describes the current progress level of the task. Use the [`label`](../SwiftUI/progressviewstyleconfiguration/label-swift.property.md) to describe the overall task, and the [`currentValueLabel`](../SwiftUI/progressviewstyleconfiguration/currentvaluelabel-swift.property.md) to provide more specific details about the progress of the task. (63580200)
- [`Image`](../SwiftUI/image.md) is now redacted when the `redacted(reason:)` modifier is applied. (65047189)
- [`InlinePickerStyle`](../SwiftUI/inlinepickerstyle.md) is now available and allows a [`Picker`](../SwiftUI/picker.md) to appear in-line with the rest of the content in its surrounding container. The style will adapt its appearance for different containers and platforms, such as individual menu items in a menu. (59868844)
- [`List`](../SwiftUI/list.md) may now be used with [`ScrollViewReader`](../SwiftUI/scrollviewreader.md). (35471164)
- [`Text`](../SwiftUI/text.md) gains a new initializer accepting a [`Formatter`](../Foundation/formatter.md). (63641785)
- `body` is now implicitly a [`ViewBuilder`](../SwiftUI/viewbuilder.md) and [`body`](../SwiftUI/app/body-swift.property.md) is now implicitly a [`SceneBuilder`](../SwiftUI/scenebuilder.md). (63606493)

## See Also

### watchOS 7
- [watchOS 7.6 Release Notes](./watchos-7_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.5 Release Notes](./watchos-7_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.4 Release Notes](./watchos-7_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.3 Release Notes](./watchos-7_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.2 Release Notes](./watchos-7_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 7.1 Release Notes](./watchos-7_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-7-release-notes)*