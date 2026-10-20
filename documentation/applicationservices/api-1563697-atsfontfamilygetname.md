# ATSFontFamilyGetName(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontFamilyGetName(_ iFamily: ATSFontFamilyRef, _ iOptions: ATSOptionFlags, _ oName: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> OSStatus
```

```c
OSStatus ATSFontFamilyGetName(ATSFontFamilyRef iFamily, ATSOptionFlags iOptions, CFStringRef *oName);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563697-atsfontfamilygetname)*