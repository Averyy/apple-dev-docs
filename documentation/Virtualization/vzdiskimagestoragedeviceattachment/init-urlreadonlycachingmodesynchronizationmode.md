# init(url:readOnly:cachingMode:synchronizationMode:)

**Framework**: Virtualization  
**Kind**: init

Initialize the attachment from a local file URL.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(url: URL, readOnly: Bool, cachingMode: VZDiskImageCachingMode, synchronizationMode: VZDiskImageSynchronizationMode) throws
```

## Parameters

- `url`: Local file URL to the disk image in RAW format.
- `readOnly`: If  , the device attachment is read-only, otherwise the device can write data to the disk image.
- `cachingMode`: The cacheing mode from one of the available   options.
- `synchronizationMode`: How the disk image synchronizes with the underlying storage when the guest operating system flushes data, described by one of the available   modes.

## See Also

- [init(url: URL, readOnly: Bool) throws](vzdiskimagestoragedeviceattachment/init(url:readonly:).md)
  Creates the attachment object from the specified disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(url:readonly:cachingmode:synchronizationmode:))*