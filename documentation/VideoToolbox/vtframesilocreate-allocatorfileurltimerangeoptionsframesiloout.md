# VTFrameSiloCreate(allocator:fileURL:timeRange:options:frameSiloOut:)

**Framework**: Videotoolbox  
**Kind**: func

Creates a frame silo object using a temporary file.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTFrameSiloCreate(allocator: CFAllocator?, fileURL: CFURL?, timeRange: CMTimeRange, options: CFDictionary?, frameSiloOut: UnsafeMutablePointer<VTFrameSilo?>) -> OSStatus
```

#### Discussion

You can use the returned frame silo object to gather frames produced by multipass encoding.

Call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release the frame silo object when you are done with it.

## Parameters

- `allocator`: An allocator for the frame silo.  Pass   to use the default allocator.
- `fileURL`: The URL of the backing file for the   object. If you pass   for  , VideoToolbox will pick a unique temporary file name.
- `timeRange`: The valid time range for the frame silo. Must be valid for progress reporting.
- `options`: Reserved, pass  .
- `frameSiloOut`: Points to a   to receive the newly created object. Call   to release your retain on the created VTFrameSilo object when you are done with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframesilocreate(allocator:fileurl:timerange:options:framesiloout:))*