# UCKeyTranslate(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Converts a combination of a virtual key code, a modifier key state, and a dead-key state into a string of one or more Unicode characters.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func UCKeyTranslate(_ keyLayoutPtr: UnsafePointer<UCKeyboardLayout>!, _ virtualKeyCode: UInt16, _ keyAction: UInt16, _ modifierKeyState: UInt32, _ keyboardType: UInt32, _ keyTranslateOptions: OptionBits, _ deadKeyState: UnsafeMutablePointer<UInt32>!, _ maxStringLength: Int, _ actualStringLength: UnsafeMutablePointer<Int>!, _ unicodeString: UnsafeMutablePointer<UniChar>!) -> OSStatus
```

#### Return_value

A result code. If you pass `NULL` in the `keyLayoutPtr` parameter, `UCKeyTranslate` returns `paramErr`. The `UCKeyTranslate` function also returns `paramErr` for an invalid `'uchr`' resource format or for invalid `virtualKeyCode` or `keyAction` values, as well as for `NULL` pointers to output values. The result `kUCOutputBufferTooSmall` (-25340) is returned for an output string length greater than `maxStringLength`.

#### Discussion

Use of the `UCKeyTranslate` function is discouraged in applications. Use the `NSEvent` method [`characters(byApplyingModifiers:)`](https://developer.apple.com/documentation/appkit/nsevent/characters(byapplyingmodifiers:)) in its place to process mouse and keyboard-related events.

The `UCKeyTranslate` function uses the data in a Unicode keyboard-layout (`'uchr'`) resource to map a combination of virtual key code and modifier key state to a sequence of up to 255 Unicode characters. This mapping process depends on, and may update, a dead key state; the `UCKeyTranslate` function and the `'uchr'` resource support multiple dead keys. The mapping may also depend on the specific type of key action and the type of physical keyboard being used. The `UCKeyTranslate` function supports non-ADB keyboards, an extensible set of modifier keys, and other possible extensions.

In most cases, your application does not need to call the `UCKeyTranslate` function, since the Text Services Manager automatically calls it on your behalf to handle input from a Unicode keyboard layout. However, there may be some circumstances in which your application should call `UCKeyTranslate`. For example, your application may need to determine what character(s) would have been generated for the virtual key code in the current key-down event if a different modifier-and-key combination had been used.

The basic process by which `UCKeyTranslate` uses the `'uchr'` resource to translate virtual key codes into Unicode characters is detailed in the following steps:

1. The bit pattern specifying the modifier key state is mapped by the `UCKeyModifiersToTableNum` structure to a table number.
2. The table number maps to an offset within a `UCKeyToCharTableIndex` structure that refers to the actual key-code-to-character tables.
3. The key-code-to-character tables map the virtual key code to `UCKeyOutput` values, for which there are two possibilities: - If bits 15 and 14 of the `UCKeyOutput` value are 01, the `UCKeyOutput` value is an index into the offsets contained in a `UCKeyStateRecordsIndex` structure. If this occurs, the mapping process for the virtual key code continues on to the next step
- Otherwise, the `UCKeyOutput` value produces one or more Unicode characters, either directly or via reference to a `UCKeySequenceDataIndex` structure. This ends the mapping process for a given virtual key code.
4. The offsets in a `UCKeyStateRecordsIndex` structure refer to `UCKeyStateRecord` dead-key state records.
5. The dead-key state records map from the current dead-key state to one or more Unicode characters to be output or the following dead-key state (if any). The mapping process for a given virtual key code may end with the dead-key state record or, if there is no dead-key state record entry for the key code, with a default state terminator, as specified in the resource’s `UCKeyStateTerminators` table.

## Parameters

- `keyLayoutPtr`: A pointer to the first element in a resource of type  . Pass a pointer to the   resource that you wish the   function to use when converting the virtual key code to a Unicode character. The resource handle associated with this pointer need not be locked, since the   function does not move memory. 
- `virtualKeyCode`: An unsigned 16-bit integer. Pass a value specifying the virtual key code that is to be translated. For ADB keyboards, virtual key codes are in the range from 0 to 127. 
- `keyAction`: An unsigned 16-bit integer. Pass a value specifying the current key action. See   for descriptions of possible values.
- `modifierKeyState`: An unsigned 32-bit integer. Pass a bit mask indicating the current state of various modifier keys. You can obtain this value from the modifiers field of the event record as follows:
- `keyboardType`: An unsigned 32-bit integer. Pass a value specifying the physical keyboard type (that is, the keyboard shape shown by Key Caps). You can call the function   for this value. 
- `keyTranslateOptions`: A bit mask of options for controlling the   function. See   and   for descriptions of possible values. 
- `deadKeyState`: A pointer to an unsigned 32-bit value, initialized to zero. The   function uses this value to store private information about the current dead key state.
- `maxStringLength`: A value of type  . Pass the number of 16-bit Unicode characters that are contained in the buffer passed in the   parameter. This may be a value of up to 255, although it would be rare to get more than 4 characters. 
- `actualStringLength`: A pointer to a value of type  . On return this value contains the actual number of Unicode characters placed into the buffer passed in the   parameter.
- `unicodeString`: An array of values of type  . Pass a pointer to the buffer whose sized is specified in the   parameter. On return, the buffer contains a string of Unicode characters resulting from the virtual key code being handled. The number of characters in this string is less than or equal to the value specified in the   parameter. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390584-uckeytranslate)*