# exportObjectToClient

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn exportObjectToClient(
 task_ttask, 
 OSObject *obj,
 io_object_t *clientObj);
```

## Overview

Make an arbitrary OSObject available to the client task.

## Parameters

- `task`: The task.
- `obj`: The object we want to export to the client.
- `clientObj`: Returned value is the client's port name.

## See Also

### Miscellaneous
- [releaseAsyncReference64](./api-1809435-releaseasyncreference64.md)
  Release the mach_port_t reference held within the OSAsyncReference64 structure.
- [releaseNotificationPort](./api-1809442-releasenotificationport.md)
  Release the mach_port_t passed to registerNotificationPort().
- [removeMappingForDescriptor](./api-1809451-removemappingfordescriptor.md)
- [sendAsyncResult64WithOptions](./api-1809458-sendasyncresult64withoptions.md)
  Send a notification as with sendAsyncResult, but with finite queueing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iouserclient/1809421-exportobjecttoclient)*