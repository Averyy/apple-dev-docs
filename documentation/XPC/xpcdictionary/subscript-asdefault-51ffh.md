# subscript(_:as:default:)

**Framework**: XPC  
**Kind**: subscript

Get a value in this dictionary as a file descriptor.

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
subscript(key: String, as type: FileDescriptor.Type = FileDescriptor.self, default defaultValue: @autoclosure () -> FileDescriptor) -> FileDescriptor { get }
```

#### Return Value

A file descriptor value, possibly `defaultValue`.

#### Overview

The returned file descriptor is owned by the caller so they must close it.

## Parameters

- `key`: The key under which to get the file descriptor.
- `type`: The expected type of the resulting value.
- `defaultValue`: The value to produce if no file descriptor is available under `key`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcdictionary/subscript(_:as:default:)-51ffh)*