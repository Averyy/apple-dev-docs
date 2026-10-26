# WKWebExtension.WindowState

**Framework**: WebKit  
**Kind**: enum  
**Role**: Enumeration

Constants used by [`WKWebExtensionWindow`](../wkwebextensionwindow.md) to indicate possible states of a window.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
enum WindowState
```

```c
enum WKWebExtensionWindowState : NSInteger;
```

## Topics

### Enumeration Cases
- [WKWebExtension.WindowState.fullscreen](./windowstate/fullscreen.md)
  Indicates a window is in full-screen mode.
- [WKWebExtension.WindowState.maximized](./windowstate/maximized.md)
  Indicates a window is maximized.
- [WKWebExtension.WindowState.minimized](./windowstate/minimized.md)
  Indicates a window is minimized.
- [WKWebExtension.WindowState.normal](./windowstate/normal.md)
  Indicates a window is in its normal state.
### Initializers
- [init?(rawValue: Int)](./windowstate/init%28rawvalue%29.md)

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
- [WKWebExtension.WindowType](./windowtype.md)
  Constants used by [`WKWebExtensionWindow`](../wkwebextensionwindow.md) to indicate the type of a window.
- [WKWebExtensionTabChangedProperties](./tabchangedproperties.md)
  Constants the web extension controller and web extension context use to indicate tab changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/windowstate)*