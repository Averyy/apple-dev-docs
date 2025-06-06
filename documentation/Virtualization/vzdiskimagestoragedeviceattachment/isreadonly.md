# isReadOnly

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the underlying disk image is read-only.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var isReadOnly: Bool { get }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the guest operating system may read the contents of the disk image, but may not write to it.

## See Also

- [var url: URL](vzdiskimagestoragedeviceattachment/url.md)
  The URL of the underlying disk image.
- [var cachingMode: VZDiskImageCachingMode](vzdiskimagestoragedeviceattachment/cachingmode.md)
  The current cacheing mode for the virtual disk image.
- [var synchronizationMode: VZDiskImageSynchronizationMode](vzdiskimagestoragedeviceattachment/synchronizationmode.md)
  The mode in which the disk image synchronizes data with the underlying storage device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/isreadonly)*