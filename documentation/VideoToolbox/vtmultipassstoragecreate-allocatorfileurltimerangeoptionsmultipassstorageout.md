# VTMultiPassStorageCreate(allocator:fileURL:timeRange:options:multiPassStorageOut:)

**Framework**: Video Toolbox  
**Kind**: func

Creates a multipass storage object using a temporary file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTMultiPassStorageCreate(allocator: CFAllocator?, fileURL: CFURL?, timeRange: CMTimeRange, options: CFDictionary?, multiPassStorageOut: UnsafeMutablePointer<VTMultiPassStorage?>) -> OSStatus
```

#### Discussion

You can use the multipass storage object to perform multipass encoding; see [`kVTCompressionPropertyKey_MultiPassStorage`](kvtcompressionpropertykey_multipassstorage.md).

Call [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to release the multipass storage object when you are done with it.

## Parameters

- `allocator`: An allocator for the session.  Pass   to use the default allocator.
- `fileURL`: Specifies where to put the backing file for the multipass storage object. If you pass   for  , the video toolbox will pick a unique temporary file name.
- `timeRange`: Gives a hint to the multipass storage about valid time stamps for data. You can pass   if you do not want to provide a time range hint.
- `options`: If the file did not exist when the storage was created, the file will be deleted when the multipass storage object is finalized, unless you set the   option to   in the   dictionary.
- `multiPassStorageOut`: A pointer to the newly created multipass storage object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmultipassstoragecreate(allocator:fileurl:timerange:options:multipassstorageout:))*