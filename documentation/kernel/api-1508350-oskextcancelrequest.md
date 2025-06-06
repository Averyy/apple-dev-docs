# OSKextCancelRequest

**Framework**: Kernel  
**Kind**: func

Cancels a pending user-space kext request without invoking the callback.

**Availability**:
- macOS 10.6+

## Declaration

```swift
OSReturn OSKextCancelRequest(OSKextRequestTag requestTag, void **contextOut);
```

#### Return_value

`kOSReturnSuccess` if the request is successfully canceled. `kOSKextReturnNotFound` if `requestTag` does not identify any pending request. Other `OSKextReturn...` errors are possible.

#### Discussion

This function cancels a pending request if it exists, so that its callback will not be invoked. It returns in `contextOut` the context pointer used to create the request so that any resources allocated for the request can be cleaned up.

Kexts do not need to cancel outstanding requests in their module stop functions; when a kext is unloaded, all pending request callbacks are invoked with a result of `kOSKextReturnTimeout` before the stop function is called.

## Parameters

- `requestTag`: A tag identifying a pending request.
- `contextOut`: If non- , filled with the context pointer originally passed with the request.

## See Also

- [kext_alloc](1577598-kext_alloc.md)
- [kext_alloc_init](1577599-kext_alloc_init.md)
- [kext_free](1577600-kext_free.md)
- [kext_request](1588829-kext_request.md)
- [kextd_ping](1520989-kextd_ping.md)
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
- [OSKextRequestResource](1508294-oskextrequestresource.md)
  Requests data from a nonlocalized resource file in a kext bundle on disk.
- [OSKextResetPgoCounters](1646298-oskextresetpgocounters.md)
- [OSKextResetPgoCountersLock](1646299-oskextresetpgocounterslock.md)
- [OSKextResetPgoCountersUnlock](1646297-oskextresetpgocountersunlock.md)
- [OSKextRetainKextWithLoadTag](1508272-oskextretainkextwithloadtag.md)
  Retain a loaded kext based on its load tag, and enable autounload for that kext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1508350-oskextcancelrequest)*