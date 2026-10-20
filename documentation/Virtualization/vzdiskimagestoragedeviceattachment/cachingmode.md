# cachingMode

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The current cacheing mode for the virtual disk image.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var cachingMode: VZDiskImageCachingMode { get }
```

```objc
@property (readonly) VZDiskImageCachingMode cachingMode;
```

## See Also

### Getting the disk image details
- [var url: URL](./url.md)
  The URL of the underlying disk image.
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether the underlying disk image is read-only.
- [var synchronizationMode: VZDiskImageSynchronizationMode](./synchronizationmode.md)
  The mode in which the disk image synchronizes data with the underlying storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/cachingmode)*