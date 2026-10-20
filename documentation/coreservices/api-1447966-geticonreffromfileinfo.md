# GetIconRefFromFileInfo(_:_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.1+ - Deprecated in 10.13

## Declaration

```swift
func GetIconRefFromFileInfo(_ inRef: UnsafePointer<FSRef>!, _ inFileNameLength: Int, _ inFileName: UnsafePointer<UniChar>!, _ inWhichInfo: FSCatalogInfoBitmap, _ inCatalogInfo: UnsafePointer<FSCatalogInfo>!, _ inUsageFlags: IconServicesUsageFlags, _ outIconRef: UnsafeMutablePointer<IconRef?>!, _ outLabel: UnsafeMutablePointer<Int16>!) -> OSStatus
```

```c
OSStatus GetIconRefFromFileInfo(const FSRef *inRef, UniCharCount inFileNameLength, const UniChar *inFileName, FSCatalogInfoBitmap inWhichInfo, const FSCatalogInfo *inCatalogInfo, IconServicesUsageFlags inUsageFlags, IconRef *outIconRef, SInt16 *outLabel);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447966-geticonreffromfileinfo)*