# removeContentRuleList(forIdentifier:completionHandler:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Removes a rule list from the current data store asynchronously.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func removeContentRuleList(forIdentifier identifier: String!, completionHandler: (((any Error)?) -> Void)!)
```

```swift
func removeContentRuleList(forIdentifier identifier: String!) async throws
```

```objc
- (void) removeContentRuleListForIdentifier:(NSString *) identifier completionHandler:(void (^)(NSError *)) completionHandler;
```

#### Discussion

This method also removes the persistent copy of the rules stored on disk.

## Parameters

- `identifier`: The unique identifier for the rule list.
- `completionHandler`: A completion handler block to call after the removal of the content rule list. This block has no return value and takes the following parameter:

  - **error**: `nil` on success, or an error object if the store encountered an error when deleting the rule list.

## See Also

### Creating and Deleting Content Rule Lists
- [func compileContentRuleList(forIdentifier: String!, encodedContentRuleList: String!, completionHandler: ((WKContentRuleList?, (any Error)?) -> Void)!)](./compilecontentrulelist%28foridentifier,encodedcontentrulelist,completionhandler%29.md)
  Compiles the specified JSON content into a new rule list and adds it to the current data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/removecontentrulelist(foridentifier:completionhandler:))*