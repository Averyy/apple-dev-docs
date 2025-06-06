# WidgetCenter.UserInfoKey

**Framework**: Widgetkit  
**Kind**: struct

An object that defines keys for accessing information in a user info dictionary.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- watchOS 9.0+

## Declaration

```swift
struct UserInfoKey
```

#### Overview

> **Note**: In Objective-C, use [`WGWidgetUserInfoKeyFamily`](wgwidgetuserinfokeyfamily.md) and [`WGWidgetUserInfoKeyKind`](wgwidgetuserinfokeykind.md) instead.

In Objective-C, use [`WGWidgetUserInfoKeyFamily`](wgwidgetuserinfokeyfamily.md) and [`WGWidgetUserInfoKeyKind`](wgwidgetuserinfokeykind.md) instead.

## Topics

### Describing a widget
- [static let family: String](widgetcenter/userinfokey/family.md)
  A key you use to access the widget’s family.
- [static let kind: String](widgetcenter/userinfokey/kind.md)
  A key you use to access the widget’s kind. The value matches the `kind` property specified in the widget’s configuration.
### Describing a Live Activity
- [static let activityID: String](widgetcenter/userinfokey/activityid.md)
  A key you use to access the activity ID if the widget represents a Live Activity.

## See Also

- [static let shared: WidgetCenter](widgetcenter/shared.md)
  The shared widget center.
- [func getCurrentConfigurations((Result<[WidgetInfo], any Error>) -> Void)](widgetcenter/getcurrentconfigurations(_:).md)
  Retrieves information about user-configured widgets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetcenter/userinfokey)*