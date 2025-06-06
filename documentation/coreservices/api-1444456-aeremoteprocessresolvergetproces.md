# AERemoteProcessResolverGetProcesses(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns an array of objects containing information about processes running on a remote machine.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func AERemoteProcessResolverGetProcesses(_ ref: AERemoteProcessResolverRef!, _ outError: UnsafeMutablePointer<CFStreamError>!) -> Unmanaged<CFArray>!
```

#### Return_value

In the case of an error, returns `NULL`, in which case the `outError` parameter provides error information. If successful, returns a `CFArrayRef` of `CFDictionaryRef` objects containing information about the discovered remote processes. Each dictionary contains the URL of a remote application and its human readable name; it may also contain a `CFNumberRef` specifying a user ID for the application, if it has one; and it may also contain a `CFNumberRef` specifying the process ID for the process. The array is owned by the resolver, so you must retain it before disposing of the resolver object itself. For information on the keys for getting information from the dictionary, see [`Remote Process Dictionary Keys`](https://developer.apple.com/documentation/applicationservices/apple_event_manager/remote_process_dictionary_keys).

#### Discussion

You first call [`AECreateRemoteProcessResolver(_:_:)`](1445692-aecreateremoteprocessresolver.md) to obtain a reference to a resolver object you can use to obtain a list of processes running on a specified remote machine. See the description for that function for additional information. You then pass that reference to `AERemoteProcessResolverGetProcesses` to get an array of objects containing information about the discovered remote processes.

If the resolver was not previously scheduled for execution (by a call to the [`AERemoteProcessResolverScheduleWithRunLoop(_:_:_:_:_:)`](1447259-aeremoteprocessresolverschedulew.md) function), `AERemoteProcessResolverGetProcesses` will block until the resulting array is available or an error occurs. If the resolver was previously scheduled but had not yet completed fetching the array, this call will block until the resolver does complete.

##### 1770203

Thread safe starting in OS X v10.3.

## Parameters

- `ref`: The   to query. Acquired from a previous call to  .
- `outError`: If the function result is  ,   contains information about the failure. See the Core Foundation Reference Documentation for a description of the   data type.

## See Also

- [func AECreateRemoteProcessResolver(CFAllocator!, CFURL!) -> AERemoteProcessResolverRef!](1445692-aecreateremoteprocessresolver.md)
  Creates an object for resolving a list of remote processes.
- [func AEDisposeRemoteProcessResolver(AERemoteProcessResolverRef!)](1442572-aedisposeremoteprocessresolver.md)
  Disposes of an `AERemoteProcessResolverRef`.
- [func AERemoteProcessResolverScheduleWithRunLoop(AERemoteProcessResolverRef!, CFRunLoop!, CFString!, AERemoteProcessResolverCallback!, UnsafePointer<AERemoteProcessResolverContext>!)](1447259-aeremoteprocessresolverschedulew.md)
  Schedules a resolver for execution on a given run loop in a given mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1444456-aeremoteprocessresolvergetproces)*