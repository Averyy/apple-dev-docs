# ATSFontQueryCallback

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
typealias ATSFontQueryCallback = (ATSFontQueryMessageID, CFPropertyList?, UnsafeMutableRawPointer?) -> Unmanaged<CFPropertyList>?
```

```c
typedef CFPropertyListRef (*ATSFontQueryCallback)(ATSFontQueryMessageID msgid, CFPropertyListRef data, void *refCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/atsfontquerycallback)*