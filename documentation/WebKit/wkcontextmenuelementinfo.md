# WKContextMenuElementInfo

**Framework**: WebKit  
**Kind**: class

An object that contains information about a link the user clicked in a webpage, and which you use to configure a context menu for that link.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKContextMenuElementInfo
```

#### Overview

A [`WKContextMenuElementInfo`](wkcontextmenuelementinfo.md) object contains the URL of a link in the web view’s content. You don’t create instances of this class directly. Instead, the web view creates them and passes them to the methods of its associated [`WKUIDelegate`](wkuidelegate.md) object when the user interacts with the link. In your delegate method implementations, use the URL in this object to determine how to configure the contextual menu.

## Topics

### Getting the Element Information
- [var linkURL: URL?](wkcontextmenuelementinfo/linkurl.md)
  The URL of the link that the user clicked.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontextmenuelementinfo)*