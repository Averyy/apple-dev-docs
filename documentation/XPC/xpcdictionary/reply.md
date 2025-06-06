# reply(_:)

**Framework**: Xpc  
**Kind**: method

Sends a reply to the originator of the dictionary.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func reply(_ reply: XPCDictionary)
```

#### Discussion

When a listener receives an [`XPCDictionary`](xpcdictionary.md), the dictionary keeps track of the client that sent it. This function sends the specified `reply` dictionary back to the originating client.

Don’t call this function more than once on a single dictionary, and don’t call it on a dictionary that wasn’t received from a client. Calling it more than once or sending a reply using a dictionary that wasn’t received triggers an API misuse crash.

## Parameters

- `reply`: A dictionary to send back to the client that sent the receiving dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/reply(_:))*