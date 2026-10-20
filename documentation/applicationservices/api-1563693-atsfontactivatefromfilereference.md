# ATSFontActivateFromFileReference(_:_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontActivateFromFileReference(_ iFile: UnsafePointer<FSRef>!, _ iContext: ATSFontContext, _ iFormat: ATSFontFormat, _ iRefCon: UnsafeMutableRawPointer!, _ iOptions: ATSOptionFlags, _ oContainer: UnsafeMutablePointer<ATSFontContainerRef>!) -> OSStatus
```

```c
OSStatus ATSFontActivateFromFileReference(const FSRef *iFile, ATSFontContext iContext, ATSFontFormat iFormat, void *iRefCon, ATSOptionFlags iOptions, ATSFontContainerRef *oContainer);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563693-atsfontactivatefromfilereference)*