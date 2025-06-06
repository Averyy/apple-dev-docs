# OSKextRequestResource

**Framework**: Kernel  
**Kind**: func

Requests data from a nonlocalized resource file in a kext bundle on disk.

**Availability**:
- macOS 10.6+

## Declaration

```swift
OSReturn OSKextRequestResource(const char *kextIdentifier, const char *resourceName, OSKextRequestResourceCallback callback, void *context, OSKextRequestTag *requestTagOut);
```

#### Return_value

`kOSReturnSuccess` if the request is successfully queued. `kOSKextReturnInvalidArgument` if `kextIdentifier` or `resourceName` or if `callback` is not an address within a loaded kext executable. `kOSKextReturnStopping` if an unload attempt is being made on the kext containing `callback`. Other `OSKextReturn...` errors are possible.

#### Discussion

This function queues an asynchronous request to the user-space kext daemon kextd(8); requests for resources early in system startup will not be fulfilled until that daemon starts. Requests made by a kext while that kext is loading (specifically in the kext's module start routine) will not be fulfilled until after the start routine returns and the kext is completely loaded. Kexts requesting resources should be sure to perform appropriate locking in the callback function.

Kext resources are stored in the kext's on-disk bundle under the Resources subdirectory. See [`Bundle Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFBundles/Introduction/Introduction.html#//apple_ref/doc/uid/10000123i) for an overview of bundle structure. The localization context of the kext daemon (namely that of the superuser) will be used in retrieving resources; kext resources intended for use in the kernel should generally not be localized.

`callback` is guaranteed to be invoked except when:

- [`OSKextCancelRequest`](1508350-oskextcancelrequest.md) is used to cancel the request. In this case the kext gets the `context` pointer and can clean it up.
- The request is made during a kext's module start routine and the start routine returns an error. In this case, callbacks cannot be safely invoked, so the kext should clean up all request contexts when returning the error from the start routine.

Kexts with pending requests are not subject to autounload, but requests are subject to timeout after a few minutes. If that amount of time passes with no response from user space, `callback` is invoked with a result of. `kOSKextReturnTimeout`.

Kexts that are explicitly unloaded have all pending request callbacks invoked with a result of `kOSKextReturnStopping`. The kext must handle these callbacks, even if its stop routine will prevent unloading. If the kext does prevent unloading, it can reissue resource requests outside of the stop function.

## Parameters

- `kextIdentifier`: The CFBundleIdentifier of the kext from which to read the file.
- `resourceName`: The name of the resource file to read.
- `callback`: A pointer to a callback function; the address must be within a currently-loaded kext.
- `context`: A pointer to arbitrary run-time data that will be passed to the callback when it is invoked. May be  .
- `requestTagOut`: If non- , filled on success with a tag identifying the pending request (or on failure with  ; can be used with  .

## See Also

- [kext_alloc](1577598-kext_alloc.md)
- [kext_alloc_init](1577599-kext_alloc_init.md)
- [kext_free](1577600-kext_free.md)
- [kext_request](1588829-kext_request.md)
- [kextd_ping](1520989-kextd_ping.md)
- [OSKextCancelRequest](1508350-oskextcancelrequest.md)
  Cancels a pending user-space kext request without invoking the callback.
- [OSKextGetCurrentIdentifier](1508305-oskextgetcurrentidentifier.md)
  Returns the CFBundleIdentifier for the calling kext as a C string.
- [OSKextGetCurrentLoadTag](1508336-oskextgetcurrentloadtag.md)
  Returns the run-time load tag for the calling kext as an `OSKextLoadTag`.
- [OSKextGetCurrentVersionString](1508326-oskextgetcurrentversionstring.md)
  Returns the CFBundleVersion for the calling kext as a C string.
- [OSKextGrabPgoData](1508333-oskextgrabpgodata.md)
- [OSKextLoadKextWithIdentifier](1508323-oskextloadkextwithidentifier.md)
  Request that a kext be loaded.
- [OSKextReleaseKextWithLoadTag](1508339-oskextreleasekextwithloadtag.md)
  Release a loaded kext based on its load tag.
- [OSKextResetPgoCounters](1646298-oskextresetpgocounters.md)
- [OSKextResetPgoCountersLock](1646299-oskextresetpgocounterslock.md)
- [OSKextResetPgoCountersUnlock](1646297-oskextresetpgocountersunlock.md)
- [OSKextRetainKextWithLoadTag](1508272-oskextretainkextwithloadtag.md)
  Retain a loaded kext based on its load tag, and enable autounload for that kext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1508294-oskextrequestresource)*