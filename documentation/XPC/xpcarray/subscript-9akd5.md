# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this array as a UUID.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript(index: Int) -> uuid_t? { get set }
```

#### Return Value

A UUID value or `nil` if no such value was found.

## Parameters

- `index`: The index at which to get or set the UUID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-9akd5)*