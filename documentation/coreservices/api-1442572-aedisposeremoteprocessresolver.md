# AEDisposeRemoteProcessResolver(_:)

**Framework**: Core Services  
**Kind**: func

Disposes of an `AERemoteProcessResolverRef`.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func AEDisposeRemoteProcessResolver(_ ref: AERemoteProcessResolverRef!)
```

#### Discussion

If this resolver is currently scheduled on a run loop, it is unscheduled, and the asynchronous callback is not executed.

##### 1770202

Thread safe starting in OS X v10.3.

## Parameters

- `ref`: The   to dispose of. Acquired from a previous call to  .

## See Also

- [func AECreateRemoteProcessResolver(CFAllocator!, CFURL!) -> AERemoteProcessResolverRef!](1445692-aecreateremoteprocessresolver.md)
  Creates an object for resolving a list of remote processes.
- [func AERemoteProcessResolverGetProcesses(AERemoteProcessResolverRef!, UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](1444456-aeremoteprocessresolvergetproces.md)
  Returns an array of objects containing information about processes running on a remote machine.
- [func AERemoteProcessResolverScheduleWithRunLoop(AERemoteProcessResolverRef!, CFRunLoop!, CFString!, AERemoteProcessResolverCallback!, UnsafePointer<AERemoteProcessResolverContext>!)](1447259-aeremoteprocessresolverschedulew.md)
  Schedules a resolver for execution on a given run loop in a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1442572-aedisposeremoteprocessresolver)*