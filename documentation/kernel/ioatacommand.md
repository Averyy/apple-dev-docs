# IOATACommand

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 11.0+

## Declaration

```cpp
class IOATACommand : IOCommand
```

## Overview

Command structure superclass, created and freed only by IOATADevice objects populated by disk device drivers with command parameters then submitted for operation to their IOATADevice provider for execution.

IOATACommand is a virtual class, a concrete subclass contains the methods and fields needed by IOATAControllers. Subclasses may be specific to particular controller hardware. Disk device drivers will only have visibility to this interface and may not subclass this object. Disk device drivers should instead make use of the void* refcon field which the controllers will not touch

## Topics

### Miscellaneous
- [getActualTransfer](./ioatacommand/api-1813827-getactualtransfer.md)
  The byte count on the ending result, as best as can be determined by the controller. May be zero, but partial transfer may have occurred on error in some cases.
- [getBuffer](./ioatacommand/api-1813832-getbuffer.md)
  the IOMemoryDescriptor used in this transaction.
- [getCommandInUse](./ioatacommand/api-1813837-getcommandinuse.md)
  returns true if IOATAController is still in control of the command.
- [getCylHi](./ioatacommand/api-1813841-getcylhi.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getCylLo](./ioatacommand/api-1813846-getcyllo.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getDevice_Head](./ioatacommand/api-1813849-getdevice_head.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getEndErrorReg](./ioatacommand/api-1813854-getenderrorreg.md)
  If the error bit was set in the status register, the value of the error register is returned at the end of a command.
- [getEndStatusReg](./ioatacommand/api-1813858-getendstatusreg.md)
  the value of the status register on the end of the command.
- [getErrorReg](./ioatacommand/api-1813861-geterrorreg.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getResult](./ioatacommand/api-1813865-getresult.md)
  IOReturn value of the result of this command. ATA family errors are defined in IOATATypes.h
- [getSectorCount](./ioatacommand/api-1813869-getsectorcount.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getSectorNumber](./ioatacommand/api-1813872-getsectornumber.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [getStatus](./ioatacommand/api-1813875-getstatus.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setBuffer](./ioatacommand/api-1813877-setbuffer.md)
  set the IIOMemoryDescriptor for this transaction.
- [setByteCount](./ioatacommand/api-1813880-setbytecount.md)
  set the byte count for this transaction. Should agree with the device command and the memory descriptor in use.
- [setCallbackPtr](./ioatacommand/api-1813883-setcallbackptr.md)
  set the function pointer to call when this command completes.
- [setCommand](./ioatacommand/api-1813885-setcommand.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setCylHi](./ioatacommand/api-1813887-setcylhi.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setCylLo](./ioatacommand/api-1813888-setcyllo.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setDevice_Head](./ioatacommand/api-1813890-setdevice_head.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setFeatures](./ioatacommand/api-1813892-setfeatures.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setFlags](./ioatacommand/api-1813894-setflags.md)
  set the flags for this command, as defined in IOATATypes.
- [setLBA28](./ioatacommand/api-1813896-setlba28.md)
  convenience method that sets the taskfile registers into a 28-bit LBA address, with unit selected and LBA bit set. return err if param out of range, return kIOSuccess (kATANoErr) = 0 on return if successful
- [setOpcode](./ioatacommand/api-1813898-setopcode.md)
  command opcode as defined in IOATATypes.
- [setPacketCommand](./ioatacommand/api-1813900-setpacketcommand.md)
  ATAPI command packet max size is 16 bytes. Makes deep copy of data.
- [setPosition](./ioatacommand/api-1813902-setposition.md)
  used to set an offset into the memory descriptor for this transfer.
- [setRegMask](./ioatacommand/api-1813904-setregmask.md)
  used when accessing registers or reading registers on an error result. Mask is defined in IOATATypes.h
- [setSectorCount](./ioatacommand/api-1813906-setsectorcount.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setSectorNumber](./ioatacommand/api-1813908-setsectornumber.md)
  Taskfile access. Registers are named in accordance with ATA Standards conventions
- [setTimeoutMS](./ioatacommand/api-1813910-settimeoutms.md)
  how long to allow this command to complete, in milliseconds, once issued to the hardware. if the time period expires, this command will return with a timeout error.
- [setTransferChunkSize](./ioatacommand/api-1813912-settransferchunksize.md)
  set the size of transfer between intervening interrupts. necessary when doing PIO Read/Write Multiple, etc. so the controller knows when to expect an interrupt during multi-sector data transfers.
- [setUnit](./ioatacommand/api-1813914-setunit.md)
  set the unit number for this command.
- [zeroCommand](./ioatacommand/api-1813915-zerocommand.md)
  set to blank state, MUST call prior to re-use of this object
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [refCon2](./ioatacommand/refcon2.md)
  for use by disk drivers, clients of IOATADevice only. IOATADevice and IOATAControllers shall not use this field in any manner.
- [refCon](./ioatacommand/refcon.md)
  for use by disk drivers, clients of IOATADevice only. IOATADevice and IOATAControllers shall not use this field in any manner.
- [fExpansionData](./ioatacommand/fexpansiondata.md)
### Instance Methods
- [- free](./ioatacommand/api-1392056-free.md)
- [- getActualTransfer](./ioatacommand/api-1392104-getactualtransfer.md)
- [- getAltStatus](./ioatacommand/api-1392045-getaltstatus.md)
- [- getBuffer](./ioatacommand/api-1392172-getbuffer.md)
- [- getCommandInUse](./ioatacommand/api-1392170-getcommandinuse.md)
- [- getCylHi](./ioatacommand/api-1392083-getcylhi.md)
- [- getCylLo](./ioatacommand/api-1392063-getcyllo.md)
- [- getDataReg](./ioatacommand/api-1392069-getdatareg.md)
- [- getDevice_Head](./ioatacommand/api-1392079-getdevice_head.md)
- [- getEndErrorReg](./ioatacommand/api-1392061-getenderrorreg.md)
- [- getEndStatusReg](./ioatacommand/api-1392054-getendstatusreg.md)
- [- getErrorReg](./ioatacommand/api-1392123-geterrorreg.md)
- [- getExtendedLBA](./ioatacommand/api-1392043-getextendedlba.md)
- [- getMetaClass](./ioatacommand/api-1392058-getmetaclass.md)
- [- getResult](./ioatacommand/api-1392142-getresult.md)
- [- getSectorCount](./ioatacommand/api-1392151-getsectorcount.md)
- [- getSectorNumber](./ioatacommand/api-1392091-getsectornumber.md)
- [- getStatus](./ioatacommand/api-1392158-getstatus.md)
- [- init](./ioatacommand/api-1392118-init.md)
- [- setBuffer](./ioatacommand/api-1392139-setbuffer.md)
- [- setByteCount](./ioatacommand/api-1392113-setbytecount.md)
- [- setCallbackPtr](./ioatacommand/api-1392047-setcallbackptr.md)
- [- setCommand](./ioatacommand/api-1392106-setcommand.md)
- [- setControl](./ioatacommand/api-1392134-setcontrol.md)
- [- setCylHi](./ioatacommand/api-1392065-setcylhi.md)
- [- setCylLo](./ioatacommand/api-1392087-setcyllo.md)
- [- setDataReg](./ioatacommand/api-1392111-setdatareg.md)
- [- setDevice_Head](./ioatacommand/api-1392126-setdevice_head.md)
- [- setEndResult](./ioatacommand/api-1392100-setendresult.md)
- [- setFeatures](./ioatacommand/api-1392154-setfeatures.md)
- [- setFlags](./ioatacommand/api-1392168-setflags.md)
- [- setLBA28](./ioatacommand/api-1392049-setlba28.md)
- [- setOpcode](./ioatacommand/api-1392166-setopcode.md)
- [- setPacketCommand](./ioatacommand/api-1392097-setpacketcommand.md)
- [- setPosition](./ioatacommand/api-1392077-setposition.md)
- [- setRegMask](./ioatacommand/api-1392075-setregmask.md)
- [- setSectorCount](./ioatacommand/api-1392144-setsectorcount.md)
- [- setSectorNumber](./ioatacommand/api-1392067-setsectornumber.md)
- [- setTimeoutMS](./ioatacommand/api-1392093-settimeoutms.md)
- [- setTransferChunkSize](./ioatacommand/api-1392109-settransferchunksize.md)
- [- setUnit](./ioatacommand/api-1392116-setunit.md)
- [- zeroCommand](./ioatacommand/api-1392132-zerocommand.md)

## Relationships

### Inherits From
- [IOCommand](./iocommand.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacommand)*