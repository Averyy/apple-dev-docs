# handleOpen

**Framework**: Kernel  
**Kind**: instm

Overrideable method to control the open / close behaviour of an IOService.

## Declaration

```swift
virtual bool handleOpen(
 IOService *forClient,
 IOOptionBits options,
 void *arg );
```

#### Return_value

Return true if the open was successful, false otherwise.

#### Overview

See IOService for discussion.

## Parameters

- `forClient`: Designates the client of the provider requesting the open.
- `options`: Options for the open, may be interpreted by the implementor of handleOpen.

## See Also

- [getFireWireUnit](iofirewiresbp2target/1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](iofirewiresbp2target/1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](iofirewiresbp2target/1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2target/1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [start](iofirewiresbp2target/1813074-start.md)
  During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.
- [stop](iofirewiresbp2target/1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1813037-handleopen)*