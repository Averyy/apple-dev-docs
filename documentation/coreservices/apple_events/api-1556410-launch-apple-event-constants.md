# Launch Apple Event Constants

**Framework**: Core Services

In a `kAEOpenApplication` event, specify information about how the receiving application was launched.

#### Overview

Although these constants were not publicly defined in OS X version 10.4, corresponding information was provided in `kAEOpenApplication` Apple events sent by that version of the OS. Therefore your application, running in macOS 10.4 or later, can examine the open application Apple event to determine if the application was launched as a login item or a service item. However, for version 10.4, you will have to define these constants in your own code file.

You check for a `keyAEPropData` parameter of the `kAEOpenApplication` Apple event, with a data value that matches `keyAELaunchedAsLogInItem` or `keyAELaunchedAsServiceItem`.

## Topics

### Constants
- [var keyAELaunchedAsLogInItem: AEKeyword](keyaelaunchedasloginitem.md)
  If present in a `kAEOpenApplication` event, the receiving application was launched as a login item and should only perform actions suitable to that environment—for example, it probably shouldn't open an untitled document.
- [var keyAELaunchedAsServiceItem: AEKeyword](keyaelaunchedasserviceitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/apple_events/1556410-launch_apple_event_constants)*