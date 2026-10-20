# WidgetCenter.UserInfoKey

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

An object that defines keys for accessing information in a user info dictionary.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
struct UserInfoKey
```

#### Overview

> **Note**: In Objective-C, use [`WGWidgetUserInfoKeyFamily`](../wgwidgetuserinfokeyfamily.md) and [`WGWidgetUserInfoKeyKind`](../wgwidgetuserinfokeykind.md) instead.

## Topics

### Describing a widget
- [static let family: String](./userinfokey/family.md)
  A key you use to access the widget’s family.
- [static let kind: String](./userinfokey/kind.md)
  A key you use to access the widget’s kind. The value matches the `kind` property specified in the widget’s configuration.
### Describing a Live Activity
- [static let activityID: String](./userinfokey/activityid.md)
  A key you use to access the activity ID if the widget represents a Live Activity.

## See Also

### Getting Widget Information
- [static let shared: WidgetCenter](./shared.md)
  The shared widget center.
- [func getCurrentConfigurations((Result<[WidgetInfo], any Error>) -> Void)](./getcurrentconfigurations%28_%29.md)
  Retrieves information about user-configured widgets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetcenter/userinfokey)*