# getFireWireUnit

**Framework**: Kernel  
**Kind**: instm

Returns an IOFireWireUnit object.

## Declaration

```cpp
virtual IOFireWireUnit * getFireWireUnit(
 void );
```

## Return Value

Returns a pointer to an IOFireWireUnit.

## Overview

An IOFireWireUnit is the provider of an IOFireWireSBP2Target. In order to use the base FireWire services you will need a reference to the unit. This method returns that reference.

## See Also

### Miscellaneous
- [handleClose](./api-1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](./api-1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](./api-1813037-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [start](./api-1813074-start.md)
  During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.
- [stop](./api-1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1812999-getfirewireunit)*