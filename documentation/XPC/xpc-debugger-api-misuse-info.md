# xpc_debugger_api_misuse_info()

**Framework**: Xpc  
**Kind**: func

Returns a pointer to a string that describes the reason XPC aborts the calling process.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func xpc_debugger_api_misuse_info() -> UnsafePointer<CChar>!
```

#### Return Value

A pointer to the human-readable string describing the reason the caller was aborted. If XPC was not responsible for the program’s termination, `NULL` will be returned.

#### Discussion

This function is only callable from within a debugger. It isn’t meant to be called by the program directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_debugger_api_misuse_info())*