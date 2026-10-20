# keyStateTerminators

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

An array of default dead-key state terminators, described as values of type [`UCKeyCharSeq`](../uckeycharseq.md); the value `keyStateTerminators[0]` is the terminator for state 1, and so on. 

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var keyStateTerminators: UCKeyCharSeq
```

```c
UCKeyCharSeq keyStateTerminators[1];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeystateterminators/1390409-keystateterminators)*