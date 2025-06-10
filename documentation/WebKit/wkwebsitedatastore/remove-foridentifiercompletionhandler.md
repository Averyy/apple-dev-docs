# remove(forIdentifier:completionHandler:)

**Framework**: WebKit  
**Kind**: method

Removes the data store that matches the identifier you provide.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class func remove(forIdentifier identifier: UUID) async throws
```

#### Discussion

Call this method to remove the data store for the unique identifier. Release any [`WKWebView`](wkwebview.md) instances using the data store before you call this method. If the system cannot complete removal of the data store, this throws an error.

## Parameters

- `identifier`: An identifier that uniquely identifies a data store.
- `completionHandler`: A block the system invokes after it removes the data store. This block has no return value, and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/remove(foridentifier:completionhandler:))*