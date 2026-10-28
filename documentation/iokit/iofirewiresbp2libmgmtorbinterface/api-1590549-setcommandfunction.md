# setCommandFunction

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the function of the management ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*setCommandFunction)(void *self, UInt32 function);
```

## Return Value

Returns kIOReturnSuccess if function was a legal function.

## Discussion

Sets the the function of the management ORB. Legal values are kFWSBP2QueryLogins, kFWSBP2AbortTask, kFWSBP2AbortTaskSet, kFWSBP2LogicalUnitReset, and kFWSBP2TargetReset.

## Parameters

- `self`: Pointer to a IOFireWireSBP2LibMgmtORBInterface.
- `function`: a value indicating the desired management function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libmgmtorbinterface/1590549-setcommandfunction)*