# createLocalIsochPort

**Framework**: Kernel  
**Kind**: instm

Create a local isochronous port to run the given DCL program

## Declaration

```swift
virtual IOFWLocalIsochPort *createLocalIsochPort(
 bool talking, 
 DCLCommand *opcodes,
 DCLTaskInfo *info = 0, 
 UInt32 startEvent = 0,
 UInt32 startState = 0,
 UInt32 startMask = 0) = 0;
```

#### Return_value

Returns an IOFWLocalIsochPort on success.

## Parameters

- `talking`: Pass true to create a talker port; pass false to create a listener port.
- `opcodes`: A pointer to your DCL program (linked list of DCLCommand structs) To use an IOFWDCL/IOFWDCLPool program, pass the DCLCommand returned by IOFWDCLPool::getProgram().
- `info`: (Optional) Pointer to DCLTaskInfo struct containing additional configuration information. If you have an IOMemoryMap for your DCL program data buffers, pass it here. You can also pass an IOWorkLoop if you want to use your own workloop to handle callbacks for the created port object.
- `startEvent`: Specifies a bus condition on which the port should start receiving/sending packets Must be kFWDCLImmediateEvent, kFWDCLCycleEvent, or kFWDCLSyBitsEvent. Pass kFWDCLImmediateEvent to start without waiting when start() is called. Pass kFWDCLCycleEvent to start() transmitting at a specified bus cycle time. Pass kFWDCLSyBitsEvent (receive only) to start receiving packets once an isochronous packet with a specified sync field arrives.
- `startState`: Pass the value for the desired start condition, as specified by 'startEvent' kFWDCLImmediateEvent: set to 0 kFWDCLCycleEvent: the cycle timer value on which to start processing packets. For talker ports, This value will be masked by 'startMask' and packet processing will be begin on the next cycle whose lowest bits match the masked value. For listener ports, pass a 15-bit value containg to the low order two bits of cycleSeconds and the 13-bit cycleCount on which to start processing packets. kFWDCLSyBitsEvent: The value of the sync field on which to start receive packets. The value will be masked by 'startMask'. For DCLCommand based isoch ports, processing will begin on the first received packet that has an isochronous header sync field matching 'startState'. For IOFWDCL/IOFWDCLPool based ports, processing will pause on each IOFWDCL that has wait set to true until a packet that has an isochronous header sync field matching 'startState' is received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirebus/1811054-createlocalisochport)*