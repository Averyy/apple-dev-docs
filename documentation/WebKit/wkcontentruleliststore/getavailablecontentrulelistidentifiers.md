# getAvailableContentRuleListIdentifiers(_:)

**Framework**: Webkit  
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
@MainActor
func availableIdentifiers() async -> [String]?
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func availableIdentifiers() async -> [String]?
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func availableIdentifiers() async -> [String]?
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: A completion handler block to call with the results. This block has no return value and takes the following parameter:

## See Also

- [func lookUpContentRuleList(forIdentifier: String!, completionHandler: ((WKContentRuleList?, (any Error)?) -> Void)!)](wkcontentruleliststore/lookupcontentrulelist(foridentifier:completionhandler:).md)
  Searches asynchronously for a specific rule list in the data store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkcontentruleliststore/getavailablecontentrulelistidentifiers(_:))*