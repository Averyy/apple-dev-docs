# Key Translation Options Mask

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies the mask for the bit that controls dead-key processing state.

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
- [kUCKeyTranslateNoDeadKeysMask](./api-1390568-key_translation_options_mask/kuckeytranslatenodeadkeysmask.md)
  The mask for the bit that turns off dead-key processing. This prevents setting any new dead-key states, but allows completion of any dead-key states currently in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390568-key_translation_options_mask)*