# getAvailableContentRuleListIdentifiers(_:)

**Framework**: WebKit  
**Kind**: method

Fetches the identifiers for all rule lists in the store asynchronously.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func availableIdentifiers() async -> [String]?
```

## Parameters

- `completionHandler`: A completion handler block to call with the results. This block has no return value and takes the following parameter: - **identifierArray**: An array of strings, each of which corresponds to an identifier for a rule list in the data store. Use each string to look up the associated [`WKContentRuleList`](wkcontentrulelist.md) object. If the data store has no rule lists, the array is empty.

## See Also

- [func lookUpContentRuleList(forIdentifier: String!, completionHandler: ((WKContentRuleList?, (any Error)?) -> Void)!)](wkcontentruleliststore/lookupcontentrulelist(foridentifier:completionhandler:).md)
  Searches asynchronously for a specific rule list in the data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/getavailablecontentrulelistidentifiers(_:))*