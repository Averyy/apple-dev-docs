# removeContentRuleList(forIdentifier:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Removes a rule list from the current data store asynchronously.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeContentRuleList(forIdentifier identifier: String!) async throws
```

#### Discussion

This method also removes the persistent copy of the rules stored on disk.

## Parameters

- `identifier`: The unique identifier for the rule list.
- `completionHandler`: A completion handler block to call after the removal of the content rule list. This block has no return value and takes the following parameter:

## See Also

- [func compileContentRuleList(forIdentifier: String!, encodedContentRuleList: String!, completionHandler: ((WKContentRuleList?, (any Error)?) -> Void)!)](wkcontentruleliststore/compilecontentrulelist(foridentifier:encodedcontentrulelist:completionhandler:).md)
  Compiles the specified JSON content into a new rule list and adds it to the current data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/removecontentrulelist(foridentifier:completionhandler:))*