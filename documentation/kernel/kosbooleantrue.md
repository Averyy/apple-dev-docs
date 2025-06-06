# kOSBooleanTrue

**Framework**: Kernel  
**Kind**: data

The OSBoolean constant for `true`.

**Availability**:
- macOS 10.0+

## Declaration

```swift
OSBoolean *const & kOSBooleanTrue;
```

#### Discussion

kOSBooleanTrue is the OSBoolean constant for `true`. This object does not need to be retained or released (but it can be). Comparisons of the form `booleanObject == kOSBooleanTrue` are acceptable and are equivalent to `booleanObject->getValue() == true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kosbooleantrue)*