# stateEntryFormat

**Framework**: Core Services  
**Kind**: structp

An unsigned 16-bit integer specifying the format of the data in the `stateEntryData` field’s array. This should be 0 if the `stateEntryCount` field is set to 0. Currently available values are `kUCKeyStateEntryTerminalFormat` and `kUCKeyStateEntryRangeFormat`; see [`Key State Entry Formats`](carbon_core/unicode_utilities/1390376-key_state_entry_formats.md) for descriptions of these values.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var stateEntryFormat: UInt16
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeystaterecord/1390450-stateentryformat)*