# Key Translation Options Flag

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Indicates the dead-key processing state.

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
- [kUCKeyTranslateNoDeadKeysBit](./api-1390507-key_translation_options_flag/kuckeytranslatenodeadkeysbit.md)
  The bit number of the bit that turns off dead-key processing. This prevents setting any new dead-key states, but allows completion of any dead-key states currently in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390507-key_translation_options_flag)*