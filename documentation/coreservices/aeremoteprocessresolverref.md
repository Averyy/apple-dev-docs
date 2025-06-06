# AERemoteProcessResolverRef

**Framework**: Core Services  
**Kind**: tdef

An opaque reference to an object that encapsulates the mechanism for obtaining a list of processes running on a remote machine.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```swift
typealias AERemoteProcessResolverRef = OpaquePointer
```

#### Discussion

You create an instance of `AERemoteProcessResolverRef` by calling [`AECreateRemoteProcessResolver(_:_:)`](1445692-aecreateremoteprocessresolver.md), and you must disposed of it by calling [`AEDisposeRemoteProcessResolver(_:)`](1442572-aedisposeremoteprocessresolver.md). An instance of this type is not a `CFType` (the base type used by all Core Foundation derived opaque types). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/aeremoteprocessresolverref)*