# DATA_QUEUE_MEMORY_APPENDIX_SIZE

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.5+

## Declaration

```c
#define DATA_QUEUE_MEMORY_APPENDIX_SIZE
```

## Discussion

Represents the size of the data queue memory appendix independent of the actual size of the queue data itself. The total size of the queue memory is equal to this value plus the size of queue header and size of the queue data region which is stored in the queueSize field of IODataQueueMeory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/data_queue_memory_appendix_size)*