# SetTarget

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set command target address

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*SetTarget)(IOFireWireLibCommandRef self, const FWAddress *addr);
```

#### Discussion

Availability: (for interfaces obtained with ID)

|  | `kIOFireWireAsyncStreamCommandInterfaceID` | NO |
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
- `addr`: A pointer to an FWAddress.

## See Also

### Miscellaneous
- [Cancel](./api-1555777-cancel.md)
  Cancel command execution
- [GetAckCode](./api-1555872-getackcode.md)
  Gets the most recently received ack code for this transaction.
- [GetBuffer](./api-1555635-getbuffer.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.
- [GetRefCon](./api-1555913-getrefcon.md)
  Gets the refcon associated with this command
- [GetResponseCode](./api-1556088-getresponsecode.md)
  Gets the most recently received response code for this transaction.
- [GetStatus](./api-1555748-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555863-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1555596-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1556091-isexecuting.md)
  Is this command object currently executing?
- [SetBuffer](./api-1555851-setbuffer.md)
  Set the buffer where read data should be stored.
- [SetCallback](./api-1556068-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetFlags](./api-1555656-setflags.md)
  Set flags governing this command's execution.
- [SetGeneration](./api-1555934-setgeneration.md)
  Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.
- [SetMaxPacket](./api-1555815-setmaxpacket.md)
  Set the maximum size in bytes of packets transferred by this command.
- [SetMaxPacketSpeed](./api-1555772-setmaxpacketspeed.md)
  Gets the most recently received ack code for this transaction.
- [SetMaxRetryCount](./api-1555707-setmaxretrycount.md)
  Sets the maximum number of retries for this command.
- [SetRefCon](./api-1555804-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTimeoutDuration](./api-1555721-settimeoutduration.md)
  Sets the duration of the timeout for this command.
- [Submit](./api-1556104-submit.md)
- [SubmitWithRefconAndCallback](./api-1555644-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirecommandinterface/1556002-settarget)*