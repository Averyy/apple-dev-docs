# MPEventID

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Represents an event group ID, which Multiprocessing Services uses to manipulate event groups.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueMPEventID *MPEventID;
```

#### Discussion

You obtain an event group ID by calling the function [`MPCreateEvent`](./api-1585702-mpcreateevent.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpeventid)*