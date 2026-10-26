# Profile Access Procedures

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Specify operations used to access profiles.

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
- [cmOpenReadAccess](./api-1560733-profile_access_procedures/cmopenreadaccess.md)
- [cmOpenWriteAccess](./api-1560733-profile_access_procedures/cmopenwriteaccess.md)
  Open the profile for writing. The total size of the profile is specified in the `size` parameter. 
- [cmReadAccess](./api-1560733-profile_access_procedures/cmreadaccess.md)
  Read the number of bytes specified by the `size` parameter.
- [cmWriteAccess](./api-1560733-profile_access_procedures/cmwriteaccess.md)
  Write the number of bytes specified by the `size` parameter.
- [cmCloseAccess](./api-1560733-profile_access_procedures/cmcloseaccess.md)
  Close the profile for reading or writing.
- [cmCreateNewAccess](./api-1560733-profile_access_procedures/cmcreatenewaccess.md)
  Create a new data stream for the profile.
- [cmAbortWriteAccess](./api-1560733-profile_access_procedures/cmabortwriteaccess.md)
  Cancel the current write attempt.
- [cmBeginAccess](./api-1560733-profile_access_procedures/cmbeginaccess.md)
  Begin the process of procedural access. This is always the first operation constant passed to the access procedure. If the call is successful, the `cmEndAccess` operation is guaranteed to be the last call to the procedure.
- [cmEndAccess](./api-1560733-profile_access_procedures/cmendaccess.md)
  End the process of procedural access. This is always the last operation constant passed to the access procedure (unless the `cmBeginAccess` call failed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures)*