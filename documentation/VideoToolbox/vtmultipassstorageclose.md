# VTMultiPassStorageClose(_:)

**Framework**: Videotoolbox  
**Kind**: func

Ensures that any pending data is written to the multipass storage file and closes the file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTMultiPassStorageClose(_ multiPassStorage: VTMultiPassStorage) -> OSStatus
```

#### Discussion

After this function is called, all functions on the multipass storage object fail. It’s still necessary to release the object by calling [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease).

## Parameters

- `multiPassStorage`: The multipass storage object to close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmultipassstorageclose(_:))*