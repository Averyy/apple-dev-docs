# setTextContentType(_:)

**Framework**: Watchkit  
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

- The input controller provides suggestions for [`oneTimeCode`](wktextcontenttype/onetimecode.md) content types, when available.
- The input controller displays a number pad for [`telephoneNumber`](wktextcontenttype/telephonenumber.md), [`creditCardNumber`](wktextcontenttype/creditcardnumber.md), [`oneTimeCode`](wktextcontenttype/onetimecode.md), and [`postalCode`](wktextcontenttype/postalcode.md) content types.
- The input controller disables dictation for [`password`](wktextcontenttype/password.md) and [`newPassword`](wktextcontenttype/newpassword.md) content types.
- The Apple Continuity Keyboard autofills data based on the content type. To share login credentials from your web page, set up an associated domain for your watchOS app.

## Parameters

- `textContentType`: The text field’s content type. Passing   clears the content type. For a list of possible content types, see  .

## See Also

- [struct WKTextContentType](wktextcontenttype.md)
  Constants that specify a text field’s semantic meaning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield/settextcontenttype(_:))*