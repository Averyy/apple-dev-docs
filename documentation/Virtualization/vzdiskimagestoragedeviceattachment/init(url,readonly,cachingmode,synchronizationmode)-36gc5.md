# init(url:readOnly:cachingMode:synchronizationMode:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initialize the attachment from a local file URL.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(url: URL, readOnly: Bool, cachingMode: VZDiskImageCachingMode, synchronizationMode: VZDiskImageSynchronizationMode) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) url readOnly:(BOOL) readOnly cachingMode:(VZDiskImageCachingMode) cachingMode synchronizationMode:(VZDiskImageSynchronizationMode) synchronizationMode error:(NSError **) error;
```

## Parameters

- `url`: Local file URL to the disk image in RAW format.
- `readOnly`: If `true`, the device attachment is read-only, otherwise the device can write data to the disk image.
- `cachingMode`: The cacheing mode from one of the available [`VZDiskImageCachingMode`](../vzdiskimagecachingmode.md) options.
- `synchronizationMode`: How the disk image synchronizes with the underlying storage when the guest operating system flushes data, described by one of the available [`VZDiskImageSynchronizationMode`](../vzdiskimagesynchronizationmode.md) modes.

## See Also

### Creating the attachment point
- [init(url: URL, readOnly: Bool) throws](./init%28url,readonly%29-9qeco.md)
  Creates the attachment object from the specified disk image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(url:readonly:cachingmode:synchronizationmode:)-36gc5)*