# SetGeneration

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*SetGeneration)(IOFireWireLibCommandRef self, UInt32 generation);
```

## Discussion

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
- `generation`: A bus generation. The current bus generation can be obtained from IOFireWireDeviceInterface::GetBusGeneration().

## See Also

### Miscellaneous
- [Cancel](./api-1556061-cancel.md)
  Cancel command execution
- [DidLock](./api-1556007-didlock.md)
  Was the last lock operation successful?
- [GetStatus](./api-1555930-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555789-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1555667-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1556082-isexecuting.md)
  Is this command object currently executing?
- [Locked](./api-1555630-locked.md)
  Get the 32-bit value returned on the last compare swap operation.
- [Locked64](./api-1555657-locked64.md)
  Get the 64-bit value returned on the last compare swap operation.
- [SetCallback](./api-1555948-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetFlags](./api-1555745-setflags.md)
  Set flags governing this command's execution.
- [SetRefCon](./api-1555702-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTarget](./api-1556016-settarget.md)
  Set command target address
- [SetValues](./api-1555784-setvalues.md)
  Set values for 32-bit compare swap operation. Calling this function will make the command object perform 32-bit compare swap transactions on the bus. To perform 64-bit compare swap operations, use the SetValues64() call, below.
- [SetValues64](./api-1555877-setvalues64.md)
  Set values for 64-bit compare swap operation. Calling this function will make the command object perform 64-bit compare swap transactions on the bus. To perform 32-bit compare swap operations, use the SetValues() call, above.
- [Submit](./api-1555647-submit.md)
- [SubmitWithRefconAndCallback](./api-1555675-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirecompareswapcommandinterface/1555712-setgeneration)*