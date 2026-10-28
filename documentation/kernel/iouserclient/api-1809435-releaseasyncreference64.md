# releaseAsyncReference64

**Framework**: Kernel  
**Kind**: instm

Release the mach_port_t reference held within the OSAsyncReference64 structure.

## Declaration

```c
static IOReturn releaseAsyncReference64(
 OSAsyncReference64reference);
```

## Return Value

A return code.

## Overview

The OSAsyncReference64 structure passed to async methods holds a reference to the wakeup mach port, which should be released to balance each async method call. Behavior is undefined if these calls are not correctly balanced.

## Parameters

- `reference`: The reference passed to the subclass IOAsyncMethod, or externalMethod() in the IOExternalMethodArguments.asyncReference field.

## See Also

### Miscellaneous
- [exportObjectToClient](./api-1809421-exportobjecttoclient.md)
- [releaseNotificationPort](./api-1809442-releasenotificationport.md)
  Release the mach_port_t passed to registerNotificationPort().
- [removeMappingForDescriptor](./api-1809451-removemappingfordescriptor.md)
- [sendAsyncResult64WithOptions](./api-1809458-sendasyncresult64withoptions.md)
  Send a notification as with sendAsyncResult, but with finite queueing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient/1809435-releaseasyncreference64)*