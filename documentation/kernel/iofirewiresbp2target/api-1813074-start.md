# start

**Framework**: Kernel  
**Kind**: instm

During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.

## Declaration

```cpp
virtual bool start(
 IOService *provider );
```

#### Return Value

Return true if the start was successful, false otherwise (which will cause the instance to be detached and usually freed).

#### Overview

See IOService for discussion.

## See Also

### Miscellaneous
- [getFireWireUnit](./api-1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](./api-1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](./api-1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](./api-1813037-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](./api-1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [stop](./api-1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1813074-start)*