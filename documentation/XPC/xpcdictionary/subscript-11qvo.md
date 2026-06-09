# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this dictionary as a UUID.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript(key: String) -> uuid_t? { get set }
```

#### Return Value

A UUID value or `nil` if no such value was found.

## Parameters

- `key`: The key under which to get or set the UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:)-11qvo)*