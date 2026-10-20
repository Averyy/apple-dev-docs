# ATSFontGetContainer(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontGetContainer(_ iFont: ATSFontRef, _ iOptions: ATSOptionFlags, _ oContainer: UnsafeMutablePointer<ATSFontContainerRef>!) -> OSStatus
```

```c
OSStatus ATSFontGetContainer(ATSFontRef iFont, ATSOptionFlags iOptions, ATSFontContainerRef *oContainer);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563651-atsfontgetcontainer)*