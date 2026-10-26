# Key State Entry Formats

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Indicate the format for dead-key state records.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kUCKeyStateEntryTerminalFormat](./api-1390376-key_state_entry_formats/kuckeystateentryterminalformat.md)
  Specifies that the entry format is that of a structure of type [`UCKeyStateEntryTerminal`](./uckeystateentryterminal.md). Use this format for simple (single) dead-key states, as in the U.S. keyboard layout.
- [kUCKeyStateEntryRangeFormat](./api-1390376-key_state_entry_formats/kuckeystateentryrangeformat.md)
  Specifies that the entry format is that of a structure of type [`UCKeyStateEntryRange`](./uckeystateentryrange.md). Use this format for complex (multiple) dead-key states, as in the hex input and Hangul input keyboard layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390376-key_state_entry_formats)*