# setCommandBlock

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the command block portion of the ORB.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*setCommandBlock)(void *self, void *buffer, UInt32 length);
```

#### Return Value

Returns KIOReturnSuccess if the command block was updated successfully.

#### Discussion

Copys the data provided in the buffer to the command block portion of the ORB.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibORBInterface.
- `buffer`: Pointer to buffer to copy command block from.
- `length`: Number of bytes of data to copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liborbinterface/1590526-setcommandblock)*