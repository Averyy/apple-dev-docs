# init(url:readOnly:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Creates the attachment object from the specified disk image.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(url: URL, readOnly: Bool) throws
```

```objc
- (instancetype) initWithURL:(NSURL *) url readOnly:(BOOL) readOnly error:(NSError **) error;
```

## Return Value

In Swift the methods returns an attachment object; in Objective-C the methods returns an attachment object on success, or `nil` if an error occurred

## Parameters

- `url`: A URL that points to a local disk image in RAW format.
- `readOnly`: A Boolean that indicates whether to configure the disk image as read-only. Specify [`true`](../../Swift/true.md) to prevent the guest operating system from writing to the disk image, and [`false`](../../Swift/false.md) to allow writing.

## See Also

### Creating the attachment point
- [init(url: URL, readOnly: Bool, cachingMode: VZDiskImageCachingMode, synchronizationMode: VZDiskImageSynchronizationMode) throws](./init%28url,readonly,cachingmode,synchronizationmode%29-36gc5.md)
  Initialize the attachment from a local file URL.
- [init(url: URL, readOnly: Bool, cachingMode: VZDiskImageCachingMode, synchronizationMode: VZDiskImageSynchronizationMode) throws](./init%28url,readonly,cachingmode,synchronizationmode%29-36gc5.md)
  Initialize the attachment from a local file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(url:readonly:)-9qeco)*