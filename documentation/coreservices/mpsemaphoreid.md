# MPSemaphoreID

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Represents a semaphore ID, which Multiprocessing Services uses to manipulate semaphores.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueMPSemaphoreID *MPSemaphoreID;
```

#### Discussion

You obtain a semaphore ID by calling the function [`MPCreateSemaphore`](./api-1585569-mpcreatesemaphore.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpsemaphoreid)*