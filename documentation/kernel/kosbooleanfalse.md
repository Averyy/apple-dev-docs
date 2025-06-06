# kOSBooleanFalse

**Framework**: Kernel  
**Kind**: data

The OSBoolean constant for `false`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
OSBoolean *const & kOSBooleanFalse;
```

#### Discussion

kOSBooleanFalse is the OSBoolean constant for `false`. This object does not need to be retained or released (but it can be). Comparisons of the form `booleanObject == kOSBooleanFalse` are acceptable and are equivalent to `booleanObject->getValue() == false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kosbooleanfalse)*