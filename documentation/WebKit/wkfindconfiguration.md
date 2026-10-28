# WKFindConfiguration

**Framework**: WebKit  
**Kind**: class  
**Role**: Class

The configuration parameters to use when searching the contents of the web view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class WKFindConfiguration
```

```objc
@interface WKFindConfiguration : NSObject
```

## Overview

Create a [`WKFindConfiguration`](./wkfindconfiguration.md) object and configure its attributes to specify how to perform searches within the web view’s contents. To initiate a search, call the appropriate method of [`WKWebView`](./wkwebview.md) and pass this object along with the search string.

## Topics

### Configuring the Search Parameters
- [var backwards: Bool](./wkfindconfiguration/backwards.md)
  A Boolean value that indicates the search direction, relative to the current selection.
- [var caseSensitive: Bool](./wkfindconfiguration/casesensitive.md)
  A Boolean value that indicates whether to consider case when matching the search string.
- [var wraps: Bool](./wkfindconfiguration/wraps.md)
  A Boolean value that indicates whether the search wraps around to the other side of the page.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Related Documentation
- [func find(String, configuration: WKFindConfiguration, completionHandler: (WKFindResult) -> Void)](./wkwebview/find%28_,configuration,completionhandler%29.md)
  Searches for the specified string in the web view’s content.
- [- findString:withConfiguration:completionHandler:](./wkwebview/findstring_withconfiguration_completionhandler_.md)
  Searches for the specified string in the web view’s content.
### Page-level search
- [class WKFindResult](./wkfindresult.md)
  An object that contains the results of searching the web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkfindconfiguration)*