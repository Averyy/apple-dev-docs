# InvokeIndexToUCStringUPP(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func InvokeIndexToUCStringUPP(_ index: UInt32, _ listDataPtr: UnsafeMutableRawPointer!, _ refcon: UnsafeMutableRawPointer!, _ outString: UnsafeMutablePointer<Unmanaged<CFString>?>!, _ tsOptions: UnsafeMutablePointer<UCTypeSelectOptions>!, _ userUPP: IndexToUCStringUPP!) -> Bool
```

```c
Boolean InvokeIndexToUCStringUPP(UInt32 index, void *listDataPtr, void *refcon, CFStringRef *outString, UCTypeSelectOptions *tsOptions, IndexToUCStringUPP userUPP);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390660-invokeindextoucstringupp)*