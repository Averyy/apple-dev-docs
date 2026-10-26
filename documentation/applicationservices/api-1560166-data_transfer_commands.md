# Data Transfer Commands

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Specify commands for caller-supplied ColorSync data transfer functions.

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [cmOpenReadSpool](./api-1560166-data_transfer_commands/cmopenreadspool.md)
  Directs the function to begin the process of reading data.
- [cmOpenWriteSpool](./api-1560166-data_transfer_commands/cmopenwritespool.md)
  Directs the function to begin the process of writing data.
- [cmReadSpool](./api-1560166-data_transfer_commands/cmreadspool.md)
  Directs the function to read the number of bytes specified by the `CMFlattenProcPtr` function’s `size` parameter. 
- [cmWriteSpool](./api-1560166-data_transfer_commands/cmwritespool.md)
  Directs the function to write the number of bytes specified by the `CMFlattenProcPtr` function’s `size` parameter. 
- [cmCloseSpool](./api-1560166-data_transfer_commands/cmclosespool.md)
  Directs the function to complete the data transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands)*