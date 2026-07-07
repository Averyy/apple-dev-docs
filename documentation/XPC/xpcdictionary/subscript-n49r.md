# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this dictionary as data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript(key: String) -> RawSpan? { get set }
```

#### Return Value

A RawSpan of the data or `nil` if no such value was found.

## Parameters

- `key`: The key under which to get or set the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:)-n49r)*