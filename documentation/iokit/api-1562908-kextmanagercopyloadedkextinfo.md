# KextManagerCopyLoadedKextInfo

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns information about loaded kexts in a dictionary.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```c
CFDictionaryRef KextManagerCopyLoadedKextInfo(CFArrayRef kextIdentifiers, CFArrayRef infoKeys);
```

## Return Value

A dictionary, keyed by bundle identifier, of dictionaries containing information about loaded kexts.

## Discussion

The information keys returned by this function are listed below. Some are taken directly from the kext's information property list, and some are generated at run time. Never assume a given key will be present for a kext.

- `CFBundleIdentifier` - CFString
- `CFBundleVersion` - CFString (note: version strings may be canonicalized but their numeric values will be the same; "1.2.0" may become "1.2", for example)
- `OSBundleCompatibleVersion` - CFString
- `OSBundleIsInterface` - CFBoolean
- `OSKernelResource` - CFBoolean
- `OSBundleCPUType` - CFNumber
- `OSBundleCPUSubtype` - CFNumber
- `OSBundlePath` - CFString (this is merely a hint stored in the kernel; the kext is not guaranteed to be at this path)
- `OSBundleExecutablePath` - CFString (the absolute path to the executable within the kext bundle; a hint as above)
- `OSBundleUUID` - CFData (the UUID of the kext executable, if it has one)
- `OSBundleStarted` - CFBoolean (true if the kext is running)
- `OSBundlePrelinked` - CFBoolean (true if the kext is loaded from a prelinked kernel)
- `OSBundleLoadTag` - CFNumber (the "Index" given by kextstat)
- `OSBundleLoadAddress` - CFNumber
- `OSBundleLoadSize` - CFNumber
- `OSBundleWiredSize` - CFNumber
- `OSBundleDependencies` - CFArray of load tags identifying immediate link dependencies
- `OSBundleRetainCount` - CFNumber (the OSObject retain count of the kext itself)
- `OSBundleClasses` - CFArray of CFDictionary containing info on C++ classes defined by the kext:

- `OSMetaClassName` - CFString
- `OSMetaClassSuperclassName` - CFString, absent for root classes
- `OSMetaClassTrackingCount` - CFNumber giving the instance count of the class itself, *plus* 1 for each direct subclass with any instances

## Parameters

- `kextIdentifiers`: An array of kext identifiers to read from the kernel. Pass `NULL` to read info for all loaded kexts.
- `infoKeys`: An array of info keys to read from the kernel. Pass `NULL` to read all information.

## See Also

### Miscellaneous
- [KextManagerCreateURLForBundleIdentifier](./api-1562905-kextmanagercreateurlforbundleide.md)
  Create a URL locating a kext with a given bundle identifier.
- [KextManagerLoadKextWithIdentifier](./api-1562907-kextmanagerloadkextwithidentifie.md)
  Request the kext loading system to load a kext with a given bundle identifier.
- [KextManagerLoadKextWithURL](./api-1562906-kextmanagerloadkextwithurl.md)
  Request the kext loading system to load a kext with a given URL.
- [KextManagerUnloadKextWithIdentifier](./api-1562904-kextmanagerunloadkextwithidentif.md)
  Request the kernel to unload a kext with a given bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1562908-kextmanagercopyloadedkextinfo)*