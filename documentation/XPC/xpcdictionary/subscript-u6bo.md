# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this dictionary as an XPCArray.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
subscript(key: String) -> XPCArray? { get set }
```

#### Return Value

An XPCArray value or `nil` if no such value was found.

## Parameters

- `key`: The key under which to get or set the XPCArray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:)-u6bo)*