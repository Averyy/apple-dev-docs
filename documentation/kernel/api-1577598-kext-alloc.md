# kext_alloc

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 15.0+

## Declaration

```swift
kern_return_t kext_alloc(vm_offset_t *addr, vm_size_t size, boolean_t fixed);
```

## See Also

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
- [OSKextRequestResource](1508294-oskextrequestresource.md)
  Requests data from a nonlocalized resource file in a kext bundle on disk.
- [OSKextResetPgoCounters](1646298-oskextresetpgocounters.md)
- [OSKextResetPgoCountersLock](1646299-oskextresetpgocounterslock.md)
- [OSKextResetPgoCountersUnlock](1646297-oskextresetpgocountersunlock.md)
- [OSKextRetainKextWithLoadTag](1508272-oskextretainkextwithloadtag.md)
  Retain a loaded kext based on its load tag, and enable autounload for that kext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1577598-kext_alloc)*