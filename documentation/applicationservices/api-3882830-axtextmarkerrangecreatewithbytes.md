# AXTextMarkerRangeCreateWithBytes(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 12.0+

## Declaration

```swift
func AXTextMarkerRangeCreateWithBytes(_ allocator: CFAllocator?, _ startMarkerBytes: UnsafePointer<UInt8>, _ startMarkerLength: CFIndex, _ endMarkerBytes: UnsafePointer<UInt8>, _ endMarkerLength: CFIndex) -> AXTextMarkerRange
```

```c
AXTextMarkerRangeRef AXTextMarkerRangeCreateWithBytes(CFAllocatorRef allocator, const UInt8 *startMarkerBytes, CFIndex startMarkerLength, const UInt8 *endMarkerBytes, CFIndex endMarkerLength);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/3882830-axtextmarkerrangecreatewithbytes)*