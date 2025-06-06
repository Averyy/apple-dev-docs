# Profile Access Procedures

**Framework**: Application Services

Specify operations used to access profiles.

#### Overview

When your application calls the `CMOpenProfile`, `CMNewProfile`, `CMCopyProfile`, or `CMNewLinkProfile` functions, it can supply the ColorSync Manager with a profile location structure of type `CMProcedureLocation` to specify a procedure that provides access to a profile. The ColorSync Manager calls your procedure when the profile is created, initialized, opened, read, updated, or closed. The profile access procedure declaration is described in `CMProfileAccessProcPtr`.

When the ColorSync Manager calls your profile access procedure, it passes one of these constants in the `command` parameter to specify an operation. Your procedure must be able to respond to each of these constants. 

## Topics

### Constants
- [var cmOpenReadAccess: Int](cmopenreadaccess.md)
- [var cmOpenWriteAccess: Int](cmopenwriteaccess.md)
  Open the profile for writing. The total size of the profile is specified in the `size` parameter. 
- [var cmReadAccess: Int](cmreadaccess.md)
  Read the number of bytes specified by the `size` parameter.
- [var cmWriteAccess: Int](cmwriteaccess.md)
  Write the number of bytes specified by the `size` parameter.
- [var cmCloseAccess: Int](cmcloseaccess.md)
  Close the profile for reading or writing.
- [var cmCreateNewAccess: Int](cmcreatenewaccess.md)
  Create a new data stream for the profile.
- [var cmAbortWriteAccess: Int](cmabortwriteaccess.md)
  Cancel the current write attempt.
- [var cmBeginAccess: Int](cmbeginaccess.md)
  Begin the process of procedural access. This is always the first operation constant passed to the access procedure. If the call is successful, the `cmEndAccess` operation is guaranteed to be the last call to the procedure.
- [var cmEndAccess: Int](cmendaccess.md)
  End the process of procedural access. This is always the last operation constant passed to the access procedure (unless the `cmBeginAccess` call failed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560733-profile_access_procedures)*