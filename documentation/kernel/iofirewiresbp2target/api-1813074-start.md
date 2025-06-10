# start

**Framework**: Kernel  
**Kind**: instm

During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.

## Declaration

```swift
virtual bool start(
 IOService *provider );
```

#### Return_value

Return true if the start was successful, false otherwise (which will cause the instance to be detached and usually freed).

#### Overview

See IOService for discussion.

## See Also

- [getFireWireUnit](iofirewiresbp2target/1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](iofirewiresbp2target/1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](iofirewiresbp2target/1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewiresbp2target/1813037-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2target/1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [stop](iofirewiresbp2target/1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1813074-start)*