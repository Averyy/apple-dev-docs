# find(_:configuration:)

**Framework**: Webkit  
**Kind**: method

Searches for the specified string in the web view’s content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func find(_ string: String, configuration: WKFindConfiguration = .init()) async throws -> WKFindResult
```

#### Return Value

The object that contains the results of the search.

## Parameters

- `string`: The search string to use.
- `configuration`: The search parameters. Use this object to specify whether the search is case sensitive, whether it moves forward or backward, and whether it wraps when it reaches the end of the page.

## See Also

- [func find(String, configuration: WKFindConfiguration, completionHandler: (WKFindResult) -> Void)](wkwebview/find(_:configuration:completionhandler:).md)
  Searches for the specified string in the web view’s content.
- [class WKFindConfiguration](wkfindconfiguration.md)
  The configuration parameters to use when searching the contents of the web view.
- [class WKFindResult](wkfindresult.md)
  An object that contains the results of searching the web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/find(_:configuration:))*