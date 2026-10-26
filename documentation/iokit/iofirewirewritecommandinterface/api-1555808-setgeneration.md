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
- `generation`: A bus generation. The current bus generation can be obtained from IOFireWireDeviceInterface::GetBusGeneration().

## See Also

### Miscellaneous
- [Cancel](./api-1555937-cancel.md)
  Cancel command execution
- [GetAckCode](./api-1555840-getackcode.md)
  Gets the most recently received ack code for this transaction.
- [GetBuffer](./api-1556087-getbuffer.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.
- [GetRefCon](./api-1556025-getrefcon.md)
  Gets the refcon associated with this command
- [GetResponseCode](./api-1555747-getresponsecode.md)
  Gets the most recently received response code for this transaction.
- [GetStatus](./api-1555704-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555717-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1555826-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1556047-isexecuting.md)
  Is this command object currently executing?
- [SetBuffer](./api-1555806-setbuffer.md)
  Set the buffer where read data should be stored.
- [SetCallback](./api-1555617-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetFlags](./api-1555905-setflags.md)
  Set flags governing this command's execution.
- [SetMaxPacket](./api-1556074-setmaxpacket.md)
  Set the maximum size in bytes of packets transferred by this command.
- [SetMaxPacketSpeed](./api-1555694-setmaxpacketspeed.md)
  Gets the most recently received ack code for this transaction.
- [SetMaxRetryCount](./api-1556117-setmaxretrycount.md)
  Sets the maximum number of retries for this command.
- [SetRefCon](./api-1555888-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTarget](./api-1555875-settarget.md)
  Set command target address
- [SetTimeoutDuration](./api-1555955-settimeoutduration.md)
  Sets the duration of the timeout for this command.
- [Submit](./api-1555990-submit.md)
- [SubmitWithRefconAndCallback](./api-1555927-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirewritecommandinterface/1555808-setgeneration)*