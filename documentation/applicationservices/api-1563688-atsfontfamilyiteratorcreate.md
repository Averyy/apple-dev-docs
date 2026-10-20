# ATSFontFamilyIteratorCreate(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontFamilyIteratorCreate(_ iContext: ATSFontContext, _ iFilter: UnsafePointer<ATSFontFilter>!, _ iRefCon: UnsafeMutableRawPointer!, _ iOptions: ATSOptionFlags, _ ioIterator: UnsafeMutablePointer<ATSFontFamilyIterator?>!) -> OSStatus
```

```c
OSStatus ATSFontFamilyIteratorCreate(ATSFontContext iContext, const ATSFontFilter *iFilter, void *iRefCon, ATSOptionFlags iOptions, ATSFontFamilyIterator *ioIterator);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563688-atsfontfamilyiteratorcreate)*