# kMDQuerySynchronous

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

Specifies that a query should block during the initial gather phase. The query’s run loop will run in the default mode. If this option is not specified the query function returns immediately after starting the query asynchronously.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
kMDQuerySynchronous = 1
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mdqueryoptionflags/kmdquerysynchronous)*