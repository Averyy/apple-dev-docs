# VTMultiPassStorage

**Framework**: Video Toolbox

An object that stores video encoding metadata from a multipass encoding session.

## Topics

### Creating Storage Objects
- [func VTMultiPassStorageCreate(allocator: CFAllocator?, fileURL: CFURL?, timeRange: CMTimeRange, options: CFDictionary?, multiPassStorageOut: UnsafeMutablePointer<VTMultiPassStorage?>) -> OSStatus](vtmultipassstoragecreate(allocator:fileurl:timerange:options:multipassstorageout:).md)
  Creates a multipass storage object using a temporary file.
### Closing Storage Objects
- [func VTMultiPassStorageClose(VTMultiPassStorage) -> OSStatus](vtmultipassstorageclose(_:).md)
  Ensures that any pending data is written to the multipass storage file and closes the file.
### Inspecting Storage Objects
- [func VTMultiPassStorageGetTypeID() -> CFTypeID](vtmultipassstoragegettypeid().md)
  Retrieves the Core Foundation type identifier for the multipass storage object.
### Data Types
- [class VTMultiPassStorage](vtmultipassstorage.md)
  An object for storing information for each frame of a multipass compression session.
### Constants
- [let kVTMultiPassStorageCreationOption_DoNotDelete: CFString](kvtmultipassstoragecreationoption_donotdelete.md)
  Indicates that the multipass storage object’s backing store should not be deleted when finalized.

## See Also

- [Encoding video for low-latency conferencing](encoding-video-for-low-latency-conferencing.md)
  Configure a compression session to optimize encoding for video-conferencing apps.
- [Encoding video for live streaming](encoding-video-for-live-streaming.md)
  Configure a compression session to encode video for live streaming.
- [Encoding video for offline transcoding](encoding-video-for-offline-transcoding.md)
  Configure a compression session to transcode video in offline workflows.
- [VTCompressionSession](vtcompressionsession-api-collection.md)
  An object that compresses video data.
- [VTDecompressionSession](vtdecompressionsession-api-collection.md)
  An object that decompresses video data.
- [VTFrameSilo](vtframesilo-api-collection.md)
  An object that stores sample buffers from a multipass encoding session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtmultipassstorage-api-collection)*