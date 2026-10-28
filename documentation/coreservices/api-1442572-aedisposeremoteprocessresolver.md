# AEDisposeRemoteProcessResolver(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes of an `AERemoteProcessResolverRef`.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func AEDisposeRemoteProcessResolver(_ ref: AERemoteProcessResolverRef!)
```

```c
void AEDisposeRemoteProcessResolver(AERemoteProcessResolverRef ref);
```

## Discussion

If this resolver is currently scheduled on a run loop, it is unscheduled, and the asynchronous callback is not executed.

### Version-Notes

Thread safe starting in OS X v10.3.

## Parameters

- `ref`: The [`AERemoteProcessResolverRef`](./aeremoteprocessresolverref.md) to dispose of. Acquired from a previous call to [`AECreateRemoteProcessResolver(_:_:)`](./api-1445692-aecreateremoteprocessresolver.md).

## See Also

### Locating Processes on Remote Computers
- [func AECreateRemoteProcessResolver(CFAllocator!, CFURL!) -> AERemoteProcessResolverRef!](./api-1445692-aecreateremoteprocessresolver.md)
  Creates an object for resolving a list of remote processes.
- [func AERemoteProcessResolverGetProcesses(AERemoteProcessResolverRef!, UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](./api-1444456-aeremoteprocessresolvergetproces.md)
  Returns an array of objects containing information about processes running on a remote machine.
- [func AERemoteProcessResolverScheduleWithRunLoop(AERemoteProcessResolverRef!, CFRunLoop!, CFString!, AERemoteProcessResolverCallback!, UnsafePointer<AERemoteProcessResolverContext>!)](./api-1447259-aeremoteprocessresolverschedulew.md)
  Schedules a resolver for execution on a given run loop in a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442572-aedisposeremoteprocessresolver)*