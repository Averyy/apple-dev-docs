# getCurrentConfigurations(_:)

**Framework**: WidgetKit  
**Kind**: method

Retrieves information about user-configured widgets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
func getCurrentConfigurations(_ completion: @escaping (Result<[WidgetInfo], any Error>) -> Void)
```

## Mentions

- [Making a configurable widget](making-a-configurable-widget.md)

## Parameters

- `completion`: A completion handler called when the widget   information is available.

## See Also

- [static let shared: WidgetCenter](widgetcenter/shared.md)
  The shared widget center.
- [WidgetCenter.UserInfoKey](widgetcenter/userinfokey.md)
  An object that defines keys for accessing information in a user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetcenter/getcurrentconfigurations(_:))*