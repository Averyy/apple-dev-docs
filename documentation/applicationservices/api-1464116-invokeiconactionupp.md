# InvokeIconActionUPP(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func InvokeIconActionUPP(_ theType: ResType, _ theIcon: UnsafeMutablePointer<Handle?>!, _ yourDataPtr: UnsafeMutableRawPointer!, _ userUPP: IconActionUPP!) -> OSErr
```

```c
OSErr InvokeIconActionUPP(ResType theType, Handle *theIcon, void *yourDataPtr, IconActionUPP userUPP);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1464116-invokeiconactionupp)*