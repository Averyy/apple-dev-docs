# AERemoteProcessResolverScheduleWithRunLoop(_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Schedules a resolver for execution on a given run loop in a given mode.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func AERemoteProcessResolverScheduleWithRunLoop(_ ref: AERemoteProcessResolverRef!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!, _ callback: AERemoteProcessResolverCallback!, _ ctx: UnsafePointer<AERemoteProcessResolverContext>!)
```

#### Discussion

Schedules a resolver for execution on a given run loop in a given mode. The resolver will move through various internal states as long as the specified run loop is run. When the resolver completes, either with success or with an error condition, the callback is executed. There is no explicit unschedule of the resolver; you must dispose of it to remove it from the run loop.

##### 1770204

Thread safe starting in OS X v10.3.

## Parameters

- `ref`: The   to query. Acquired from a previous call to  .
- `runLoop`: The run loop on which to schedule resolution of remote processes. For information on run loops, see Introduction to Run Loops. See the Core Foundation Reference Documentation for a description of the   data type.
- `runLoopMode`: Specifies the run loop mode. See Input Modes for information on available modes. See the Core Foundation Reference Documentation for a description of the   data type.
- `callback`: A callback function to be executed when the resolver completes. See   for information on the callback definition.
- `ctx`: Optionally supplies information of use while resolving remote processes. If this parameter is not  , the info field of this structure is passed to the callback function (otherwise, the info parameter to the   function will explicitly be  ). See   for a description of this data type.

## See Also

- [func AECreateRemoteProcessResolver(CFAllocator!, CFURL!) -> AERemoteProcessResolverRef!](1445692-aecreateremoteprocessresolver.md)
  Creates an object for resolving a list of remote processes.
- [func AEDisposeRemoteProcessResolver(AERemoteProcessResolverRef!)](1442572-aedisposeremoteprocessresolver.md)
  Disposes of an `AERemoteProcessResolverRef`.
- [func AERemoteProcessResolverGetProcesses(AERemoteProcessResolverRef!, UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](1444456-aeremoteprocessresolvergetproces.md)
  Returns an array of objects containing information about processes running on a remote machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1447259-aeremoteprocessresolverschedulew)*