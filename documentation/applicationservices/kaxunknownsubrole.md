# kAXUnknownSubrole

**Framework**: Application Services  
**Kind**: data  
**Role**: Global Variable

**Availability**:
- macOS 10.2+

## Declaration

```swift
var kAXUnknownSubrole: String { get }
```

```c
#define kAXUnknownSubrole
```

## Discussion

A subrole for an unknown type of window. A window should include a subrole to further define its type. If your window does not conform to an existing subrole, you can use the unknown subrole. Alternatively, you can return the `eventNotHandledErr` error when your window is asked for its subrole.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/kaxunknownsubrole)*