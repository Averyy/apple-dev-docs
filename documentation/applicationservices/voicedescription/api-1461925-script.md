# script

**Framework**: Application Services  
**Kind**: structp

The encoding code of the text that the voice can process.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var script: Int16
```

#### Discussion

Note that this field contains a 16-bit value. You can use any of the 16-bit values described in External String Encodings or [`CFStringBuiltInEncodings`](https://developer.apple.com/documentation/corefoundation/cfstringbuiltinencodings). However, if you need to use a 32-bit value, such as UTF8, you pass the value in the first array element of the [`reserved`](voicedescription/1462772-reserved.md) field, and you also need to specify `-1` or [`kCFStringEncodingInvalidId`](https://developer.apple.com/documentation/corefoundation/kcfstringencodinginvalidid) in the [`script`](voicedescription/1461925-script.md) field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/voicedescription/1461925-script)*