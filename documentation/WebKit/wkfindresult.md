# WKFindResult

**Framework**: Webkit  
**Kind**: class

An object that contains the results of searching the web view’s contents.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKFindResult
```

#### Overview

When you perform a search using the methods of [`WKWebView`](wkwebview.md), the web view creates a [`WKFindResult`](wkfindresult.md) object and delivers it to your completion handler. You don’t create instances of this class directly. Use the objects that the web view provides to determine whether it found a match for the content.

## Topics

### Getting the Search Result
- [var matchFound: Bool](wkfindresult/matchfound.md)
  A Boolean value that indicates whether the web view found a match during the search.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class WKFindConfiguration](wkfindconfiguration.md)
  The configuration parameters to use when searching the contents of the web view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindresult)*