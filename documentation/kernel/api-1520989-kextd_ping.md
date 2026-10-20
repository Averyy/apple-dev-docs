# kextd_ping

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.6+

## Declaration

```c
kern_return_t kextd_ping(mach_port_t server);
```

## See Also

### kext
- [kext_alloc](./api-1577598-kext_alloc.md)
- [kext_alloc_init](./api-1577599-kext_alloc_init.md)
- [kext_free](./api-1577600-kext_free.md)
- [kext_request](./api-1588829-kext_request.md)
- [OSKextCancelRequest](./api-1508350-oskextcancelrequest.md)
  Cancels a pending user-space kext request without invoking the callback.
- [OSKextGetCurrentIdentifier](./api-1508305-oskextgetcurrentidentifier.md)
  Returns the CFBundleIdentifier for the calling kext as a C string.
- [OSKextGetCurrentLoadTag](./api-1508336-oskextgetcurrentloadtag.md)
  Returns the run-time load tag for the calling kext as an `OSKextLoadTag`.
- [OSKextGetCurrentVersionString](./api-1508326-oskextgetcurrentversionstring.md)
  Returns the CFBundleVersion for the calling kext as a C string.
- [OSKextGrabPgoData](./api-1508333-oskextgrabpgodata.md)
- [OSKextLoadKextWithIdentifier](./api-1508323-oskextloadkextwithidentifier.md)
  Request that a kext be loaded.
- [OSKextReleaseKextWithLoadTag](./api-1508339-oskextreleasekextwithloadtag.md)
  Release a loaded kext based on its load tag.
- [OSKextRequestResource](./api-1508294-oskextrequestresource.md)
  Requests data from a nonlocalized resource file in a kext bundle on disk.
- [OSKextResetPgoCounters](./api-1646298-oskextresetpgocounters.md)
- [OSKextResetPgoCountersLock](./api-1646299-oskextresetpgocounterslock.md)
- [OSKextResetPgoCountersUnlock](./api-1646297-oskextresetpgocountersunlock.md)
- [OSKextRetainKextWithLoadTag](./api-1508272-oskextretainkextwithloadtag.md)
  Retain a loaded kext based on its load tag, and enable autounload for that kext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1520989-kextd_ping)*