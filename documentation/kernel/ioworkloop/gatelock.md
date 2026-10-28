# gateLock

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```c
IORecursiveLock *gateLock;
```

## Overview

Mutual exclusion lock that is used by close and open Gate functions. This is a recursive lock, which allows multiple layers of code to share a single IOWorkLoop without deadlock. This is common in IOKit since threads of execution tend to follow the service plane in the IORegistry, and multiple objects along the call path may acquire the gate for the same (shared) workloop.

## See Also

### Instance Variables
- [workToDoLock](./worktodolock.md)
- [workToDo](./worktodo.md)
- [workThread](./workthread.md)
- [reserved](./reserved.md)
- [loopRestart](./looprestart.md)
- [eventChain](./eventchain.md)
- [controlG](./controlg.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioworkloop/gatelock)*