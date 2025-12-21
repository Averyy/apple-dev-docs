# lookUpContentRuleList(forIdentifier:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Searches asynchronously for a specific rule list in the data store.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentRuleList(forIdentifier identifier: String!) async throws -> WKContentRuleList?
```

## Parameters

- `identifier`: The identifier of the list you want.
- `completionHandler`: A completion handler block to call with the results of the search. This block has no return value and takes the following parameters:

## See Also

- [func getAvailableContentRuleListIdentifiers((([String]?) -> Void)!)](wkcontentruleliststore/getavailablecontentrulelistidentifiers(_:).md)
  Fetches the identifiers for all rule lists in the store asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/lookupcontentrulelist(foridentifier:completionhandler:))*