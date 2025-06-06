# InvokeIndexToUCStringUPP(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func InvokeIndexToUCStringUPP(_ index: UInt32, _ listDataPtr: UnsafeMutableRawPointer!, _ refcon: UnsafeMutableRawPointer!, _ outString: UnsafeMutablePointer<Unmanaged<CFString>?>!, _ tsOptions: UnsafeMutablePointer<UCTypeSelectOptions>!, _ userUPP: IndexToUCStringUPP!) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390660-invokeindextoucstringupp)*