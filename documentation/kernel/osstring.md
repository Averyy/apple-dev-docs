# OSString

**Framework**: Kernel  
**Kind**: cl

OSString wraps a C string in a C++ object for use in Libkern collections.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class OSString : OSObject
```

#### Overview

OSString is a container class for managing arrays of characters. An OSString normally maintains its own character buffer and allows changes, but you can create an "immutable" OSString that references an external C string buffer using the "NoCopy" creator functions. Functions called to change the contents of an immutable OSString will fail.

OSString makes no provisions for different character encodings and assumes that a string is a nul-terminated sequence of single-byte characters. User-space code must either assume an encoding (typically ASCII or UTF-8) or determine it in some other way (such as an IORegistryEntry property).

OSString's intended use is as a reference-counted object container for a C string and little more. While OSString provides full access to the underlying C string, it provides little in the way of string object manipulation; there are no append or insert functions, only a set-character function. If you need to manipulate OSStrings, it's generally best to get the C strings, alter them as necessary, and create a new OSString object from the resulting C string.

With very few exceptions in the I/O Kit, all Libkern-based C++ classes, functions, and macros are  to use in a primary interrupt context. Consult the I/O Kit documentation related to primary interrupts for more information.

OSString provides no concurrency protection; it's up to the usage context to provide any protection necessary. Some portions of the I/O Kit, such as IORegistryEntry, handle synchronization via defined member functions for setting properties.

## Topics

### Miscellaneous
- [free](osstring/1808271-free.md)
  Deallocates or releases any resources used by the OSString instance.
- [getChar](osstring/1808273-getchar.md)
  Returns the character at a given index in the string object.
- [getCStringNoCopy](osstring/1808275-getcstringnocopy.md)
  Returns a pointer to the internal C string buffer.
- [getLength](osstring/1808278-getlength.md)
  Returns the number of characters in the OSString object.
- [initWithCString](osstring/1808281-initwithcstring.md)
  Initializes an OSString from a C string.
- [initWithCStringNoCopy](osstring/1808284-initwithcstringnocopy.md)
  Initializes an immutable OSString to share the provided C string buffer.
- [initWithString](osstring/1808286-initwithstring.md)
  Initializes an OSString from another OSString.
- [isEqualTo(const char *)](osstring/1808288-isequalto.md)
  Tests the equality of an OSString object with a C string.
- [isEqualTo(const OSData *)](osstring/1808292-isequalto.md)
  Tests the equality of an OSData object and the OSString instance.
- [isEqualTo(const OSMetaClassBase *)](osstring/1808295-isequalto.md)
  Tests the equality of an OSString object to an arbitrary object.
- [isEqualTo(const OSString *)](osstring/1808297-isequalto.md)
  Tests the equality of two OSString objects.
- [serialize](osstring/1808298-serialize.md)
  Archives the receiver into the provided OSSerialize object.
- [setChar](osstring/1808300-setchar.md)
  Replaces a character at a given index in the string object.
- [withCString](osstring/1808301-withcstring.md)
  Creates and initializes an OSString from a C string.
- [withCStringNoCopy](osstring/1808304-withcstringnocopy.md)
  Creates and initializes an immutable OSString that shares the provided C string buffer.
- [withString](osstring/1808306-withstring.md)
  Creates and initializes an OSString from another OSString.
### Instance Methods
- [- free](../driverkit/osstring/free.md)
- [- getCStringNoCopy](../driverkit/osstring/getcstringnocopy.md)
  Returns a pointer to the OSString object’s internal data buffer.
- [- getChar](osstring/1490409-getchar.md)
- [- getLength](../driverkit/osstring/getlength.md)
  Returns length of string not including null terminator.
- [- getMetaClass](osstring/1490433-getmetaclass.md)
- [- initWithCString](osstring/1490404-initwithcstring.md)
- [- initWithCStringNoCopy](osstring/1490434-initwithcstringnocopy.md)
- [- initWithString](osstring/1490425-initwithstring.md)
- [- isEqualTo](../driverkit/osstring/isequalto-5paj5.md)
  Compares the string with an OSString.
- [- isEqualTo](../driverkit/osstring/isequalto-1uq1f.md)
  Compares the string with an OSData.
- [- isEqualTo](../driverkit/osstring/isequalto-2rg80.md)
  Compares the string with a c-string.
- [- isEqualTo](../driverkit/osstring/isequalto-712xj.md)
  Compares the string with an OSObject
- [- serialize](osstring/1490429-serialize.md)
- [- setChar](osstring/1490414-setchar.md)
### Type Methods
- [+ withCString](../driverkit/osstring/withcstring-4wsql.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withCString](../driverkit/osstring/withcstring-721oh.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [+ withCStringNoCopy](../driverkit/osstring/withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withString](../driverkit/osstring/withstring.md)
  Allocates an OSString object with a copy of an OString object.

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [OSBoolean](osboolean.md)
  OSBoolean wraps a boolean value in a C++ object for use in Libkern collections.
- [OSNumber](osnumber.md)
  OSNumber wraps an integer value in a C++ object for use in Libkern collections.
- [OSData](osdata.md)
  OSData wraps an array of bytes in a C++ object for use in Libkern collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring)*