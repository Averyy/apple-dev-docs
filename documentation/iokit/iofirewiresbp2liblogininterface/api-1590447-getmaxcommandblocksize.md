# getMaxCommandBlockSize

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the maximum command block size.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt32 (*getMaxCommandBlockSize)(void *self);
```

## Return Value

Returns a UInt32 containing the maximum command block size.

## Discussion

The device publishes an upper limit on the size of command block that it can accept. That value can be accessed via this method.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590447-getmaxcommandblocksize)*