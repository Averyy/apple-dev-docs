# NSAttributedStringCompletionHandler

**Framework**: WebKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```c
typedef void (^)(NSAttributedString *, NSDictionary<NSString *,id> *, NSError *) NSAttributedStringCompletionHandler;
```

## Discussion

Document-Level attributes, like NSBackgroundColorDocumentAttribute, or an error. An implementation of this block type must expect to be called asynchronously when passed to HTML loading methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/nsattributedstringcompletionhandler)*