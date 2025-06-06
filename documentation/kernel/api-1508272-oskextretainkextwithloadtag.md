# OSKextRetainKextWithLoadTag

**Framework**: Kernel  
**Kind**: func

Retain a loaded kext based on its load tag, and enable autounload for that kext.

**Availability**:
- macOS 10.6+

## Declaration

```swift
OSReturn OSKextRetainKextWithLoadTag(OSKextLoadTag loadTag);
```

#### Return_value

`kOSReturnSuccess` if the kext was retained. `kOSKextReturnNotFound` if the kext was not found. `kOSKextReturnInvalidArgument` if `loadTag` is `kOSKextInvalidLoadTag`.

#### Discussion

Retaining a kext prevents it from being unloaded, either explicitly or automatically, and enables autounload for the kext. When autounload is enabled, then shortly after the kext's last reference is dropped, it will be unloaded if there are no outstanding references to it and there are no instances of its Libkern C++ subclasses (if any).

Kexts that define subclasses of IOService have autounload enabled automatically. Other kexts can use the reference count to manage automatic unload without having to define and create Libkern C++ objects. For example, a filesystem kext can retain itself whenever a new mount is created, and release itself when a mount is removed. When the last mount is removed, the kext will be unloaded after a brief delay.

A kext can get its own load tag using the [`OSKextGetCurrentLoadTag`](1508336-oskextgetcurrentloadtag.md).

Kexts should not retain and release other kexts; linkage references are accounted for internally.

## Parameters

- `loadTag`: The load tag of the kext to be retained. See  .

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
- [OSKextRequestResource](1508294-oskextrequestresource.md)
  Requests data from a nonlocalized resource file in a kext bundle on disk.
- [OSKextResetPgoCounters](1646298-oskextresetpgocounters.md)
- [OSKextResetPgoCountersLock](1646299-oskextresetpgocounterslock.md)
- [OSKextResetPgoCountersUnlock](1646297-oskextresetpgocountersunlock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1508272-oskextretainkextwithloadtag)*