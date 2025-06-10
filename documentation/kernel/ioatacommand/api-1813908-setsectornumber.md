# setSectorNumber

**Framework**: Kernel  
**Kind**: instm

Taskfile access. Registers are named in accordance with ATA Standards conventions

## Declaration

```swift
virtual void setSectorNumber(
 UInt8 in);
```

## See Also

- [getActualTransfer](ioatacommand/1813827-getactualtransfer.md)
  The byte count on the ending result, as best as can be determined by the controller. May be zero, but partial transfer may have occurred on error in some cases.
- [getBuffer](ioatacommand/1813832-getbuffer.md)
  the IOMemoryDescriptor used in this transaction.
- [getCommandInUse](ioatacommand/1813837-getcommandinuse.md)
  returns true if IOATAController is still in control of the command.
- [getCylHi](ioatacommand/1813841-getcylhi.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getCylLo](ioatacommand/1813846-getcyllo.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getDevice_Head](ioatacommand/1813849-getdevice_head.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getEndErrorReg](ioatacommand/1813854-getenderrorreg.md)
  If the error bit was set in the status register, the value of the error register is returned at the end of a command.
- [getEndStatusReg](ioatacommand/1813858-getendstatusreg.md)
  the value of the status register on the end of the command.
- [getErrorReg](ioatacommand/1813861-geterrorreg.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getResult](ioatacommand/1813865-getresult.md)
  IOReturn value of the result of this command. ATA family errors are defined in IOATATypes.h
- [getSectorCount](ioatacommand/1813869-getsectorcount.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getSectorNumber](ioatacommand/1813872-getsectornumber.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getStatus](ioatacommand/1813875-getstatus.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setBuffer](ioatacommand/1813877-setbuffer.md)
  set the IIOMemoryDescriptor for this transaction.
- [setByteCount](ioatacommand/1813880-setbytecount.md)
  set the byte count for this transaction. Should agree with the device command and the memory descriptor in use.
- [setCallbackPtr](ioatacommand/1813883-setcallbackptr.md)
  set the function pointer to call when this command completes.
- [setCommand](ioatacommand/1813885-setcommand.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setCylHi](ioatacommand/1813887-setcylhi.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setCylLo](ioatacommand/1813888-setcyllo.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setDevice_Head](ioatacommand/1813890-setdevice_head.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setFeatures](ioatacommand/1813892-setfeatures.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setFlags](ioatacommand/1813894-setflags.md)
  set the flags for this command, as defined in IOATATypes.
- [setLBA28](ioatacommand/1813896-setlba28.md)
  convenience method that sets the taskfile registers into a 28-bit LBA address, with unit selected and LBA bit set. return err if param out of range, return kIOSuccess (kATANoErr) = 0 on return if successful
- [setOpcode](ioatacommand/1813898-setopcode.md)
  command opcode as defined in IOATATypes.
- [setPacketCommand](ioatacommand/1813900-setpacketcommand.md)
  ATAPI command packet max size is 16 bytes. Makes deep copy of data.
- [setPosition](ioatacommand/1813902-setposition.md)
  used to set an offset into the memory descriptor for this transfer.
- [setRegMask](ioatacommand/1813904-setregmask.md)
  used when accessing registers or reading registers on an error result. Mask is defined in IOATATypes.h
- [setSectorCount](ioatacommand/1813906-setsectorcount.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setTimeoutMS](ioatacommand/1813910-settimeoutms.md)
  how long to allow this command to complete, in milliseconds, once issued to the hardware. if the time period expires, this command will return with a timeout error.
- [setTransferChunkSize](ioatacommand/1813912-settransferchunksize.md)
  set the size of transfer between intervening interrupts. necessary when doing PIO Read/Write Multiple, etc. so the controller knows when to expect an interrupt during multi-sector data transfers.
- [setUnit](ioatacommand/1813914-setunit.md)
  set the unit number for this command.
- [zeroCommand](ioatacommand/1813915-zerocommand.md)
  set to blank state, MUST call prior to re-use of this object


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacommand/1813908-setsectornumber)*