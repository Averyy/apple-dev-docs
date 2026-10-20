# IOCFUnserializeWithSize(_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.10+
- visionOS 2.4+

## Declaration

```swift
func IOCFUnserializeWithSize(_ buffer: UnsafePointer<CChar>!, _ bufferSize: Int, _ allocator: CFAllocator!, _ options: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> CFTypeRef!
```

```c
CFTypeRef IOCFUnserializeWithSize(const char *buffer, size_t bufferSize, CFAllocatorRef allocator, CFOptionFlags options, CFStringRef *errorString);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514745-iocfunserializewithsize)*