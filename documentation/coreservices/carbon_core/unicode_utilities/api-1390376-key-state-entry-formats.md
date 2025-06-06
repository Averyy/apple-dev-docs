# Key State Entry Formats

**Framework**: Core Services

Indicate the format for dead-key state records.

#### Overview

These constants are used in `UCKeyStateRecord` structures to indicate the format for dead-key state records.

## Topics

### Constants
- [var kUCKeyStateEntryTerminalFormat: Int](kuckeystateentryterminalformat.md)
  Specifies that the entry format is that of a structure of type [`UCKeyStateEntryTerminal`](uckeystateentryterminal.md). Use this format for simple (single) dead-key states, as in the U.S. keyboard layout.
- [var kUCKeyStateEntryRangeFormat: Int](kuckeystateentryrangeformat.md)
  Specifies that the entry format is that of a structure of type [`UCKeyStateEntryRange`](uckeystateentryrange.md). Use this format for complex (multiple) dead-key states, as in the hex input and Hangul input keyboard layouts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/carbon_core/unicode_utilities/1390376-key_state_entry_formats)*