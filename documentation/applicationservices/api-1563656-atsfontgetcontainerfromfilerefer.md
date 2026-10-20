# ATSFontGetContainerFromFileReference(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontGetContainerFromFileReference(_ iFile: UnsafePointer<FSRef>!, _ iContext: ATSFontContext, _ iOptions: ATSOptionFlags, _ oContainer: UnsafeMutablePointer<ATSFontContainerRef>!) -> OSStatus
```

```c
OSStatus ATSFontGetContainerFromFileReference(const FSRef *iFile, ATSFontContext iContext, ATSOptionFlags iOptions, ATSFontContainerRef *oContainer);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563656-atsfontgetcontainerfromfilerefer)*