# matchPropertyTable

**Framework**: Kernel  
**Kind**: instm

Implements SBP2 specific matching.

## Declaration

```swift
virtual bool matchPropertyTable(
 OSDictionary *table );
```

#### Return_value

Returns false if the family considers the matching dictionary does not match in properties it understands, true otherwise.

#### Overview

See IOService for discussion.

## Parameters

- `table`: The dictionary of properties to be matched against.

## See Also

- [getFireWireUnit](iofirewiresbp2target/1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](iofirewiresbp2target/1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](iofirewiresbp2target/1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewiresbp2target/1813037-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [start](iofirewiresbp2target/1813074-start.md)
  During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.
- [stop](iofirewiresbp2target/1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target/1813051-matchpropertytable)*