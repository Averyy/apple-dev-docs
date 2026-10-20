# ATSFontGetHorizontalMetrics(_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontGetHorizontalMetrics(_ iFont: ATSFontRef, _ iOptions: ATSOptionFlags, _ oMetrics: UnsafeMutablePointer<ATSFontMetrics>!) -> OSStatus
```

```c
OSStatus ATSFontGetHorizontalMetrics(ATSFontRef iFont, ATSOptionFlags iOptions, ATSFontMetrics *oMetrics);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563665-atsfontgethorizontalmetrics)*