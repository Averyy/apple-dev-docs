# init(url:readOnly:)

**Framework**: Virtualization  
**Kind**: init

Creates the attachment object from the specified disk image.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(url: URL, readOnly: Bool) throws
```

#### Return Value

In Swift the methods returns an attachment object; in Objective-C the methods returns an attachment object on success, or `nil` if an error occurred

## Parameters

- `url`: A URL that points to a local disk image in RAW format.
- `readOnly`: A Boolean that indicates whether to configure the disk image as read-only. Specify   to prevent the guest operating system from writing to the disk image, and   to allow writing.

## See Also

- [init(url: URL, readOnly: Bool, cachingMode: VZDiskImageCachingMode, synchronizationMode: VZDiskImageSynchronizationMode) throws](vzdiskimagestoragedeviceattachment/init(url:readonly:cachingmode:synchronizationmode:).md)
  Initialize the attachment from a local file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(url:readonly:))*