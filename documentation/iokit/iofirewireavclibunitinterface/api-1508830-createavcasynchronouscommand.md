# createAVCAsynchronousCommand

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*createAVCAsynchronousCommand)(void *self, const UInt8 *command, UInt32 cmdLen, IOFireWireAVCLibAsynchronousCommandCallback completionCallback, void *pRefCon, IOFireWireAVCLibAsynchronousCommand **ppCommandObject);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508830-createavcasynchronouscommand)*