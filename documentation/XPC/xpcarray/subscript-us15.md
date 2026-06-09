# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this array as data.

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
subscript(index: Int) -> RawSpan? { get set }
```

#### Return Value

A RawSpan of the data or `nil` if no such value was found.

## Parameters

- `index`: The index at which to get or set the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-us15)*