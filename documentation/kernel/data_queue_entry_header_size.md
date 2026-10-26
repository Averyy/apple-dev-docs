# DATA_QUEUE_ENTRY_HEADER_SIZE

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

**Availability**:
- macOS 10.0+

## Declaration

```c
#define DATA_QUEUE_ENTRY_HEADER_SIZE
```

#### Discussion

Represents the size of the data queue entry header independent of the actual size of the data in the entry. This is the overhead of each entry in the queue. The total size of an entry is equal to this value plus the size stored in the entry's size field (in IODataQueueEntry).


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/data_queue_entry_header_size)*