# CMHandleLocation

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains a handle specification for a profile stored in relocatable memory. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMHandleLocation {
    ...
} CMHandleLocation;
```

#### Overview

Your application uses the `CMHandleLocation` structure to provide a handle specification for a profile stored in relocatable memory. You provide the handle specification structure in the `CMProfileLocation` structure’s `u` field to specify an existing profile or a profile to be created. 

## Topics

### Instance Properties
- [h](./cmhandlelocation/api-1560567-h.md)
  A data structure of type `Handle` containing a handle that indicates the location of a profile in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmhandlelocation)*