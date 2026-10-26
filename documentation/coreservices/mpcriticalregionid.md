# MPCriticalRegionID

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Represents a critical region ID, which Multiprocessing Services uses to manipulate critical regions. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueMPCriticalRegionID *MPCriticalRegionID;
```

#### Discussion

You obtain a critical region ID by calling the function [`MPCreateCriticalRegion`](./api-1585663-mpcreatecriticalregion.md). 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpcriticalregionid)*