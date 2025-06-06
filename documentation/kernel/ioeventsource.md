# IOEventSource

**Framework**: Kernel  
**Kind**: cl

Abstract class for all work-loop event sources.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOEventSource : OSObject
```

#### Overview

The IOEventSource declares the abstract super class that all event sources must inherit from if an IOWorkLoop is to receive events from them.

An event source can represent any event that should cause the work-loop of a device to wake up and perform work. Two examples of event sources are the IOInterruptEventSource which delivers interrupt notifications and IOCommandGate which delivers command requests.

A kernel module can always use the work-loop model for serialising access to anything at all. The IOEventSource is used for communicating events to the work-loop, and the chain of event sources should be used to walk the possible event sources and demultipex them. Note a particular instance of an event source may only be a member of 1 linked list chain. If you need to move it between chains than make sure it is removed from the original chain before attempting to move it.

The IOEventSource makes no attempt to maintain the consistency of its internal data across multi-threading. It is assumed that the user of these basic tools will protect the data that these objects represent in some sort of device wide instance lock. For example the IOWorkLoop maintains the event chain by using an IOCommandGate and thus single threading access to its state.

All subclasses of IOEventSource that wish to perform work on the work-loop thread are expected to implement the checkForWork() member function. As of macOS, 10.7 (Darwin 11), checkForWork is no longer pure virtual, and should not be overridden if there is no work to be done.

checkForWork() is the key method in this class. It is called by some work-loop when convienient and is expected to evaluate its internal state and determine if an event has occurred since the last call. In the case of an event having occurred then the instance defined target(owner)/action will be called. The action is stored as an ordinary C function pointer but the first parameter is always the owner. This means that a C++ member function can be used as an action function though this depends on the ABI.

Although the eventChainNext variable contains a reference to the next event source in the chain this reference is not retained. The list 'owner' i.e. the client that creates the event, not the work-loop, is expected to retain the source.

## Topics

### Miscellaneous
- [checkForWork](ioeventsource/1810760-checkforwork.md)
  Virtual member function used by IOWorkLoop for work scheduling.
- [disable](ioeventsource/1810784-disable.md)
  Disable event source.
- [enable](ioeventsource/1810807-enable.md)
  Enable event source.
- [getAction](ioeventsource/1810828-getaction.md)
  Get'ter for $link action variable.
- [getNext](ioeventsource/1810847-getnext.md)
  Get'ter for $link eventChainNext variable.
- [getWorkLoop](ioeventsource/1810872-getworkloop.md)
  Get'ter for $link workLoop variable.
- [init](ioeventsource/1810895-init.md)
  Primary initialiser for the IOEventSource class.
- [isEnabled](ioeventsource/1810913-isenabled.md)
  Get'ter for $link enable variable.
- [onThread](ioeventsource/1810935-onthread.md)
  Convenience function for workLoop->onThread.
- [setAction](ioeventsource/1810952-setaction.md)
  Set'ter for $link action variable.
- [setNext](ioeventsource/1810967-setnext.md)
  Set'ter for $link eventChainNext variable.
- [setWorkLoop](ioeventsource/1810984-setworkloop.md)
  Set'ter for $link workLoop variable.
### Callbacks
- [Action](ioworkloop/action.md)
### Constants
- [Miscellaneous Defines](ioeventsource/miscellaneous_defines.md)
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [workLoop](ioeventsource/workloop.md)
- [reserved](ioeventsource/reserved.md)
- [refcon](ioeventsource/refcon.md)
- [owner](ioeventsource/owner.md)
- [eventChainNext](ioeventsource/eventchainnext.md)
- [enabled](ioeventsource/enabled.md)
- [action](ioeventsource/action-8l7.md)
### Instance Methods
- [- checkForWork](ioeventsource/1520975-checkforwork.md)
- [- closeGate](ioeventsource/1520952-closegate.md)
- [- disable](ioeventsource/1520972-disable.md)
- [- enable](ioeventsource/1520958-enable.md)
- [- free](ioeventsource/1520964-free.md)
- [- getAction](ioeventsource/1520956-getaction.md)
- [- getActionBlock](ioeventsource/2967267-getactionblock.md)
- [- getMetaClass](ioeventsource/1520955-getmetaclass.md)
- [- getNext](ioeventsource/1520966-getnext.md)
- [- getRefcon](ioeventsource/2967268-getrefcon.md)
- [- getWorkLoop](ioeventsource/1520961-getworkloop.md)
- [- init](ioeventsource/1520960-init.md)
- [- isEnabled](ioeventsource/1520957-isenabled.md)
- [- onThread](ioeventsource/1520968-onthread.md)
- [- openGate](ioeventsource/1520969-opengate.md)
- [- setAction](ioeventsource/1520974-setaction.md)
- [- setActionBlock](ioeventsource/2967269-setactionblock.md)
- [- setNext](ioeventsource/1520962-setnext.md)
- [- setRefcon](ioeventsource/2967270-setrefcon.md)
- [- setWorkLoop](ioeventsource/1520953-setworkloop.md)
- [- signalWorkAvailable](ioeventsource/1520948-signalworkavailable.md)
- [- sleepGate](ioeventsource/1520954-sleepgate.md)
- [- sleepGate](ioeventsource/3516453-sleepgate.md)
- [- tryCloseGate](ioeventsource/1520976-tryclosegate.md)
- [- wakeupGate](ioeventsource/1520950-wakeupgate.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOCommandPool](iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommandGate](iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IOCommand](iocommand.md)
  This class is an abstract class which represents an I/O command.
- [IODispatchSource](iodispatchsource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioeventsource)*