# ATSFontGetTable(_:_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontGetTable(_ iFont: ATSFontRef, _ iTag: FourCharCode, _ iOffset: ByteOffset, _ iBufferSize: Int, _ ioBuffer: UnsafeMutableRawPointer!, _ oSize: UnsafeMutablePointer<Int>!) -> OSStatus
```

```c
OSStatus ATSFontGetTable(ATSFontRef iFont, FourCharCode iTag, ByteOffset iOffset, ByteCount iBufferSize, void *ioBuffer, ByteCount *oSize);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563699-atsfontgettable)*