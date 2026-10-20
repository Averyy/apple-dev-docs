# AEDeterminePermissionToAutomateTarget(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.14+

## Declaration

```swift
func AEDeterminePermissionToAutomateTarget(_ target: UnsafePointer<AEAddressDesc>!, _ theAEEventClass: AEEventClass, _ theAEEventID: AEEventID, _ askUserIfNeeded: Bool) -> OSStatus
```

```c
OSStatus AEDeterminePermissionToAutomateTarget(const AEAddressDesc *target, AEEventClass theAEEventClass, AEEventID theAEEventID, Boolean askUserIfNeeded);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/3025784-aedeterminepermissiontoautomatet)*