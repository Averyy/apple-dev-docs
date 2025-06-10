# handleIsOpen

**Framework**: Kernel  
**Kind**: instm

Overrideable method to control the open / close behaviour of an IOService.

## Declaration

```swift
virtual bool handleIsOpen(
 const IOService *forClient ) const;
```

#### Return_value

Returns true if the specific, or any, client has the IOService open.

#### Overview

See IOService for discussion.

## Parameters

- `forClient`: If non-zero, isOpen returns the open state for that client. If zero is passed, isOpen returns the open state for all clients.

## See Also

- [getFireWireUnit](iofirewiresbp2target/1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](iofirewiresbp2target/1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewiresbp2target/1813037-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2target/1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [start](iofirewiresbp2target/1813074-start.md)
  During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.
- [stop](iofirewiresbp2target/1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1813021-handleisopen)*