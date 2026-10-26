# UniCharArrayOffset

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Represents the boundary between two characters.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef unsigned long UniCharArrayOffset;
```

#### Discussion

A `UniCharArrayOffset` represents the boundary between two characters. For example, the first character in a buffer lies between offsets 0 and 1. So the first character in the buffer can be referred to as either “offset 0, leading” or “offset 1, trailing.” This distinction is useful when you deal with caret positions. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/unichararrayoffset)*