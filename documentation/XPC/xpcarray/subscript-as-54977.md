# subscript(_:as:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this array as a file descriptor.

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
subscript(index: Int, as type: FileDescriptor.Type = FileDescriptor.self) -> FileDescriptor? { get }
```

#### Return Value

A file descriptor value or `nil` if no such value was found.

#### Overview

The returned file descriptor is owned by the caller so they must close it.

## Parameters

- `index`: The index at which to get the file descriptor.
- `type`: The expected type of the resulting value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcarray/subscript(_:as:)-54977)*