# KextManagerCreateURLForBundleIdentifier

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Create a URL locating a kext with a given bundle identifier.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.2+

## Declaration

```c
CFURLRef KextManagerCreateURLForBundleIdentifier(CFAllocatorRef allocator, CFStringRef kextIdentifier);
```

#### Return Value

A CFURLRef locating a kext with the requested bundle identifier. Returns `NULL` if the kext cannot be found, or on error.

#### Discussion

Kexts are looked up first by whether they are loaded, second by version. Specifically, if `kextIdentifier` identifies a kext that is currently loaded, the returned URL will locate that kext if it's still present on disk. If the requested kext is not loaded, or if its bundle is not at the location it was originally loaded from, the returned URL will locate the latest version of the desired kext, if one can be found within the system extensions folder. If no version of the kext can be found, `NULL` is returned.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or `kCFAllocatorDefault` to use the current default allocator.
- `kextIdentifier`: The bundle identifier to look up.

## See Also

### Miscellaneous
- [KextManagerCopyLoadedKextInfo](./api-1562908-kextmanagercopyloadedkextinfo.md)
  Returns information about loaded kexts in a dictionary.
- [KextManagerLoadKextWithIdentifier](./api-1562907-kextmanagerloadkextwithidentifie.md)
  Request the kext loading system to load a kext with a given bundle identifier.
- [KextManagerLoadKextWithURL](./api-1562906-kextmanagerloadkextwithurl.md)
  Request the kext loading system to load a kext with a given URL.
- [KextManagerUnloadKextWithIdentifier](./api-1562904-kextmanagerunloadkextwithidentif.md)
  Request the kernel to unload a kext with a given bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1562905-kextmanagercreateurlforbundleide)*