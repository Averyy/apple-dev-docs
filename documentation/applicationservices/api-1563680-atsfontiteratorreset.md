# ATSFontIteratorReset(_:_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
func ATSFontIteratorReset(_ iContext: ATSFontContext, _ iFilter: UnsafePointer<ATSFontFilter>!, _ iRefCon: UnsafeMutableRawPointer!, _ iOptions: ATSOptionFlags, _ ioIterator: UnsafeMutablePointer<ATSFontIterator?>!) -> OSStatus
```

```c
OSStatus ATSFontIteratorReset(ATSFontContext iContext, const ATSFontFilter *iFilter, void *iRefCon, ATSOptionFlags iOptions, ATSFontIterator *ioIterator);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1563680-atsfontiteratorreset)*