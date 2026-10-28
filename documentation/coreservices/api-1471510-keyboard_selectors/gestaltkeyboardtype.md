# gestaltKeyboardType

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltKeyboardType = 'kbd '
```

## Discussion

The selector you pass to the `Gestalt` function to determine the type of the keyboard.

If the Apple Desktop Bus (ADB) is in use, there may be multiple keyboards or other ADB devices attached to the machine. The `gestaltKeyboardType` selector identifies only the type of the keyboard on which the last keystroke occurred. 

You cannot use this selector to find out what ADB devices are connected. For that, you can use the Apple Desktop Bus Manager. Note that the ADB keyboard types described by `Gestalt` do not necessarily map directly to ADB device handler IDs.

Future support for the `gestaltKeyboardType` selector is not guaranteed. To determine the type of the keyboard last touched without using `Gestalt`, check the system global variable `KbdType`.

If the Gestalt Manager does not recognize the keyboard type, it returns an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471510-keyboard_selectors/gestaltkeyboardtype)*