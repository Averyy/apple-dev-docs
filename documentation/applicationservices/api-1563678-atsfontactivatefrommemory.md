# ATSFontActivateFromMemory(_:_:_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontActivateFromMemory(_ iData: LogicalAddress!, _ iLength: Int, _ iContext: ATSFontContext, _ iFormat: ATSFontFormat, _ iReserved: UnsafeMutableRawPointer!, _ iOptions: ATSOptionFlags, _ oContainer: UnsafeMutablePointer<ATSFontContainerRef>!) -> OSStatus
```

```c
OSStatus ATSFontActivateFromMemory(LogicalAddress iData, ByteCount iLength, ATSFontContext iContext, ATSFontFormat iFormat, void *iReserved, ATSOptionFlags iOptions, ATSFontContainerRef *oContainer);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563678-atsfontactivatefrommemory)*