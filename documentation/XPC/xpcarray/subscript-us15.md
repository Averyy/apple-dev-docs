# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this array as data.

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
subscript(index: Int) -> RawSpan? { get set }
```

#### Return Value

A RawSpan of the data or `nil` if no such value was found.

## Parameters

- `index`: The index at which to get or set the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-us15)*