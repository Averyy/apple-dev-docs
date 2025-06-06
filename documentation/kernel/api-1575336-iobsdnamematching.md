# IOBSDNameMatching

**Framework**: Kernel  
**Kind**: func

Create a matching dictionary that specifies an IOService match based on BSD device name.

**Availability**:
- macOS 10.0+

## Declaration

```swift
OSDictionary * IOBSDNameMatching(const char *name);
```

#### Return_value

The matching dictionary created, is returned on success, or zero on failure. The dictionary is commonly passed to IOServiceGetMatchingServices or IOServiceAddNotification which will consume a reference, otherwise it should be released with CFRelease by the caller.

#### Discussion

IOServices that represent BSD devices have an associated BSD name. This function creates a matching dictionary that will match IOService's with a given BSD name.

## Parameters

- `masterPort`: The primary port obtained from IOMasterPort(). Pass kIOMasterPortDefault to look up the default primary port.
- `options`: No options are currently defined.
- `bsdName`: The BSD name, as a const char *.

## See Also

- [IORegistryEntry](ioregistryentry.md)
  The base class for all objects in the registry.
- [IORegistryIterator](ioregistryiterator.md)
  An iterator over the registry.
- [IOPrintPlane](1558295-ioprintplane.md)
- [Registry Utilities](iokit_fundamentals/registry_utilities.md)
- [Registry Keys](iokit_fundamentals/registry_keys.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575336-iobsdnamematching)*