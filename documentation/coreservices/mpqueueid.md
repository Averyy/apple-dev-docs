# MPQueueID

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Represents a queue ID, which Multiprocessing Services uses to manipulate message queues.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueMPQueueID *MPQueueID;
```

## Discussion

You obtain a queue ID by calling the function [`MPCreateQueue`](./api-1585694-mpcreatequeue.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpqueueid)*