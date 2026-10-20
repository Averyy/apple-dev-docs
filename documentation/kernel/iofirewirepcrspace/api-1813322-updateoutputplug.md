# updateOutputPlug

**Framework**: Kernel  
**Kind**: instm

updates the value of an output plug (simulating a lock transaction).

## Declaration

```cpp
virtual IOReturn updateOutputPlug(
 UInt32plug,
 UInt32oldVal,
 UInt32newVal);
```

## Parameters

- `plug`: value returned by allocateOutputPlug.
- `oldVal`: value returned by readOutputPlug.
- `newVal`: new value to store in plug if it's current value is oldVal.

## See Also

### Miscellaneous
- [allocateInputPlug](./api-1813120-allocateinputplug.md)
  allocates an input plug.
- [allocateOutputPlug](./api-1813128-allocateoutputplug.md)
  allocates an output plug.
- [clearAllP2PConnections](./api-1813138-clearallp2pconnections.md)
- [freeInputPlug](./api-1813150-freeinputplug.md)
  deallocates an input plug.
- [freeOutputPlug](./api-1813163-freeoutputplug.md)
  deallocates an output plug.
- [getPCRAddressSpace](./api-1813173-getpcraddressspace.md)
  returns the IOFireWirePCRSpace object for the given FireWire bus
- [init](./api-1813189-init.md)
  initializes the IOFireWirePCRSpace object
- [readInputMasterPlug](./api-1813201-readinputmasterplug.md)
  Returns the current value of the primary input plug.
- [readInputPlug](./api-1813218-readinputplug.md)
  returns the current value of an input plug.
- [readOutputMasterPlug](./api-1813228-readoutputmasterplug.md)
  Returns the current value of the primary output plug.
- [readOutputPlug](./api-1813239-readoutputplug.md)
  returns the current value of an output plug.
- [setAVCTargetSpacePointer](./api-1813255-setavctargetspacepointer.md)
- [updateInputMasterPlug](./api-1813265-updateinputmasterplug.md)
  Updates the value of the primary input plug (simulating a lock transaction).
- [updateInputPlug](./api-1813280-updateinputplug.md)
  updates the value of an input plug (simulating a lock transaction).
- [updateOutputMasterPlug](./api-1813299-updateoutputmasterplug.md)
  Updates the value of the primary output plug (simulating a lock transaction).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirepcrspace/1813322-updateoutputplug)*