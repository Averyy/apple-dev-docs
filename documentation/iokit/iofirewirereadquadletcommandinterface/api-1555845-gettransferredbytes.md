# GetTransferredBytes

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Return number of bytes transferred by this command object when it last completed execution.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
UInt32 (*GetTransferredBytes)(IOFireWireLibCommandRef self);
```

#### Return Value

A UInt32 containing the bytes transferred value

#### Discussion

Availability: (for interfaces obtained with ID)

|  | `kIOFireWireAsyncStreamCommandInterfaceID` | YES |
| --- | --- | --- |
|  | `kIOFireWireCompareSwapCommandInterfaceID` | YES |
|  | `kIOFireWireWriteQuadletCommandInterfaceID` | YES |
|  | `kIOFireWireReadQuadletCommandInterfaceID` | YES |
|  | `kIOFireWireWriteCommandInterfaceID_v2` | YES |
|  | `kIOFireWireWriteCommandInterfaceID` | YES |
|  | `kIOFireWireReadCommandInterfaceID_v2` | YES |
|  | `kIOFireWireReadCommandInterfaceID` | YES |

## Parameters

- `self`: The command object interface of interest

## See Also

### Miscellaneous
- [Cancel](./api-1555751-cancel.md)
  Cancel command execution
- [GetStatus](./api-1555890-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555821-gettargetaddress.md)
  Get command target address.
- [IsExecuting](./api-1555970-isexecuting.md)
  Is this command object currently executing?
- [SetCallback](./api-1555924-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetGeneration](./api-1555768-setgeneration.md)
  Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.
- [SetQuads](./api-1556027-setquads.md)
  Set destination for read data
- [SetRefCon](./api-1556073-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTarget](./api-1556064-settarget.md)
  Set command target address
- [Submit](./api-1555710-submit.md)
- [SubmitWithRefconAndCallback](./api-1555919-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirereadquadletcommandinterface/1555845-gettransferredbytes)*