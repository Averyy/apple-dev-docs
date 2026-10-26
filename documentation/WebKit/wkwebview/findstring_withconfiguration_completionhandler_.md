# findString:withConfiguration:completionHandler:

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Searches for the specified string in the web view’s content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```objc
- (void) findString:(NSString *) string withConfiguration:(WKFindConfiguration *) configuration completionHandler:(void (^)(WKFindResult *)) completionHandler;
```

## Parameters

- `string`: The search string to use.
- `configuration`: The search parameters. Use this object to specify whether the search is case-sensitive, moves forward or backward, and wraps when it reaches the end of the page.
- `completionHandler`: The completion handler to call with the results of the search. This handler has no return value and takes the following parameter:

  - **result**: The object that contains the results of the search.

## See Also

### Searching the current page’s content
- [class WKFindConfiguration](../wkfindconfiguration.md)
  The configuration parameters to use when searching the contents of the web view.
- [class WKFindResult](../wkfindresult.md)
  An object that contains the results of searching the web view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebview/findstring:withconfiguration:completionhandler:)*