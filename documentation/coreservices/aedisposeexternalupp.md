# AEDisposeExternalUPP

**Framework**: Core Services  
**Kind**: tdef

Defines a universal procedure pointer to a function the Apple Event Manager calls to dispose of a descriptor created by the `AECreateDescFromExternalPtr` function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
typealias AEDisposeExternalUPP = AEDisposeExternalProcPtr
```

#### Discussion

See the [`AEDisposeExternalProcPtr`](aedisposeexternalprocptr.md) callback function. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aedisposeexternalupp)*