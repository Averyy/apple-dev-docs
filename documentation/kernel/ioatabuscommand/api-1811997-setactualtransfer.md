# setActualTransfer

**Framework**: Kernel  
**Kind**: instm

set the byte count of bytes actually transferred.

## Declaration

```swift
virtual void setActualTransfer (
 IOByteCount bytesTransferred );
```

## See Also

- [allocateCmd](ioatabuscommand/1811850-allocatecmd.md)
  factory method to create an instance of this class used by subclasses of IOATADevice
- [executeCallback](ioatabuscommand/1811860-executecallback.md)
  call the completion callback function
- [getBuffer](ioatabuscommand/1811872-getbuffer.md)
  get pointer to the memory descriptor for this transaction
- [getByteCount](ioatabuscommand/1811883-getbytecount.md)
  return the byte count for this transaction to transfer.
- [getCallbackPtr](ioatabuscommand/1811895-getcallbackptr.md)
  return the callback pointer
- [getFlags](ioatabuscommand/1811906-getflags.md)
  return the flags for this command.
- [getOpcode](ioatabuscommand/1811919-getopcode.md)
  return the command opcode
- [getPacketData](ioatabuscommand/1811925-getpacketdata.md)
  return pointer to the array of packet data.
- [getPacketSize](ioatabuscommand/1811935-getpacketsize.md)
  return the size of atapi packet if any.
- [getPosition](ioatabuscommand/1811945-getposition.md)
  the position within the memory buffer for the transaction.
- [getRegMask](ioatabuscommand/1811953-getregmask.md)
  get the register mask for desired regs
- [getTaskFilePtr](ioatabuscommand/1811963-gettaskfileptr.md)
  return the taskfile structure pointer.
- [getTimeoutMS](ioatabuscommand/1811972-gettimeoutms.md)
  return the timeout value for this command
- [getTransferChunkSize](ioatabuscommand/1811979-gettransferchunksize.md)
  number of bytes between interrupts.
- [getUnit](ioatabuscommand/1811986-getunit.md)
  return the unit id (0 primary, 1 secondary)
- [init](ioatabuscommand/1811993-init.md)
  Zeroes all data, returns false if allocation fails. protected.
- [setCommandInUse](ioatabuscommand/1812002-setcommandinuse.md)
  mark the command as being in progress.
- [setResult](ioatabuscommand/1812006-setresult.md)
  set the result code
- [zeroCommand](ioatabuscommand/1812011-zerocommand.md)
  set to blank state, call prior to re-use of this object


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatabuscommand/1811997-setactualtransfer)*