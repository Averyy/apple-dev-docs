# WKWebExtension.WindowType

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Constants used by [`WKWebExtensionWindow`](../wkwebextensionwindow.md) to indicate the type of a window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum WindowType
```

```c
enum WKWebExtensionWindowType : NSInteger;
```

## Topics

### Enumeration Cases
- [WKWebExtension.WindowType.normal](./windowtype/normal.md)
  Indicates a normal window.
- [WKWebExtension.WindowType.popup](./windowtype/popup.md)
  Indicates a pop-up window.
### Initializers
- [init?(rawValue: Int)](./windowtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [WKWebExtension.WindowState](./windowstate.md)
  Constants used by [`WKWebExtensionWindow`](../wkwebextensionwindow.md) to indicate possible states of a window.
- [WKWebExtensionTabChangedProperties](./tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowtype)*