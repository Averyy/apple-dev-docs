# SetFlags

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set flags governing this command's execution.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
void (*SetFlags)(IOFireWireLibCommandRef self, UInt32 inFlags);
```

## Discussion

Availability: (for interfaces obtained with ID)

|  | `kIOFireWireAsyncStreamCommandInterfaceID` | YES |
| --- | --- | --- |
|  | `kIOFireWireCompareSwapCommandInterfaceID` | NO |
|  | `kIOFireWireWriteQuadletCommandInterfaceID` | NO |
|  | `kIOFireWireReadQuadletCommandInterfaceID` | NO |
|  | `kIOFireWireWriteCommandInterfaceID_v2` | YES |
|  | `kIOFireWireWriteCommandInterfaceID` | NO |
|  | `kIOFireWireReadCommandInterfaceID_v2` | YES |
|  | `kIOFireWireReadCommandInterfaceID` | NO |

## Parameters

- `self`: The command object interface of interest
- `inFlags`: A UInt32 with bits set corresponding to the flags that should be set for this command object. The following values may be used:

  - kFWCommandNoFlags -- all flags off
  - kFWCommandInterfaceForceNoCopy -- data sent by this command should always be received/sent directly from the buffer set with SetBuffer(). Whatever data is in the buffer when the command is submitted will be used.
  - kFWCommandInterfaceForceCopyAlways -- data will always be copied out of the command object data buffer when SetBuffer() is called, up to a maximum allowed size (kFWUserCommandSubmitWithCopyMaxBufferBytes). This can result in faster data transfer. Changes made to the data buffer contents after calling SetBuffer() will be ignored; SetBuffer() should be called whenever the data buffer contents change.
  - kFWCommandInterfaceSyncExecute -- Setting this flag causes the command object to execute synchronously. The calling context will block until the command object has completed execution or an error occurs. Using synchronous execution can avoid kernel transitions associated with asynchronous completion and often remove the need for a state machine.
  - kFWCommandInterfaceForceBlockRequest -- Setting this flag causes read and write transactions to use block request packets even if the payload is 4 bytes. If this flag is not set 4 byte transactions will occur using quadlet transactions.

## See Also

### Miscellaneous
- [Cancel](./api-1555896-cancel.md)
  Cancel command execution
- [DidLock](./api-1555844-didlock.md)
  Was the last lock operation successful?
- [GetAckCode](./api-1555800-getackcode.md)
  Gets the most recently received ack code for this transaction.
- [GetBuffer](./api-1555973-getbuffer.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.
- [GetRefCon](./api-1555971-getrefcon.md)
  Gets the refcon associated with this command
- [GetResponseCode](./api-1555785-getresponsecode.md)
  Gets the most recently received response code for this transaction.
- [GetStatus](./api-1555987-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555653-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1556080-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1555728-isexecuting.md)
  Is this command object currently executing?
- [Locked](./api-1556070-locked.md)
  Get the 32-bit value returned on the last compare swap operation.
- [Locked64](./api-1555892-locked64.md)
  Get the 64-bit value returned on the last compare swap operation.
- [SetBuffer](./api-1556056-setbuffer.md)
  Set the buffer where read data should be stored.
- [SetCallback](./api-1555951-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetGeneration](./api-1555663-setgeneration.md)
  Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.
- [SetMaxPacket](./api-1555720-setmaxpacket.md)
  Set the maximum size in bytes of packets transferred by this command.
- [SetMaxPacketSpeed](./api-1555812-setmaxpacketspeed.md)
  Gets the most recently received ack code for this transaction.
- [SetMaxRetryCount](./api-1556086-setmaxretrycount.md)
  Sets the maximum number of retries for this command.
- [SetRefCon](./api-1556042-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTarget](./api-1555954-settarget.md)
  Set command target address
- [SetTimeoutDuration](./api-1556059-settimeoutduration.md)
  Sets the duration of the timeout for this command.
- [SetValues](./api-1556032-setvalues.md)
  Set values for 32-bit compare swap operation. Calling this function will make the command object perform 32-bit compare swap transactions on the bus. To perform 64-bit compare swap operations, use the SetValues64() call, below.
- [SetValues64](./api-1555705-setvalues64.md)
  Set values for 64-bit compare swap operation. Calling this function will make the command object perform 64-bit compare swap transactions on the bus. To perform 32-bit compare swap operations, use the SetValues() call, above.
- [Submit](./api-1555869-submit.md)
- [SubmitWithRefconAndCallback](./api-1556003-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirecompareswapcommandinterface_v3/1555723-setflags)*