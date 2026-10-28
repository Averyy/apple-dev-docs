# setParentKnowsState

**Framework**: Kernel  
**Kind**: instm

Sets the stateKnown variable.

## Declaration

```c
void setParentKnowsState (
 bool );
```

## Overview

Called by the parent when the object is created and called by the child when it discovers that the parent now knows its state.

## See Also

### Miscellaneous
- [childHasRequestedPower](./api-1810220-childhasrequestedpower.md)
  Return the flag that says whether the child has called requestPowerDomainState.
- [getAwaitingAck](./api-1810241-getawaitingack.md)
  Returns the awaitingAck variable.
- [getDesiredDomainState](./api-1810268-getdesireddomainstate.md)
  Returns the desiredDomainState variable.
- [getPreventIdleSleepFlag](./api-1810287-getpreventidlesleepflag.md)
  Returns the preventIdleSleepFlag variable.
- [getPreventSystemSleepFlag](./api-1810313-getpreventsystemsleepflag.md)
  Returns the preventSystemSleepFlag variable.
- [getReadyFlag](./api-1810329-getreadyflag.md)
  Returns the readyFlag variable.
- [parentCurrentPowerFlags](./api-1810355-parentcurrentpowerflags.md)
  Returns the currentPowerFlags variable.
- [parentKnowsState](./api-1810379-parentknowsstate.md)
  Returns the stateKnown variable.
- [setAwaitingAck](./api-1810405-setawaitingack.md)
  Sets the awaitingAck variable.
- [setChildHasRequestedPower](./api-1810436-setchildhasrequestedpower.md)
  Set the flag that says that the child has called requestPowerDomainState.
- [setDesiredDomainState](./api-1810465-setdesireddomainstate.md)
  Sets the desiredDomainState variable.
- [setParentCurrentPowerFlags](./api-1810489-setparentcurrentpowerflags.md)
  Sets the currentPowerFlags variable.
- [setPreventIdleSleepFlag](./api-1810555-setpreventidlesleepflag.md)
  Sets the preventIdleSleepFlag variable.
- [setPreventSystemSleepFlag](./api-1810587-setpreventsystemsleepflag.md)
  Sets the preventSystemSleepFlag variable.
- [setReadyFlag](./api-1810620-setreadyflag.md)
  Sets the readyFlag variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopowerconnection/1810522-setparentknowsstate)*