# kUCKeyTranslateNoDeadKeysMask

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

The mask for the bit that turns off dead-key processing. This prevents setting any new dead-key states, but allows completion of any dead-key states currently in effect.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
kUCKeyTranslateNoDeadKeysMask = 1L << kUCKeyTranslateNoDeadKeysBit
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390568-key_translation_options_mask/kuckeytranslatenodeadkeysmask)*