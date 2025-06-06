# PMCreateSession(_:)

**Framework**: Application Services  
**Kind**: func

Creates and initializes a printing session object and creates a context for printing operations.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func PMCreateSession(_ printSession: UnsafeMutablePointer<PMPrintSession?>) -> OSStatus
```

#### Return_value

A result code. See [`Result Codes`](core_printing#1670007.md).

#### Discussion

This function allocates memory for a new printing session object in your application’s memory space and sets its reference count to 1. The new printing session object is initialized with information that the printing system uses for a print job.

## Parameters

- `printSession`: A pointer to your   variable. On return, the variable refers to a new printing session object. You are responsible for releasing the printing session object with the function  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1463247-pmcreatesession)*