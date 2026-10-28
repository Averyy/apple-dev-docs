# KextManagerUnloadKextWithIdentifier

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Request the kernel to unload a kext with a given bundle identifier.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```c
OSReturn KextManagerUnloadKextWithIdentifier(CFStringRef kextIdentifier);
```

## Return Value

`kOSReturnSuccess` if the kext is found and successfully unloaded, otherwise returns on error. See `/usr/include/libkern/OSKextLib.h` for error codes.

## Discussion

The calling process must have an effective user id of 0 (superuser).

## Parameters

- `kextIdentifier`: The bundle identifier of the kext to unload.

## See Also

### Miscellaneous
- [KextManagerCopyLoadedKextInfo](./api-1562908-kextmanagercopyloadedkextinfo.md)
  Returns information about loaded kexts in a dictionary.
- [KextManagerCreateURLForBundleIdentifier](./api-1562905-kextmanagercreateurlforbundleide.md)
  Create a URL locating a kext with a given bundle identifier.
- [KextManagerLoadKextWithIdentifier](./api-1562907-kextmanagerloadkextwithidentifie.md)
  Request the kext loading system to load a kext with a given bundle identifier.
- [KextManagerLoadKextWithURL](./api-1562906-kextmanagerloadkextwithurl.md)
  Request the kext loading system to load a kext with a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1562904-kextmanagerunloadkextwithidentif)*