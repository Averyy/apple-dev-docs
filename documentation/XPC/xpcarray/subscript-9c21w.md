# subscript(_:)

**Framework**: XPC  
**Kind**: subscript

Get or set a value in this array as a file descriptor.

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
subscript(index: Int) -> FileDescriptor? { get set }
```

#### Return Value

A file descriptor value or `nil` if no such value was found.

#### Overview

A file descriptor passed in will be duplicated so the caller must still close theirs. A returned file descriptor is owned by the caller so it must be closed.

## Parameters

- `index`: The index at which to get or set the file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:)-9c21w)*