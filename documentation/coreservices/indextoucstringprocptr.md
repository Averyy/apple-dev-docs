# IndexToUCStringProcPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```swift
typealias IndexToUCStringProcPtr = (UInt32, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFString>?>?, UnsafeMutablePointer<UCTypeSelectOptions>?) -> DarwinBoolean
```

```c
typedef Boolean (*IndexToUCStringProcPtr)(UInt32 index, void *listDataPtr, void *refcon, CFStringRef *outString, UCTypeSelectOptions *tsOptions);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/indextoucstringprocptr)*