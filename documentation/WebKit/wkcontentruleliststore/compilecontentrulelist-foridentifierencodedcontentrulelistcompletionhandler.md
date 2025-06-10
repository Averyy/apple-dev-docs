# compileContentRuleList(forIdentifier:encodedContentRuleList:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Compiles the specified JSON content into a new rule list and adds it to the current data store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func compileContentRuleList(forIdentifier identifier: String!, encodedContentRuleList: String!) async throws -> WKContentRuleList?
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func compileContentRuleList(forIdentifier identifier: String!, encodedContentRuleList: String!) async throws -> WKContentRuleList?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `identifier`: A unique identifier for the new list. If a list with the specified identifier already exists in the store, this method overwrites the old rule list with the new content.
- `encodedContentRuleList`: The JSON source for the new rule list. For information about how to format the JSON content, see  .
- `completionHandler`: A completion handler block to call after compilation finishes. This block has no return value and takes the following parameters:

## See Also

- [func removeContentRuleList(forIdentifier: String!, completionHandler: (((any Error)?) -> Void)!)](wkcontentruleliststore/removecontentrulelist(foridentifier:completionhandler:).md)
  Removes a rule list from the current data store asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/compilecontentrulelist(foridentifier:encodedcontentrulelist:completionhandler:))*