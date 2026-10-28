# GetAckCode

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets the most recently received ack code for this transaction.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
UInt32 (*GetAckCode)(IOFireWireLibCommandRef self);
```

## Return Value

The FireWire ack code.

## Parameters

- `self`: A reference to the command

## See Also

### Miscellaneous
- [Cancel](./api-1556085-cancel.md)
  Cancel command execution
- [GetBuffer](./api-1555715-getbuffer.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.
- [GetRefCon](./api-1555645-getrefcon.md)
  Gets the refcon associated with this command
- [GetResponseCode](./api-1556076-getresponsecode.md)
  Gets the most recently received response code for this transaction.
- [GetStatus](./api-1555697-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555626-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1555792-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1555918-isexecuting.md)
  Is this command object currently executing?
- [SetBuffer](./api-1556094-setbuffer.md)
  Set the buffer where read data should be stored.
- [SetCallback](./api-1555992-setcallback.md)
  Set the completion handler to be called once the command completes asynchronous execution .
- [SetChannel](./api-1556108-setchannel.md)
  Set the new channel to transmit the AsyncStream command.
- [SetFlags](./api-1555736-setflags.md)
  Set flags governing this command's execution.
- [SetGeneration](./api-1555988-setgeneration.md)
  Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.
- [SetMaxPacket](./api-1555624-setmaxpacket.md)
  Set the maximum size in bytes of packets transferred by this command.
- [SetMaxPacketSpeed](./api-1555695-setmaxpacketspeed.md)
  Gets the most recently received ack code for this transaction.
- [SetMaxRetryCount](./api-1555983-setmaxretrycount.md)
  Sets the maximum number of retries for this command.
- [SetRefCon](./api-1555818-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetSyncBits](./api-1556029-setsyncbits.md)
  Set the sync bits for the AsynStream packets.
- [SetTagBits](./api-1555862-settagbits.md)
  Set the tag bits for the AsynStream packets.
- [SetTarget](./api-1555682-settarget.md)
  Set command target address
- [SetTimeoutDuration](./api-1555946-settimeoutduration.md)
  Sets the duration of the timeout for this command.
- [Submit](./api-1556112-submit.md)
- [SubmitWithRefconAndCallback](./api-1556071-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireasyncstreamcommandinterface/1555749-getackcode)*