# ATSFontGetVerticalMetrics(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontGetVerticalMetrics(_ iFont: ATSFontRef, _ iOptions: ATSOptionFlags, _ oMetrics: UnsafeMutablePointer<ATSFontMetrics>!) -> OSStatus
```

```c
OSStatus ATSFontGetVerticalMetrics(ATSFontRef iFont, ATSOptionFlags iOptions, ATSFontMetrics *oMetrics);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563653-atsfontgetverticalmetrics)*