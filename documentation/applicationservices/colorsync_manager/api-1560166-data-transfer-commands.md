# Data Transfer Commands

**Framework**: Application Services

Specify commands for caller-supplied ColorSync data transfer functions.

#### Overview

When your application calls the function [`CMFlattenProfile`](colorsync_manager/1804897-cmflattenprofile.md), any of the functions in the group [`Accessing Profile Elements`](colorsync_manager#1666059.md), or the PostScript-related functions of type [`Working With PostScript`](colorsync_manager#1666896.md), the selected CMM—or, for the `CMUnflattenProfile` function, the ColorSync Manager—calls the flatten function you supply to transform profile data. The call passes one of the command constants defined by this enumeration.

Your application provides a pointer to your ColorSync data transfer function as a parameter to the functions. The ColorSync Manager or the CMM calls your data transfer function, passing the command in the `command` parameter. For more information on the flatten function, see [`CMFlattenProfile`](colorsync_manager/1804897-cmflattenprofile.md). 

## Topics

### Constants
- [var cmOpenReadSpool: Int](cmopenreadspool.md)
  Directs the function to begin the process of reading data.
- [var cmOpenWriteSpool: Int](cmopenwritespool.md)
  Directs the function to begin the process of writing data.
- [var cmReadSpool: Int](cmreadspool.md)
  Directs the function to read the number of bytes specified by the `CMFlattenProcPtr` function’s `size` parameter. 
- [var cmWriteSpool: Int](cmwritespool.md)
  Directs the function to write the number of bytes specified by the `CMFlattenProcPtr` function’s `size` parameter. 
- [var cmCloseSpool: Int](cmclosespool.md)
  Directs the function to complete the data transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560166-data_transfer_commands)*