# releaseNotificationPort

**Framework**: Kernel  
**Kind**: instm

Release the mach_port_t passed to registerNotificationPort().

## Declaration

```c
static IOReturn releaseNotificationPort(
 mach_port_treference);
```

#### Return Value

A return code.

#### Overview

The mach_port_t passed to the registerNotificationPort() methods should be released to balance each call to registerNotificationPort(). Behavior is undefined if these calls are not correctly balanced.

## Parameters

- `reference`: The mach_port_t argument previously passed to the subclass implementation of registerNotificationPort().

## See Also

### Miscellaneous
- [exportObjectToClient](./api-1809421-exportobjecttoclient.md)
- [releaseAsyncReference64](./api-1809435-releaseasyncreference64.md)
  Release the mach_port_t reference held within the OSAsyncReference64 structure.
- [removeMappingForDescriptor](./api-1809451-removemappingfordescriptor.md)
- [sendAsyncResult64WithOptions](./api-1809458-sendasyncresult64withoptions.md)
  Send a notification as with sendAsyncResult, but with finite queueing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient/1809442-releasenotificationport)*