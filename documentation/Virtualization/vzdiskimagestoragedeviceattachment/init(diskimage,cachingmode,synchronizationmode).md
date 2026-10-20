# init(diskImage:cachingMode:synchronizationMode:)

**Framework**: Virtualization  
**Kind**: init  
**Role**: Initializer

Initializes the attachment from a disk image.

**Availability**:
- macOS 27.0+

## Declaration

```swift
convenience init(diskImage: DiskImage, cachingMode: VZDiskImageCachingMode = .automatic, synchronizationMode: VZDiskImageSynchronizationMode = .full) throws
```

#### Discussion

This initializer enables the use of [`DiskImage`](../../DiskImageKit/diskimage.md) objects created with the [DiskImageKit](../../DiskImageKit/DiskImageKit.md) framework, including stacked images with cache and overlay layers.

The following example shows how to initialize a storage attachment object using a disk image.

```swift
    import Virtualization
    
    let imageURL = // A `URL` that references a disk image.
    let diskImage = try DiskImage(opening: .init(url: imageURL))
    let storageAttachment = try VZDiskImageStorageDeviceAttachment(diskImage: diskImage)
    
```

## Parameters

- `diskImage`: A diskImage object created using the [DiskImageKit](../../DiskImageKit/DiskImageKit.md) framework. It supports both single and stacked disk images.
- `cachingMode`: The host-level [`VZDiskImageCachingMode`](../vzdiskimagecachingmode.md) policy for the disk image. This is independent of cache layers in the disk image stack.
- `synchronizationMode`: How the disk image synchronizes with the underlying storage when the guest operating system flushes data, described by one of the available [`VZDiskImageSynchronizationMode`](../vzdiskimagesynchronizationmode.md) modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzdiskimagestoragedeviceattachment/init(diskimage:cachingmode:synchronizationmode:))*