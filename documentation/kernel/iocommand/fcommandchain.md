# fCommandChain

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```swift
queue_chain_t fCommandChain;
```

#### Overview

This variable is used by the current 'owner' to queue the command. During the life cycle of a command it moves through a series of queues. This is the queue pointer for it. Only valid while 'ownership' is clear. For instance a IOCommandPool uses this pointer to maintain its list of free commands. May be manipulated using the kern/queue.h macros


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommand/fcommandchain)*