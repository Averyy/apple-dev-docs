# KextManagerLoadKextWithIdentifier

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Request the kext loading system to load a kext with a given bundle identifier.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.6+

## Declaration

```c
OSReturn KextManagerLoadKextWithIdentifier(CFStringRef kextIdentifier, CFArrayRef dependencyKextAndFolderURLs);
```

## Return Value

`kOSReturnSuccess` if the kext is successfully loaded (or is already loaded), otherwise returns on error.

## Discussion

`kextIdentifier` is looked up in the system extensions folder and among any kexts from `dependencyKextAndFolderURLs`. Any non-kext URLs in `dependencyKextAndFolderURLs` are scanned at the top level for kexts and plugins of kexts.

Either the calling process must have an effective user id of 0 (superuser), or the kext being loaded and all its dependencies must reside in /System and have an OSBundleAllowUserLoad property of `true`.

## Parameters

- `kextIdentifier`: The bundle identifier of the kext to look up and load.
- `dependencyKextAndFolderURLs`: An array of additional URLs, of individual kexts and of folders that may contain kexts.

## See Also

### Miscellaneous
- [KextManagerCopyLoadedKextInfo](./api-1562908-kextmanagercopyloadedkextinfo.md)
  Returns information about loaded kexts in a dictionary.
- [KextManagerCreateURLForBundleIdentifier](./api-1562905-kextmanagercreateurlforbundleide.md)
  Create a URL locating a kext with a given bundle identifier.
- [KextManagerLoadKextWithURL](./api-1562906-kextmanagerloadkextwithurl.md)
  Request the kext loading system to load a kext with a given URL.
- [KextManagerUnloadKextWithIdentifier](./api-1562904-kextmanagerunloadkextwithidentif.md)
  Request the kernel to unload a kext with a given bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1562907-kextmanagerloadkextwithidentifie)*