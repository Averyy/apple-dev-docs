# MPCoherenceID

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Represents a memory coherence group. 

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef struct OpaqueMPCoherenceID *MPCoherenceID;
```

## Discussion

A coherence group is the set of processors and other bus controllers that have cache-coherent access to memory. Mac OS 9 defines only one coherence group, which is all the processors that can access internal memory (RAM). Other coherence groups are possible; for example, a PCI card with its own memory and processors can comprise a coherence group.  


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpcoherenceid)*