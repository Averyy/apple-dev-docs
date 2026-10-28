# SetCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Set the completion handler to be called once the command completes asynchronous execution .

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*SetCallback)(IOFireWireLibCommandRef self, IOFireWireLibCommandCallback inCallback);
```

## Discussion

Availability: (for interfaces obtained with ID)

|  | `kIOFireWireAsyncStreamCommandInterfaceID` | YES |
| --- | --- | --- |
|  | `kIOFireWireCompareSwapCommandInterfaceID` | YES |
|  | `kIOFireWireWriteQuadletCommandInterfaceID` | YES |
|  | `kIOFireWireReadQuadletCommandInterfaceID` | YES |
|  | `kIOFireWireWriteCommandInterfaceID_v2` | YES |
|  | `kIOFireWireWriteCommandInterfaceID` | YES |
|  | `kIOFireWireReadCommandInterfaceID_v2` | YES |
|  | `kIOFireWireReadCommandInterfaceID` | YES |

## Parameters

- `self`: The command object interface of interest
- `inCallback`: A callback handler. Passing nil forces the command object to execute synchronously.

## See Also

### Miscellaneous
- [Cancel](./api-1555764-cancel.md)
  Cancel command execution
- [GetStatus](./api-1555831-getstatus.md)
  Return command completion status.
- [GetTargetAddress](./api-1555908-gettargetaddress.md)
  Get command target address.
- [GetTransferredBytes](./api-1556096-gettransferredbytes.md)
  Return number of bytes transferred by this command object when it last completed execution.
- [IsExecuting](./api-1555679-isexecuting.md)
  Is this command object currently executing?
- [SetGeneration](./api-1555786-setgeneration.md)
  Set FireWire bus generation for which the command object shall be valid. If the failOnReset attribute has been set, the command will only be considered for execution during the bus generation specified by this function.
- [SetQuads](./api-1555636-setquads.md)
- [SetRefCon](./api-1555925-setrefcon.md)
  Set the user refCon value. This is the user defined value that will be passed in the refCon argument to the completion function.
- [SetTarget](./api-1555597-settarget.md)
  Set command target address
- [Submit](./api-1555782-submit.md)
- [SubmitWithRefconAndCallback](./api-1555841-submitwithrefconandcallback.md)
  Set the command refCon value and callback handler, and submit the command to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirewritequadletcommandinterface/1556106-setcallback)*