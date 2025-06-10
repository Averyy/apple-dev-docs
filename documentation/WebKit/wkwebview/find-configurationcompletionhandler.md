# find(_:configuration:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Searches for the specified string in the web view’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func find(_ string: String, configuration: WKFindConfiguration = .init(), completionHandler: @escaping @MainActor (WKFindResult) -> Void)
```

## Parameters

- `string`: The search string to use.
- `configuration`: The search parameters. Use this object to specify whether the search is case sensitive, whether it moves forward or backward, and whether it wraps when it reaches the end of the page.
- `completionHandler`: The completion handler to call with the results of the search. This handler has no return value and takes the following parameter:

## See Also

- [func find(String, configuration: WKFindConfiguration) async throws -> WKFindResult](wkwebview/find(_:configuration:).md)
  Searches for the specified string in the web view’s content.
- [class WKFindConfiguration](wkfindconfiguration.md)
  The configuration parameters to use when searching the contents of the web view.
- [class WKFindResult](wkfindresult.md)
  An object that contains the results of searching the web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/find(_:configuration:completionhandler:))*