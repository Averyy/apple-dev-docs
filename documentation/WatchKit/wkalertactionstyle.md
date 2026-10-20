# WKAlertActionStyle

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the style of the action button.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
enum WKAlertActionStyle
```

```c
enum WKAlertActionStyle : NSInteger;
```

## Topics

### Constants
- [WKAlertActionStyle.default](./wkalertactionstyle/default.md)
  The default style. Use this for most of your buttons.
- [WKAlertActionStyle.cancel](./wkalertactionstyle/cancel.md)
  A cancel action. Use this style for an action that cancels the operation without making changes.
- [WKAlertActionStyle.destructive](./wkalertactionstyle/destructive.md)
  An action that causes destructive behavior to the user’s data or the app. Destructive actions are styled in a way that warns the user of the destructive nature of the action.
### Initializers
- [init?(rawValue: Int)](./wkalertactionstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [typealias WKAlertActionHandler](./wkalertactionhandler.md)
  A block to perform in response to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkalertactionstyle)*