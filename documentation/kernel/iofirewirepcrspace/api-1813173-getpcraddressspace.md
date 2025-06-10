# getPCRAddressSpace

**Framework**: Kernel  
**Kind**: instm

returns the IOFireWirePCRSpace object for the given FireWire bus

## Declaration

```swift
static IOFireWirePCRSpace *getPCRAddressSpace(
 IOFireWireBus *bus);
```

## Parameters

- `bus`: The FireWire bus

## See Also

- [allocateInputPlug](iofirewirepcrspace/1813120-allocateinputplug.md)
  allocates an input plug.
- [allocateOutputPlug](iofirewirepcrspace/1813128-allocateoutputplug.md)
  allocates an output plug.
- [clearAllP2PConnections](iofirewirepcrspace/1813138-clearallp2pconnections.md)
- [freeInputPlug](iofirewirepcrspace/1813150-freeinputplug.md)
  deallocates an input plug.
- [freeOutputPlug](iofirewirepcrspace/1813163-freeoutputplug.md)
  deallocates an output plug.
- [init](iofirewirepcrspace/1813189-init.md)
  initializes the IOFireWirePCRSpace object
- [readInputMasterPlug](iofirewirepcrspace/1813201-readinputmasterplug.md)
  Returns the current value of the primary input plug.
- [readInputPlug](iofirewirepcrspace/1813218-readinputplug.md)
  returns the current value of an input plug.
- [readOutputMasterPlug](iofirewirepcrspace/1813228-readoutputmasterplug.md)
  Returns the current value of the primary output plug.
- [readOutputPlug](iofirewirepcrspace/1813239-readoutputplug.md)
  returns the current value of an output plug.
- [setAVCTargetSpacePointer](iofirewirepcrspace/1813255-setavctargetspacepointer.md)
- [updateInputMasterPlug](iofirewirepcrspace/1813265-updateinputmasterplug.md)
  Updates the value of the primary input plug (simulating a lock transaction).
- [updateInputPlug](iofirewirepcrspace/1813280-updateinputplug.md)
  updates the value of an input plug (simulating a lock transaction).
- [updateOutputMasterPlug](iofirewirepcrspace/1813299-updateoutputmasterplug.md)
  Updates the value of the primary output plug (simulating a lock transaction).
- [updateOutputPlug](iofirewirepcrspace/1813322-updateoutputplug.md)
  updates the value of an output plug (simulating a lock transaction).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirepcrspace/1813173-getpcraddressspace)*