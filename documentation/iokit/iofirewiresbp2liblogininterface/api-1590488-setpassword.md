# setPassword

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the login password.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
IOReturn (*setPassword)(void *self, void *buffer, UInt32 length);
```

## Return Value

Returns kIOReturnSuccess on success.

## Discussion

Sets the login password using a buffer and a length. An alternate version exists that accepts an IOMemoryDescriptor. If the password length is 8 or less the password is copied directly into the login orb. If the length is greater than 8 the buffer is referenced by address in the login ORB. In this case the buffer is not copied and should remain allocated for the duration of the login attempt.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `buffer`: a pointer to the password buffer.
- `length`: the length in bytes of the password buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590488-setpassword)*