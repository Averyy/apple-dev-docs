# AECreateRemoteProcessResolver(_:_:)

**Framework**: Core Services  
**Kind**: func

Creates an object for resolving a list of remote processes.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func AECreateRemoteProcessResolver(_ allocator: CFAllocator!, _ url: CFURL!) -> AERemoteProcessResolverRef!
```

#### Return_value

An [`AERemoteProcessResolverRef`](aeremoteprocessresolverref.md), which must be disposed of with [`AEDisposeRemoteProcessResolver(_:)`](1442572-aedisposeremoteprocessresolver.md). A resolver can only be used one time; once it has obtained a list of remote processes from a server, or gotten an error, it can no longer be scheduled. To retrieve a new list of processes, create a new instance of this object.

#### Discussion

You supply this function with the URL for a remote host and port; it returns a reference to a resolver object. To obtain a list of remote processes from the resolver, you can query it synchronously with [`AERemoteProcessResolverGetProcesses(_:_:)`](1444456-aeremoteprocessresolvergetproces.md), which blocks until the request completes (either successfully or with an error).

If asynchronous behavior is desired, you can optionally use [`AERemoteProcessResolverScheduleWithRunLoop(_:_:_:_:_:)`](1447259-aeremoteprocessresolverschedulew.md) to schedule the resolver asynchronously on a run loop. If so, you supply a callback routine (see [`AERemoteProcessResolverCallback`](aeremoteprocessresolvercallback.md)) that is executed when the resolver completes. To obtain information about the remote processes, you will again have to call [`AERemoteProcessResolverGetProcesses(_:_:)`](1444456-aeremoteprocessresolvergetproces.md). 

A resolver can only be used once; once it has fetched the data or gotten an error it can no longer be scheduled. The data obtained by the resolver is a `CFArrayRef` of `CFDictionaryRef` objects. For information on the format of the returned remote process information, see the description of the function result for the function [`AERemoteProcessResolverGetProcesses(_:_:)`](1444456-aeremoteprocessresolvergetproces.md), and also [`Remote Process Dictionary Keys`](https://developer.apple.com/documentation/applicationservices/apple_event_manager/remote_process_dictionary_keys).

##### 1770201

Thread safe starting in OS X v10.3.

## Parameters

- `allocator`: An object that is used to allocates and deallocate any Core Foundation types created or returned by this API. You can pass   to get the default allocation behavior. The allocator is based on  , an opaque data type described in the Core Foundation Reference Documentation.
- `url`: A   reference identifying the remote host and port on which to look for processes. See the Core Foundation Reference Documentation for a description of the   data type.

## See Also

- [func AEDisposeRemoteProcessResolver(AERemoteProcessResolverRef!)](1442572-aedisposeremoteprocessresolver.md)
  Disposes of an `AERemoteProcessResolverRef`.
- [func AERemoteProcessResolverGetProcesses(AERemoteProcessResolverRef!, UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!](1444456-aeremoteprocessresolvergetproces.md)
  Returns an array of objects containing information about processes running on a remote machine.
- [func AERemoteProcessResolverScheduleWithRunLoop(AERemoteProcessResolverRef!, CFRunLoop!, CFString!, AERemoteProcessResolverCallback!, UnsafePointer<AERemoteProcessResolverContext>!)](1447259-aeremoteprocessresolverschedulew.md)
  Schedules a resolver for execution on a given run loop in a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1445692-aecreateremoteprocessresolver)*