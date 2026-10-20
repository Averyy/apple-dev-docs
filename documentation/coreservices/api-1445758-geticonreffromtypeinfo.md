# GetIconRefFromTypeInfo(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+ - Deprecated in 10.15

## Declaration

```swift
func GetIconRefFromTypeInfo(_ inCreator: OSType, _ inType: OSType, _ inExtension: CFString!, _ inMIMEType: CFString!, _ inUsageFlags: IconServicesUsageFlags, _ outIconRef: UnsafeMutablePointer<IconRef?>!) -> OSErr
```

```c
OSErr GetIconRefFromTypeInfo(OSType inCreator, OSType inType, CFStringRef inExtension, CFStringRef inMIMEType, IconServicesUsageFlags inUsageFlags, IconRef *outIconRef);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445758-geticonreffromtypeinfo)*