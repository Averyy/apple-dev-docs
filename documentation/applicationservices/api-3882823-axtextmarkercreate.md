# AXTextMarkerCreate(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 12.0+

## Declaration

```swift
func AXTextMarkerCreate(_ allocator: CFAllocator?, _ bytes: UnsafePointer<UInt8>, _ length: CFIndex) -> AXTextMarker
```

```c
AXTextMarkerRef AXTextMarkerCreate(CFAllocatorRef allocator, const UInt8 *bytes, CFIndex length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/3882823-axtextmarkercreate)*