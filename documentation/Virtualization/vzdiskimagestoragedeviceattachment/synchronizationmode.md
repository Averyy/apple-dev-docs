# synchronizationMode

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The mode in which the disk image synchronizes data with the underlying storage device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var synchronizationMode: VZDiskImageSynchronizationMode { get }
```

```objc
@property (readonly) VZDiskImageSynchronizationMode synchronizationMode;
```

## See Also

### Getting the disk image details
- [var url: URL](./url.md)
  The URL of the underlying disk image.
- [var isReadOnly: Bool](./isreadonly.md)
  A Boolean value that indicates whether the underlying disk image is read-only.
- [var cachingMode: VZDiskImageCachingMode](./cachingmode.md)
  The current cacheing mode for the virtual disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/synchronizationmode)*