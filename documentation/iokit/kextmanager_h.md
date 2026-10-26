# KextManager.h

**Framework**: IOKit  
**Role**: API Collection

The KextManager API provides a simple interface for applications to load kernel extensions (kexts) via RPC to kextd, and to look up the URLs for kexts by bundle identifier.

#### Overview

##### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <libkern/OSReturn.h>
- <sys/cdefs.h>

## Topics

### Miscellaneous
- [KextManagerCopyLoadedKextInfo](./api-1562908-kextmanagercopyloadedkextinfo.md)
  Returns information about loaded kexts in a dictionary.
- [KextManagerCreateURLForBundleIdentifier](./api-1562905-kextmanagercreateurlforbundleide.md)
  Create a URL locating a kext with a given bundle identifier.
- [KextManagerLoadKextWithIdentifier](./api-1562907-kextmanagerloadkextwithidentifie.md)
  Request the kext loading system to load a kext with a given bundle identifier.
- [KextManagerLoadKextWithURL](./api-1562906-kextmanagerloadkextwithurl.md)
  Request the kext loading system to load a kext with a given URL.
- [KextManagerUnloadKextWithIdentifier](./api-1562904-kextmanagerunloadkextwithidentif.md)
  Request the kernel to unload a kext with a given bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kextmanager_h)*