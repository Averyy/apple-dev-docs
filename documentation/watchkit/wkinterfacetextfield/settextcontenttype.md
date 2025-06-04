# setTextContentType(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the text field’s semantic meaning.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func setTextContentType(_ textContentType: WKTextContentType?)
```

#### Discussion

The text field’s content type modifies how the text input controller and Apple Continuity Keyboard behave.

- The input controller provides suggestions for [`oneTimeCode`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/onetimecode) content types, when available.
- The input controller displays a number pad for [`telephoneNumber`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/telephonenumber), [`creditCardNumber`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/creditcardnumber), [`oneTimeCode`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/onetimecode), and [`postalCode`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/postalcode) content types.
- The input controller disables dictation for [`password`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/password) and [`newPassword`](https://developer.apple.com/documentation/watchkit/wktextcontenttype/newpassword) content types.
- The Apple Continuity Keyboard autofills data based on the content type. To share login credentials from your web page, set up an associated domain for your watchOS app.

## Parameters

- `textContentType`: The text field’s content type. Passing   clears the content type. For a list of possible content types, see  .

## See Also

- [struct WKTextContentType](wktextcontenttype.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktextcontenttype))
  Constants that specify a text field’s semantic meaning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/settextcontenttype(_:))*