# ATSFontGetTableDirectory(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontGetTableDirectory(_ iFont: ATSFontRef, _ iBufferSize: Int, _ ioBuffer: UnsafeMutableRawPointer!, _ oSize: UnsafeMutablePointer<Int>!) -> OSStatus
```

```c
OSStatus ATSFontGetTableDirectory(ATSFontRef iFont, ByteCount iBufferSize, void *ioBuffer, ByteCount *oSize);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563677-atsfontgettabledirectory)*