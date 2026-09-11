# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this dictionary as a file descriptor.

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
subscript(key: String) -> FileDescriptor? { get set }
```

#### Return Value

A file descriptor value or `nil` if no such value was found.

#### Overview

A file descriptor passed in will be duplicated so the caller must still close theirs. A returned file descriptor is owned by the caller so it must be closed.

## Parameters

- `key`: The key under which to get or set the file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:)-hl1w)*