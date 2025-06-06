# cmBeginAccess

**Framework**: Application Services  
**Kind**: data

Begin the process of procedural access. This is always the first operation constant passed to the access procedure. If the call is successful, the `cmEndAccess` operation is guaranteed to be the last call to the procedure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmBeginAccess: Int { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmbeginaccess)*