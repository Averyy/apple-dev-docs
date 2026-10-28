# handleOpen

**Framework**: Kernel  
**Kind**: instm

Overrideable method to control the open / close behaviour of an IOService.

## Declaration

```cpp
virtual bool handleOpen(
 IOService *forClient,
 IOOptionBits options,
 void *arg );
```

## Return Value

Return true if the open was successful, false otherwise.

## Overview

See IOService for discussion.

## Parameters

- `forClient`: Designates the client of the provider requesting the open.
- `options`: Options for the open, may be interpreted by the implementor of handleOpen.

## See Also

### Miscellaneous
- [getFireWireUnit](./api-1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](./api-1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](./api-1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [start](./api-1813074-start.md)
  During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.
- [stop](./api-1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1813037-handleopen)*