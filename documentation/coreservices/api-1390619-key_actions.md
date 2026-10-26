# Key Actions

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Indicate the current key action.

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
- [kUCKeyActionDown](./api-1390619-key_actions/kuckeyactiondown.md)
  The user is pressing the key.
- [kUCKeyActionUp](./api-1390619-key_actions/kuckeyactionup.md)
  The user is releasing the key.
- [kUCKeyActionAutoKey](./api-1390619-key_actions/kuckeyactionautokey.md)
  The user has the key in an “auto-key” pressed state that is, the user is holding down the key for an extended period of time and is thereby generating multiple key strokes from the single key.
- [kUCKeyActionDisplay](./api-1390619-key_actions/kuckeyactiondisplay.md)
  The user is requesting information for key display, as in the Key Caps application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390619-key_actions)*